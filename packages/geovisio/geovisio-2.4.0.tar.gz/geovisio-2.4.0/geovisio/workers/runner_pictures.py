from fs import open_fs
from fs.path import dirname
from PIL import Image, ImageOps
from flask import current_app
import psycopg
import sentry_sdk
from geovisio import utils
from geovisio import errors
from dataclasses import dataclass
import logging
from contextlib import contextmanager
from enum import Enum
from typing import Any
import threading
from uuid import UUID

import geovisio.utils.filesystems

log = logging.getLogger("geovisio.runner_pictures")

PICTURE_PROCESS_MAX_RETRY = 10  # Number of times a job will be retryed if there is a `RecoverableProcessException` during process (like if the blurring api is not reachable).


class PictureBackgroundProcessor(object):
    def init_app(self, app):
        nb_threads = app.config["EXECUTOR_MAX_WORKERS"]
        self.enabled = nb_threads != 0

        if self.enabled:
            from flask_executor import Executor

            self.executor = Executor(app, name="PicProcessor")
        else:
            import sys

            if "run" in sys.argv or "waitress" in sys.argv:  # hack not to display a frightening warning uselessly
                log.warning("No picture background processor run, no picture will be processed unless another separate worker is run")
                log.warning("A separate process can be run with:")
                log.warning("flask picture-worker")

    def process_pictures(self):
        """
        Ask for a background picture process that will run until not pictures need to be processed
        """
        if self.enabled:
            worker = PictureProcessor(config=current_app.config)
            return self.executor.submit(worker.process_next_pictures)


background_processor = PictureBackgroundProcessor()


class ProcessTask(str, Enum):
    prepare = "prepare"
    delete = "delete"


@dataclass
class DbPicture:
    id: str
    metadata: dict

    def blurred_by_author(self):
        return self.metadata.get("blurredByAuthor", False)


@dataclass
class DbJob:
    reporting_conn: psycopg.Connection
    id: UUID
    pic: DbPicture
    task: ProcessTask


def updateSequenceHeadings(db, sequenceId, relativeHeading=0, updateOnlyMissing=True):
    """Defines pictures heading according to sequence path.
    Database is not committed in this function, to make entry definitively stored
    you have to call db.commit() after or use an autocommit connection.

    Parameters
    ----------
    db : psycopg.Connection
            Database connection
    sequenceId : uuid
            The sequence's uuid, as stored in the database
    relativeHeading : int
            Camera relative orientation compared to path, in degrees clockwise.
            Example: 0° = looking forward, 90° = looking to right, 180° = looking backward, -90° = looking left.
    updateOnlyMissing : bool
            If true, doesn't change existing heading values in database
    """

    db.execute(
        """
		WITH h AS (
			SELECT
				p.id,
				CASE
					WHEN LEAD(sp.rank) OVER othpics IS NULL AND LAG(sp.rank) OVER othpics IS NULL
						THEN NULL
					WHEN LEAD(sp.rank) OVER othpics IS NULL
						THEN (360 + FLOOR(DEGREES(ST_Azimuth(LAG(p.geom) OVER othpics, p.geom)))::int + (%(diff)s %% 360)) %% 360
					ELSE
						(360 + FLOOR(DEGREES(ST_Azimuth(p.geom, LEAD(p.geom) OVER othpics)))::int + (%(diff)s %% 360)) %% 360
				END AS heading
			FROM pictures p
			JOIN sequences_pictures sp ON sp.pic_id = p.id AND sp.seq_id = %(seq)s
			WINDOW othpics AS (ORDER BY sp.rank)
		)
		UPDATE pictures p
		SET heading = h.heading, heading_computed = true
		FROM h
		WHERE h.id = p.id
		"""
        + (
            " AND (p.heading IS NULL OR p.heading = 0 OR p.heading_computed)" if updateOnlyMissing else ""
        ),  # lots of camera have heading set to 0 for unset heading, so we recompute the heading when it's 0 too, even if this could be a valid value
        {"seq": sequenceId, "diff": relativeHeading},
    )


def processPictureFiles(pic: DbPicture, config):
    """Generates the files associated with a sequence picture.

    If needed the image is blurred before the tiles and thumbnail are generated.

    Parameters
    ----------
    db : psycopg.Connection
            Database connection
    dbPic : DbPicture
            The picture metadata extracted from database
    config : dict
            Flask app.config (passed as param to allow using ThreadPoolExecutor)
    """
    skipBlur = pic.blurred_by_author() or config.get("API_BLUR_URL") == None
    fses = config["FILESYSTEMS"]
    fs = fses.permanent if skipBlur else fses.tmp
    picHdPath = utils.pictures.getHDPicturePath(pic.id)

    if not fs.exists(picHdPath):
        # if we were looking for the picture in the temporary fs ans it's not here, we check if it's in the permanent one
        # it can be the case when we try to reprocess an already processed picture
        if fs != fses.permanent and fses.permanent.exists(picHdPath):
            fs = fses.permanent
        else:
            raise Exception(f"Impossible to find picture file: {picHdPath}")

    with fs.openbin(picHdPath) as pictureBytes:
        picture = Image.open(pictureBytes)

        # Create picture folders for this specific picture
        picDerivatesFolder = utils.pictures.getPictureFolderPath(pic.id)
        fses.derivates.makedirs(picDerivatesFolder, recreate=True)
        fses.permanent.makedirs(dirname(picHdPath), recreate=True)

        # Create blurred version if required
        if not skipBlur:
            with sentry_sdk.start_span(description="Blurring picture"):
                try:
                    picture = utils.pictures.createBlurredHDPicture(fses.permanent, config.get("API_BLUR_URL"), pictureBytes, picHdPath)
                except Exception as e:
                    logging.exception(e)
                    raise RecoverableProcessException("Blur API failure: " + errors.getMessageFromException(e)) from e

                # Delete original unblurred file
                geovisio.utils.filesystems.removeFsEvenNotFound(fses.tmp, picHdPath)

                # Cleanup parent folders
                parentFolders = picHdPath.split("/")
                parentFolders.pop()
                checkFolder = parentFolders.pop()
                while checkFolder:
                    currentFolder = "/".join(parentFolders) + "/" + checkFolder
                    if fses.tmp.exists(currentFolder) and fses.tmp.isempty(currentFolder):
                        geovisio.utils.filesystems.removeFsTreeEvenNotFound(fses.tmp, currentFolder)
                        checkFolder = parentFolders.pop()
                    else:
                        checkFolder = False

        else:
            # Make sure image rotation is always applied
            #  -> Not necessary on pictures from blur API, as SGBlur ensures rotation is always applied
            picture = ImageOps.exif_transpose(picture)

        # Always pre-generate thumbnail
        utils.pictures.createThumbPicture(fses.derivates, picture, picDerivatesFolder + "/thumb.jpg", pic.metadata["type"])

        # Create SD and tiles
        if config.get("PICTURE_PROCESS_DERIVATES_STRATEGY") == "PREPROCESS":
            utils.pictures.generatePictureDerivates(
                fses.derivates, picture, pic.metadata, picDerivatesFolder, pic.metadata["type"], skipThumbnail=True
            )


class RecoverableProcessException(Exception):
    def __init__(self, msg):
        super().__init__(msg)


class PictureProcessor:
    stop: bool
    config: dict[Any, Any]

    def __init__(self, config, stop=True) -> None:
        self.config = config
        self.stop = stop
        if threading.current_thread() is threading.main_thread():
            # if worker is in daemon mode, register signals to gracefully stop it
            self._register_signals()

    def process_next_pictures(self):
        try:
            while True:
                r = process_next_picture(self.config)
                if not r:
                    if self.stop:
                        return
                    # no more picture to process
                    # wait a bit until there are some
                    import time

                    time.sleep(1)

        except:
            log.exception("Exiting thread")

    def _register_signals(self):
        import signal

        signal.signal(signal.SIGINT, self._graceful_shutdown)
        signal.signal(signal.SIGTERM, self._graceful_shutdown)

    def _graceful_shutdown(self, *args):
        log.info("Stoping worker, waiting for last picture processing to finish...")
        self.stop = True


def process_next_picture(config):
    with sentry_sdk.start_transaction(op="task", name="process_next_picture"):
        with _get_next_picture_to_process(config) as job:
            if job is None:
                return False
            if job.task == ProcessTask.prepare:
                with sentry_sdk.start_span(description="Processing picture") as span:
                    span.set_data("pic_id", job.pic.id)
                    with utils.time.log_elapsed(f"Processing picture {job.pic.id}"):
                        processPictureFiles(job.pic, config)
            elif job.task == ProcessTask.delete:
                with sentry_sdk.start_span(description="Deleting picture") as span:
                    span.set_data("pic_id", job.pic.id)
                    with utils.time.log_elapsed(f"Deleting picture {job.pic.id}"):
                        _delete_picture(job)
            else:
                raise RecoverableProcessException(f"Unhandled process task: {job.task}")

    return True


@contextmanager
def _get_next_picture_to_process(config):
    """
    Open a new connection and return the next picture to process
    Note: the picture should be used as a context manager to close the connection when we stop using the returned picture.

    The new connection is needed because we lock the `pictures_to_process` for the whole transaction for another worker not to process the same picture
    """
    error = None
    with psycopg.connect(config["DB_URL"], autocommit=True) as locking_transaction:
        with locking_transaction.transaction():
            r = locking_transaction.execute(
                """
            SELECT p.id, pictures_to_process.task, p.metadata
                FROM pictures_to_process
                JOIN pictures p ON p.id = pictures_to_process.picture_id
                ORDER by
                    pictures_to_process.nb_errors,
                    pictures_to_process.ts
                FOR UPDATE of pictures_to_process SKIP LOCKED
                LIMIT 1
            """
            ).fetchone()
            if r is None:
                # Nothing to process
                yield None
            else:
                log.debug(f"Processing {r[0]}")

                db_pic = DbPicture(id=str(r[0]), metadata=r[2])

                with psycopg.connect(config["DB_URL"], autocommit=True) as reporting_conn:
                    job = _initialize_picture_process(reporting_conn, pic=db_pic, task=ProcessTask(r[1]))
                    try:
                        yield job

                        # Finalize the picture process, set the picture status and remove the picture from the queue process
                        _finalize_picture_process(locking_transaction, job)
                        log.debug(f"Picture {db_pic.id} processed")
                    except RecoverableProcessException as e:
                        _mark_process_as_error(locking_transaction, job, e, config, recoverable=True)
                    except InterruptedError as interruption:
                        log.error(f"Interruption received, stoping job {job.id} for picture {db_pic.id}")
                        # starts a new connection, since the current one can be corrupted by the exception
                        with psycopg.connect(config["DB_URL"], autocommit=True) as t:
                            _mark_process_as_error(t, job, interruption, config, recoverable=True)
                        error = interruption
                    except Exception as e:
                        log.exception(f"Impossible to finish job {job.id} for picture {db_pic.id}")
                        _mark_process_as_error(locking_transaction, job, e, config, recoverable=False)

                        # try to finalize the sequence anyway
                        _finalize_sequence_if_last_picture(job)
                        error = e

    # we raise an error after the transaction has been comited to be sure to have the state persisted in the database
    if error:
        raise error


def _finalize_sequence_if_last_picture(job: DbJob):
    r = job.reporting_conn.execute(
        """
		SELECT sp.seq_id AS id FROM sequences_pictures AS sp
		WHERE sp.pic_id = %(id)s
	""",
        {"id": job.pic.id},
    ).fetchone()
    if not r:
        raise Exception(f"impossible to find sequence associated to picture {job.pic.id}")

    seqId = r[0]

    is_sequence_finalized = _is_sequence_finalized(job.reporting_conn, seqId)
    if not is_sequence_finalized:
        log.debug("sequence not finalized")
        return

    with sentry_sdk.start_span(description="Finalizing sequence") as span:
        span.set_data("sequence_id", seqId)
        log.debug(f"Finalizing sequence {seqId}")

        with utils.time.log_elapsed(f"Finalizing sequence {seqId}"):
            # Complete missing headings in pictures
            updateSequenceHeadings(job.reporting_conn, seqId)

            # Change sequence database status in DB
            # Also generates data in computed columns
            job.reporting_conn.execute(
                """
                WITH c AS (
                    SELECT
                        ST_MakeLine(ARRAY_AGG(p.geom ORDER BY sp.rank)) AS geom,
                        MIN(p.ts::DATE) AS day,
                        ARRAY_AGG(DISTINCT TRIM(
                            CONCAT(p.metadata->>'make', ' ', p.metadata->>'model')
                        )) AS models,
                        ARRAY_AGG(DISTINCT p.metadata->>'type') AS types
                    FROM sequences_pictures sp
                    JOIN pictures p ON sp.pic_id = p.id
                    WHERE sp.seq_id = %(seq)s
                )
                UPDATE sequences
                SET
                    status = 'ready',
                    geom = c.geom,
                    computed_type = CASE WHEN array_length(c.types, 1) = 1 THEN c.types[1] ELSE NULL END,
                    computed_model = CASE WHEN array_length(c.models, 1) = 1 THEN c.models[1] ELSE NULL END,
                    computed_capture_date = c.day
                FROM c
                WHERE id = %(seq)s
            """,
                {"seq": seqId},
            )

            log.info(f"Sequence {seqId} is ready")


def _is_sequence_finalized(db, seq_id: str):
    """
    We consider a sequence as ready, if all pictures have been processed and there is at least one correctly processed picture
    Eg. we don't want pictures with preparing_status = 'not-processed' and at least one 'prepared'
    """
    statuses = db.execute(
        """SELECT DISTINCT(preparing_status) FROM pictures p 
        JOIN sequences_pictures sp ON sp.pic_id = p.id
        WHERE
            sp.seq_id = %(id)s
            AND p.preparing_status <> 'broken'
  		;
	""",
        {"id": seq_id},
    ).fetchall()

    return [("prepared",)] == statuses


def _finalize_picture_process(db, job: DbJob):
    job.reporting_conn.execute(
        "UPDATE job_history SET finished_at = CURRENT_TIMESTAMP WHERE id = %(id)s",
        {"id": job.id},
    )
    if job.task == ProcessTask.prepare:
        # Note: the status is slowly been deprecated by replacing it with more precise status, and in the end it will be removed
        job.reporting_conn.execute(
            "UPDATE pictures SET status = 'ready', preparing_status = 'prepared' WHERE id = %(pic_id)s",
            {"pic_id": job.pic.id},
        )

        # Check if we need to finalize the sequence
        _finalize_sequence_if_last_picture(job)
    elif job.task == ProcessTask.delete:
        # TODO set the status to 'deleted' instead of removing it
        db.execute(
            "DELETE FROM pictures WHERE id = %(pic_id)s",
            {"pic_id": job.pic.id},
        )
    db.execute(
        "DELETE FROM pictures_to_process WHERE picture_id = %(pic_id)s",
        {"pic_id": job.pic.id},
    )


def _initialize_picture_process(reporting_conn: psycopg.Connection, pic: DbPicture, task: ProcessTask) -> DbJob:
    r = reporting_conn.execute(
        """INSERT INTO job_history(picture_id, task)
    VALUES (%(id)s, %(task)s)
    RETURNING id
	""",
        {"id": pic.id, "task": task.value},
    ).fetchone()

    if not r:
        raise Exception("impossible to insert task in database")
    return DbJob(reporting_conn=reporting_conn, pic=pic, id=r[0], task=task)


def _mark_process_as_error(db, job: DbJob, e: Exception, config, recoverable: bool = False):
    job.reporting_conn.execute(
        """UPDATE job_history SET
			error = %(err)s, finished_at = CURRENT_TIMESTAMP
		WHERE id = %(id)s""",
        {"err": str(e), "id": job.id},
    )
    if recoverable:
        nb_error = db.execute(
            """
			UPDATE pictures_to_process SET
				nb_errors = nb_errors + 1
			WHERE picture_id = %(id)s
            RETURNING nb_errors""",
            {"err": str(e), "id": job.pic.id},
        ).fetchone()
        if nb_error and nb_error[0] > PICTURE_PROCESS_MAX_RETRY:
            logging.info(f"Job to process picture {job.pic.id} has failed {nb_error} times, we stop trying to process it.")
            recoverable = False

    if not recoverable:
        # Note: the status is slowly been deprecated by replacing it with more precise status, and in the end it will be removed
        job.reporting_conn.execute(
            """UPDATE pictures SET
                preparing_status = 'broken', status = 'broken'
            WHERE id = %(id)s""",
            {"id": job.pic.id},
        )
        # on unrecoverable error, we remove the picture from the queue to process
        db.execute(
            """
			DELETE FROM pictures_to_process
				WHERE picture_id = %(id)s""",
            {"id": job.pic.id},
        )


def _delete_picture(job: DbJob):
    """Delete a picture from the filesystem"""
    log.debug(f"Deleting picture files {job.pic.id}")
    utils.pictures.removeAllFiles(job.pic.id)
