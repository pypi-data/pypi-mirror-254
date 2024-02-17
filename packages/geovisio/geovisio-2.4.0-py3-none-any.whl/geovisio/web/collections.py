import logging
from geovisio import errors, utils
from geovisio.utils import auth
from geovisio.utils.sequences import get_pagination_links
from geovisio.web.params import (
    parse_datetime,
    parse_datetime_interval,
    parse_bbox,
    parse_filter,
    parse_sortby,
    parse_collections_limit,
)
from geovisio.utils.sequences import (
    STAC_FIELD_MAPPINGS,
    STAC_FIELD_TO_SQL_FILTER,
    CollectionsRequest,
    Collections,
    get_collections,
)
from geovisio.utils.fields import SortBy, SortByField, SQLDirection, Bounds, BBox
from geovisio.web.rss import dbSequencesToGeoRSS
import psycopg
from psycopg.rows import dict_row
from psycopg.sql import SQL
from flask import current_app, request, url_for, Blueprint
from geovisio.web.utils import (
    STAC_VERSION,
    accountIdOrDefault,
    cleanNoneInDict,
    cleanNoneInList,
    dbTsToStac,
    get_license_link,
    get_root_link,
    removeNoneInDict,
)
from geovisio.workers import runner_pictures
import geovisio.utils.sequences
from typing import Dict, Any


bp = Blueprint("stac_collections", __name__, url_prefix="/api")


def dbSequenceToStacCollection(dbSeq, description="A sequence of geolocated pictures"):
    """Transforms a sequence extracted from database into a STAC Collection

    Parameters
    ----------
    dbSeq : dict
        A row from sequences table in database (with id, name, minx, miny, maxx, maxy, mints, maxts fields)
    request
    current_app

    Returns
    -------
    object
        The equivalent in STAC Collection format
    """
    mints, maxts = dbSeq.get("mints"), dbSeq.get("maxts")
    return removeNoneInDict(
        {
            "type": "Collection",
            "stac_version": STAC_VERSION,
            "stac_extensions": ["https://stac-extensions.github.io/stats/v0.2.0/schema.json"],  # For stats: fields
            "id": str(dbSeq["id"]),
            "title": str(dbSeq["name"]),
            "description": description,
            "keywords": ["pictures", str(dbSeq["name"])],
            "license": current_app.config["API_PICTURES_LICENSE_SPDX_ID"],
            "created": dbTsToStac(dbSeq["created"]),
            "updated": dbTsToStac(dbSeq.get("updated")),
            "geovisio:status": dbSeq.get("status"),
            "providers": [
                {"name": dbSeq["account_name"], "roles": ["producer"]},
            ],
            "extent": {
                "spatial": {"bbox": [[dbSeq["minx"] or -180.0, dbSeq["miny"] or -90.0, dbSeq["maxx"] or 180.0, dbSeq["maxy"] or 90.0]]},
                "temporal": {
                    "interval": [
                        [
                            dbTsToStac(mints),
                            dbTsToStac(maxts),
                        ]
                    ]
                },
            },
            "summaries": cleanNoneInDict({"pers:interior_orientation": dbSeq.get("metas")}),
            "stats:items": removeNoneInDict({"count": dbSeq.get("nbpic")}),
            "links": cleanNoneInList(
                [
                    (
                        {
                            "rel": "items",
                            "type": "application/geo+json",
                            "title": "Pictures in this sequence",
                            "href": url_for("stac_items.getCollectionItems", _external=True, collectionId=dbSeq["id"]),
                        }
                        if not str(dbSeq["id"]).startswith("user:")
                        else None
                    ),
                    {
                        "rel": "parent",
                        "type": "application/json",
                        "title": "Instance catalog",
                        "href": url_for("stac.getLanding", _external=True),
                    },
                    get_root_link(),
                    {
                        "rel": "self",
                        "type": "application/json",
                        "title": "Metadata of this sequence",
                        "href": url_for("stac_collections.getCollection", _external=True, collectionId=dbSeq["id"]),
                    },
                    get_license_link(),
                ]
            ),
        }
    )


@bp.route("/collections")
def getAllCollections():
    """List available collections
    ---
    tags:
        - Sequences
    parameters:
        - $ref: '#/components/parameters/STAC_collections_limit'
        - name: created_after
          in: query
          description: Deprecated, use "filter" parameter instead (`filter=created > some_date`). Filter for collection uploaded after this date. To filter by capture date, use datetime instead.
          required: false
          deprecated: true
          schema:
            type: string
            format: date-time
        - name: created_before
          in: query
          description: Deprecated, use "filter" parameter instead (`filter=created < some_date`). Filter for collection uploaded before this date. To filter by capture date, use datetime instead.
          required: false
          deprecated: true
          schema:
            type: string
            format: date-time
        - name: format
          in: query
          description: Expected output format (STAC JSON or RSS XML)
          required: false
          schema:
            type: string
            enum: [rss, json]
            default: json
        - $ref: '#/components/parameters/STAC_bbox'
        - $ref: '#/components/parameters/STAC_collections_filter'
        - name: datetime
          in: query
          required: false
          schema:
            type: string
          explode: false
          description: >-
            Filter sequence by capture date. To filter by upload date, use "filter" parameter instead.

            You can filter by a single date or a date interval, open or closed.

            Adhere to RFC 3339. Open intervals are expressed using double-dots.

            This endpoint will only answer based on date (not time) value, even
            if time can be set in query (for STAC compatibility purposes).

            Examples:

            * A date-time: "2018-02-12"

            * A closed interval: "2018-02-12/2018-03-18"

            * Open intervals: "2018-02-12/.." or "../2018-03-18"

    responses:
        200:
            description: the list of available collections
            content:
                application/json:
                    schema:
                        $ref: '#/components/schemas/GeoVisioCollections'
                application/rss+xml:
                    schema:
                        $ref: '#/components/schemas/GeoVisioCollectionsRSS'
    """

    args = request.args

    # Expected output format
    format = args["format"] if args.get("format") in ["rss", "json"] else "json"
    if (
        args.get("format") is None
        and request.accept_mimetypes.best_match(["application/json", "application/rss+xml"], "application/json") == "application/rss+xml"
    ):
        format = "rss"

    # Sort-by parameter
    sortBy = parse_sortby(request.args.get("sortby"))
    if not sortBy:
        direction = SQLDirection.DESC if format == "rss" else SQLDirection.ASC
        sortBy = SortBy(fields=[SortByField(field=STAC_FIELD_MAPPINGS["created"], direction=direction)])

    collection_request = CollectionsRequest(sort_by=sortBy)

    # Filter parameter
    collection_request.user_filter = parse_filter(request.args.get("filter"))
    collection_request.pagination_filter = parse_filter(request.args.get("page"))

    # Limit parameter
    collection_request.limit = parse_collections_limit(request.args.get("limit"))

    # Datetime
    min_dt, max_dt = parse_datetime_interval(args.get("datetime"))
    collection_request.min_dt = min_dt
    collection_request.max_dt = max_dt

    # Bounding box
    bbox = parse_bbox(args.get("bbox"))
    if bbox:
        collection_request.bbox = BBox(
            minx=bbox[0],
            miny=bbox[1],
            maxx=bbox[2],
            maxy=bbox[3],
        )

    # Created after/before
    created_after = args.get("created_after")
    created_before = args.get("created_before")

    if created_after:
        collection_request.created_after = parse_datetime(created_after, error=f"Invalid `created_after` argument", fallback_as_UTC=True)

    if created_before:
        collection_request.created_before = parse_datetime(created_before, error=f"Invalid `created_before` argument", fallback_as_UTC=True)

    links = [
        get_root_link(),
        {"rel": "parent", "type": "application/json", "href": url_for("stac.getLanding", _external=True)},
        {
            "rel": "self",
            "type": "application/json",
            "href": url_for(
                "stac_collections.getAllCollections",
                _external=True,
                limit=args.get("limit"),
                created_after=args.get("created_after"),
            ),
        },
    ]
    with psycopg.connect(current_app.config["DB_URL"], row_factory=dict_row) as conn:
        with conn.cursor() as cursor:
            stats = cursor.execute("SELECT min(inserted_at) as min, max(inserted_at) as max FROM sequences").fetchone()
            if stats is None:
                return ({"collections": [], "links": links}, 200, {"Content-Type": "application/json"})
            datasetBounds = Bounds(min=stats["min"], max=stats["max"])
            if collection_request.created_after and collection_request.created_after > datasetBounds.max:
                raise errors.InvalidAPIUsage(f"There is no collection created after {collection_request.created_after}")
            if collection_request.created_before and collection_request.created_before < datasetBounds.min:
                raise errors.InvalidAPIUsage(f"There is no collection created before {collection_request.created_before}")

    db_collections = get_collections(collection_request)

    # RSS results
    if format == "rss":
        return (dbSequencesToGeoRSS(db_collections.collections).rss(), 200, {"Content-Type": "text/xml"})

    stac_collections = [dbSequenceToStacCollection(c) for c in db_collections.collections]
    pagination_links = []

    additional_filters = request.args.get("filter")

    pagination_links = get_pagination_links(
        route="stac_collections.getAllCollections",
        routeArgs={"limit": collection_request.limit},
        field=sortBy.fields[0].field.stac,
        direction=sortBy.fields[0].direction,
        datasetBounds=datasetBounds,
        dataBounds=db_collections.query_first_order_bounds,
        additional_filters=additional_filters,
    )

    # Compute paginated links
    links.extend(pagination_links)

    return (
        {
            "collections": stac_collections,
            "links": links,
        },
        200,
        {"Content-Type": "application/json"},
    )


@bp.route("/collections/<uuid:collectionId>")
def getCollection(collectionId):
    """Retrieve metadata of a single collection
    ---
    tags:
        - Sequences
    parameters:
        - name: collectionId
          in: path
          description: ID of collection to retrieve
          required: true
          schema:
            type: string
    responses:
        200:
            description: the collection metadata
            content:
                application/json:
                    schema:
                        $ref: '#/components/schemas/GeoVisioCollection'
    """

    account = auth.get_current_account()

    params = {
        "id": collectionId,
        # Only the owner of an account can view sequence not 'ready'
        "account": account.id if account is not None else None,
    }

    with psycopg.connect(current_app.config["DB_URL"], row_factory=dict_row) as conn:
        with conn.cursor() as cursor:
            record = cursor.execute(
                """
				SELECT
					s.id,
					s.metadata->>'title' AS name,
					ST_XMin(s.geom) AS minx,
					ST_YMin(s.geom) AS miny,
					ST_XMax(s.geom) AS maxx,
					ST_YMax(s.geom) AS maxy,
					s.status AS status,
					accounts.name AS account_name,
					s.inserted_at AS created,
	 				s.updated_at AS updated,
					a.*
				FROM sequences s
				JOIN accounts ON s.account_id = accounts.id, (
					SELECT
						MIN(ts) as mints,
						MAX(ts) as maxts,
						array_agg(DISTINCT jsonb_build_object(
							'make', metadata->>'make',
							'model', metadata->>'model',
							'focal_length', metadata->>'focal_length',
							'field_of_view', metadata->>'field_of_view'
						)) AS metas,
						COUNT(*) AS nbpic
					FROM pictures p
					JOIN sequences_pictures sp ON sp.seq_id = %(id)s AND sp.pic_id = p.id
				) a
				WHERE s.id = %(id)s
					AND (s.status != 'hidden' OR s.account_id = %(account)s)
					AND s.status != 'deleted'
			""",
                params,
            ).fetchone()

            if record is None:
                raise errors.InvalidAPIUsage("Collection doesn't exist", status_code=404)

            return (
                dbSequenceToStacCollection(record),
                200,
                {
                    "Content-Type": "application/json",
                },
            )


@bp.route("/collections/<uuid:collectionId>/thumb.jpg", methods=["GET"])
def getCollectionThumbnail(collectionId):
    """Get the thumbnail representing a single collection
    ---
    tags:
        - Sequences
    parameters:
        - name: collectionId
          in: path
          description: ID of collection to retrieve
          required: true
          schema:
            type: string
    responses:
        200:
            description: 500px wide ready-for-display image
            content:
                image/jpeg:
                    schema:
                        type: string
                        format: binary
    """
    account = auth.get_current_account()

    params = {
        "seq": collectionId,
        # Only the owner of an account can view pictures not 'ready'
        "account": account.id if account is not None else None,
    }

    with psycopg.connect(current_app.config["DB_URL"], row_factory=dict_row) as conn:
        with conn.cursor() as cursor:
            records = cursor.execute(
                """
				SELECT
					sp.pic_id
				FROM sequences_pictures sp
				JOIN pictures p ON sp.pic_id = p.id
				JOIN sequences s ON sp.seq_id = s.id
				WHERE
					sp.seq_id = %(seq)s
					AND (p.status = 'ready' OR p.account_id = %(account)s)
					AND is_sequence_visible_by_user(s, %(account)s)
				LIMIT 1
			""",
                params,
            ).fetchone()

            if records is None:
                raise errors.InvalidAPIUsage("Impossible to find a thumbnail for the collection", status_code=404)

            return utils.pictures.sendThumbnail(records["pic_id"], "jpg")


@bp.route("/collections", methods=["POST"])
@auth.login_required_by_setting("API_FORCE_AUTH_ON_UPLOAD")
def postCollection(account=None):
    """Create a new sequence
    ---
    tags:
        - Upload
    requestBody:
        content:
            application/json:
                schema:
                    $ref: '#/components/schemas/GeoVisioPostCollection'
            application/x-www-form-urlencoded:
                schema:
                    $ref: '#/components/schemas/GeoVisioPostCollection'
            multipart/form-data:
                schema:
                    $ref: '#/components/schemas/GeoVisioPostCollection'
    security:
        - bearerToken: []
        - cookieAuth: []
    responses:
        200:
            description: the collection metadata
            content:
                application/json:
                    schema:
                        $ref: '#/components/schemas/GeoVisioCollection'
    """

    # Parse received parameters
    metadata = {}
    content_type = request.headers.get("Content-Type")
    if request.is_json:
        metadata["title"] = request.json.get("title")
    elif content_type in ["multipart/form-data", "application/x-www-form-urlencoded"]:
        metadata["title"] = request.form.get("title")

    metadata = removeNoneInDict(metadata)

    # Create sequence folder
    accountId = accountIdOrDefault(account)
    seqId = geovisio.utils.sequences.createSequence(metadata, accountId)

    # Return created sequence
    return (
        getCollection(seqId)[0],
        200,
        {
            "Content-Type": "application/json",
            "Access-Control-Expose-Headers": "Location",  # Needed for allowing web browsers access Location header
            "Location": url_for("stac_collections.getCollection", _external=True, collectionId=seqId),
        },
    )


@bp.route("/collections/<uuid:collectionId>", methods=["PATCH"])
@auth.login_required()
def patchCollection(collectionId, account):
    """Edits properties of an existing collection
    ---
    tags:
        - Editing
    parameters:
        - name: collectionId
          in: path
          description: The sequence ID
          required: true
          schema:
            type: string
    requestBody:
        content:
            application/json:
                schema:
                    $ref: '#/components/schemas/GeoVisioPatchCollection'
            application/x-www-form-urlencoded:
                schema:
                    $ref: '#/components/schemas/GeoVisioPatchCollection'
            multipart/form-data:
                schema:
                    $ref: '#/components/schemas/GeoVisioPatchCollection'
    security:
        - bearerToken: []
        - cookieAuth: []
    responses:
        200:
            description: the wanted collection
            content:
                application/json:
                    schema:
                        $ref: '#/components/schemas/GeoVisioCollection'
    """

    # Parse received parameters
    metadata = {}
    content_type = (request.headers.get("Content-Type") or "").split(";")[0]
    for param in ["visible", "title"]:
        if request.is_json:
            metadata[param] = request.json.get(param)
        elif content_type in ["multipart/form-data", "application/x-www-form-urlencoded"]:
            metadata[param] = request.form.get(param)

    # Check if visibility param is valid
    visible = metadata.get("visible")
    if visible is not None:
        if visible in ["true", "false"]:
            visible = visible == "true"
        else:
            raise errors.InvalidAPIUsage("Picture visibility parameter (visible) should be either unset, true or false", status_code=400)

    # Check if title is valid
    newTitle = metadata.get("title")
    if newTitle is not None:
        if not (isinstance(newTitle, str) and len(newTitle) <= 250):
            raise errors.InvalidAPIUsage("Sequence title is not valid, should be a string with a max of 250 characters", status_code=400)

    # If no parameter is changed, no need to contact DB, just return sequence as is
    if {visible, newTitle} == {None}:
        return getCollection(collectionId)

    # Check if sequence exists and if given account is authorized to edit
    with psycopg.connect(current_app.config["DB_URL"], row_factory=dict_row) as conn, conn.cursor() as cursor:
        seq = cursor.execute("SELECT status, metadata, account_id FROM sequences WHERE id = %s", [collectionId]).fetchone()

        # Sequence not found
        if not seq:
            raise errors.InvalidAPIUsage(f"Sequence {collectionId} wasn't found in database", status_code=404)

        # Account associated to sequence doesn't match current user
        if account is not None and account.id != str(seq["account_id"]):
            raise errors.InvalidAPIUsage("You're not authorized to edit this sequence", status_code=403)

        oldStatus = seq["status"]
        oldMetadata = seq["metadata"]
        oldTitle = oldMetadata.get("title")

        # Check if sequence is in a preparing/broken/... state so no edit possible
        if oldStatus not in ["ready", "hidden"]:
            raise errors.InvalidAPIUsage(
                f"Sequence {collectionId} is in {oldStatus} state, its visibility can't be changed for now", status_code=400
            )

        # Let's edit this picture
        sqlUpdates = []
        sqlParams = {"id": collectionId}

        if visible is not None:
            newStatus = "ready" if visible is True else "hidden"
            if newStatus != oldStatus:
                sqlUpdates.append(SQL("status = %(status)s"))
                sqlParams["status"] = newStatus

        if newTitle is not None and oldTitle != newTitle:
            sqlUpdates.append(SQL("metadata = jsonb_set(metadata, '{title}', %(title)s)"))
            sqlParams["title"] = f'"{newTitle}"'

        if len(sqlUpdates) > 0:
            cursor.execute(
                SQL(
                    """
                UPDATE sequences
                SET {updates}
                WHERE id = %(id)s
            """
                ).format(updates=SQL(", ").join(sqlUpdates)),
                sqlParams,
            )
            conn.commit()

        # Redirect response to a classic GET
        return getCollection(collectionId)


@bp.route("/collections/<uuid:collectionId>", methods=["DELETE"])
@auth.login_required()
def deleteCollection(collectionId, account):
    """Delete a collection and all the associated pictures
    The associated images will be hidden right away and deleted asynchronously
    ---
    tags:
        - Editing
    parameters:
        - name: collectionId
          in: path
          description: ID of the collection
          required: true
          schema:
            type: string
    security:
        - bearerToken: []
        - cookieAuth: []
    responses:
        204:
            description: The collection has been correctly deleted
    """

    # Check if collection exists and if given account is authorized to edit
    with psycopg.connect(current_app.config["DB_URL"]) as conn:
        with conn.cursor() as cursor:
            sequence = cursor.execute("SELECT status, account_id FROM sequences WHERE id = %s", [collectionId]).fetchone()

            # sequence not found
            if not sequence:
                raise errors.InvalidAPIUsage(f"Collection {collectionId} wasn't found in database", status_code=404)

            # Account associated to sequence doesn't match current user
            if account is not None and account.id != str(sequence[1]):
                raise errors.InvalidAPIUsage("You're not authorized to edit this sequence", status_code=403)

            logging.info(f"Asking for deletion of sequence {collectionId} and all its pictures")

            # mark all the pictures as waiting for deletion for async removal as this can be quite long if the storage is slow if there are lots of pictures
            # Note: To avoid a deadlock if some workers are currently also working on those picture to prepare them,
            # the SQL queries are split in 2:
            # - First a query to add the async deletion task to the queue.
            # - Then a query changing the status of the picture to `waiting-for-delete`
            #
            # The trick there is that there can only be one task for a given picture (either preparing or deleting it)
            # And the first query do a `ON CONFLICT DO UPDATE` to change the remaining `prepare` task to `delete`.
            # So at the end of this query, we know that there are no more workers working on those pictures, so we can change their status
            # without fearing a deadlock.
            nb_updated = cursor.execute(
                """
                WITH pic2rm AS (
                    SELECT pic_id FROM sequences_pictures WHERE seq_id = %(seq)s
                ),
                picWithoutOtherSeq AS (
                    SELECT pic_id FROM pic2rm
                    EXCEPT
                    SELECT pic_id FROM sequences_pictures WHERE pic_id IN (SELECT pic_id FROM pic2rm) AND seq_id != %(seq)s
                )
                INSERT INTO pictures_to_process(picture_id, task)
                    SELECT pic_id, 'delete' FROM picWithoutOtherSeq
                    ON CONFLICT (picture_id) DO UPDATE SET task = 'delete'
			""",
                {"seq": collectionId},
            ).rowcount

            # after the task have been added to the queue, we mark all picture for deletion
            cursor.execute(
                """
                WITH pic2rm AS (
                    SELECT pic_id FROM sequences_pictures WHERE seq_id = %(seq)s
                ),
                picWithoutOtherSeq AS (
                    SELECT pic_id FROM pic2rm
                    EXCEPT
                    SELECT pic_id FROM sequences_pictures WHERE pic_id IN (SELECT pic_id FROM pic2rm) AND seq_id != %(seq)s
                )
                UPDATE pictures SET status = 'waiting-for-delete' WHERE id IN (SELECT pic_id FROM picWithoutOtherSeq)
			""",
                {"seq": collectionId},
            ).rowcount

            cursor.execute("UPDATE sequences SET status = 'deleted' WHERE id = %s", [collectionId])
            conn.commit()

            # add background task if needed, to really delete pictures
            for _ in range(nb_updated):
                runner_pictures.background_processor.process_pictures()

            return "", 204


@bp.route("/collections/<uuid:collectionId>/geovisio_status")
def getCollectionImportStatus(collectionId):
    """Retrieve import status of all pictures in sequence
    ---
    tags:
        - Upload
    parameters:
        - name: collectionId
          in: path
          description: ID of collection to retrieve
          required: true
          schema:
            type: string
    responses:
        200:
            description: the pictures statuses
            content:
                application/json:
                    schema:
                        $ref: '#/components/schemas/GeoVisioCollectionImportStatus'
    """

    account = auth.get_current_account()
    params = {"seq_id": collectionId, "account": account.id if account is not None else None}
    with psycopg.connect(current_app.config["DB_URL"], row_factory=dict_row) as conn:
        with conn.cursor() as cursor:
            sequence_status = cursor.execute(
                """WITH
pic_jobs_stats AS (
    SELECT
    picture_id,
    (MAX(ARRAY[finished_at::varchar, error]))[2] last_job_error,
    MAX(finished_at) last_job_finished_at,
    (MAX(ARRAY[started_at, finished_at]))[2] IS NULL is_job_running,
    COUNT(job_history.*) as nb_jobs,
    COUNT(job_history.*) FILTER (WHERE job_history.error IS NOT NULL) as nb_errors
    FROM job_history
    WHERE picture_id IN (
        SELECT pic_id from sequences_pictures WHERE seq_id = %(seq_id)s
    )
    GROUP BY picture_id
)
, items AS (
    SELECT
    p.id,
    p.status,
    sp.rank,
    s.id as seq_id,
    pic_jobs_stats.is_job_running,
    pic_jobs_stats.last_job_error,
    pic_jobs_stats.nb_errors,
    pic_jobs_stats.last_job_finished_at
    FROM sequences s
    LEFT JOIN sequences_pictures sp ON sp.seq_id = s.id
    LEFT JOIN pictures p ON sp.pic_id = p.id
    LEFT JOIN pic_jobs_stats ON pic_jobs_stats.picture_id = p.id
    WHERE
                s.id = %(seq_id)s
                AND (p IS NULL OR p.status != 'hidden' OR p.account_id = %(account)s)
                AND (s.status != 'hidden' OR s.account_id = %(account)s) -- show deleted sequence here
    ORDER BY s.id, sp.rank
)
SELECT json_build_object(
        'status', s.status,
        'items', json_agg(
                    json_strip_nulls(
                        json_build_object(
                            'id', i.id,
                            -- status is a bit deprecated, we'll split this field in more fields (like `processing_in_progress`, `hidden`, ...)
                            -- but we maintain it for retrocompatibility
                            'status', CASE 
                                    WHEN i.is_job_running IS TRUE THEN 'preparing' 
                                    WHEN i.last_job_error IS NOT NULL THEN 'broken' 
                                    ELSE i.status
                                END, 
                            'processing_in_progress', i.is_job_running,
                            'process_error', i.last_job_error,
                            'nb_errors', i.nb_errors,
                            'processed_at', i.last_job_finished_at,
                            'rank', i.rank
                        )
                )
        )
) AS sequence
FROM items i
JOIN sequences s on i.seq_id = s.id
GROUP by s.id;""",
                params,
            ).fetchall()

            if len(sequence_status) == 0:
                raise errors.InvalidAPIUsage("Sequence doesn't exists", status_code=404)

            return sequence_status[0]["sequence"]


@bp.route("/users/<uuid:userId>/collection")
@auth.isUserIdMatchingCurrentAccount()
def getUserCollection(userId, userIdMatchesAccount=False):
    """Retrieves an collection of the user list collections

    It's quite the same as "/users/<uuid:userId>/catalog/" but with additional information, as a STAC collection have more metadatas than STAC catalogs.

    Links contain information of user sequences (child), as well as pagination links (next/prev).

    Also, links are filtered to match passed conditions, so you can have pagination and filters on client-side.

    Note that on paginated results, filter can only be used with column used in sortby parameter.

    ---
    tags:
        - Sequences
        - Users
    parameters:
        - name: userId
          in: path
          description: User ID
          required: true
          schema:
            type: string
        - $ref: '#/components/parameters/STAC_collections_limit'
        - $ref: '#/components/parameters/STAC_collections_filter'
        - $ref: '#/components/parameters/STAC_bbox'
        - $ref: '#/components/parameters/OGC_sortby'
    responses:
        200:
            description: the Collection listing all sequences associated to given user
            content:
                application/json:
                    schema:
                        $ref: '#/components/schemas/GeoVisioCollectionOfCollection'
    """

    # Sort-by parameter
    sortBy = parse_sortby(request.args.get("sortby"))
    if not sortBy:
        sortBy = SortBy(fields=[SortByField(field=STAC_FIELD_MAPPINGS["created"], direction=SQLDirection.DESC)])

    collection_request = CollectionsRequest(sort_by=sortBy, userOwnsAllCollections=userIdMatchesAccount)

    # Filter parameter
    collection_request.user_filter = parse_filter(request.args.get("filter"))

    # Filters added by the pagination
    collection_request.pagination_filter = parse_filter(request.args.get("page"))

    # Limit parameter
    collection_request.limit = parse_collections_limit(request.args.get("limit"))
    collection_request.user_id = userId

    # Bounding box
    bbox = parse_bbox(request.args.get("bbox"))
    if bbox:
        collection_request.bbox = BBox(
            minx=bbox[0],
            miny=bbox[1],
            maxx=bbox[2],
            maxy=bbox[3],
        )

    meta_filter = [
        SQL("{field} IS NOT NULL").format(field=collection_request.sort_by.fields[0].field.sql_filter),
        SQL("s.account_id = %(account)s"),
    ]
    if collection_request.user_filter is not None:
        meta_filter.append(collection_request.user_filter)

    if collection_request.user_filter is None or "status" not in collection_request.user_filter.as_string(None):
        # if the filter does not contains any `status` condition, we want to show only 'ready' collection to the general users, and non deleted one for the owner
        if not userIdMatchesAccount:
            meta_filter.extend([SQL("s.status = 'ready'"), SQL("p.status = 'ready'")])
        else:
            meta_filter.append(SQL("s.status != 'deleted'"))

    # Check user account parameter
    with psycopg.connect(current_app.config["DB_URL"], row_factory=dict_row) as conn:
        with conn.cursor() as cursor:
            userName = cursor.execute("SELECT name FROM accounts WHERE id = %s", [userId]).fetchone()

            if not userName:
                raise errors.InvalidAPIUsage(f"Impossible to find user {userId}")
            userName = userName["name"]

            meta_collection = cursor.execute(
                SQL(
                    """SELECT
					COUNT(sp.pic_id) AS nbpic,
					COUNT(s.id) AS nbseq,
					MIN(p.ts) AS mints,
					MAX(p.ts) AS maxts,
					MIN(GREATEST(-180, ST_X(p.geom))) AS minx,
					MIN(GREATEST(-90, ST_Y(p.geom))) AS miny,
					MAX(LEAST(180, ST_X(p.geom))) AS maxx,
					MAX(LEAST(90, ST_Y(p.geom))) AS maxy,
                    MIN(s.inserted_at) AS created,
                    MAX(s.updated_at) AS updated,
                    MIN({order_column}) AS min_order,
                    MAX({order_column}) AS max_order
				FROM sequences s
				LEFT JOIN sequences_pictures sp ON s.id = sp.seq_id
				LEFT JOIN pictures p on sp.pic_id = p.id
				WHERE {filter}
			    """
                ).format(
                    filter=SQL(" AND ").join(meta_filter),
                    order_column=collection_request.sort_by.fields[0].field.sql_filter,
                ),
                params={"account": userId},
            ).fetchone()

            if not meta_collection or meta_collection["created"] is None:
                # No data found, trying to give the most meaningfull error message
                if collection_request.user_filter is None:
                    raise errors.InvalidAPIUsage(f"No data loaded for user {userId}", 404)
                else:
                    raise errors.InvalidAPIUsage(f"No matching sequences found", 404)

    collections = get_collections(collection_request)

    sequences_links = [
        removeNoneInDict(
            {
                "id": s["id"],
                "title": s["name"],
                "rel": "child",
                "href": url_for("stac_collections.getCollection", _external=True, collectionId=s["id"]),
                "stats:items": {"count": s["nbpic"]},
                "created": dbTsToStac(s["created"]),
                "updated": dbTsToStac(s["updated"]),
                "extent": {
                    "temporal": {
                        "interval": [
                            [
                                dbTsToStac(s["mints"]),
                                dbTsToStac(s["maxts"]),
                            ]
                        ]
                    },
                    "spatial": {"bbox": [[s["minx"] or -180.0, s["miny"] or -90.0, s["maxx"] or 180.0, s["maxy"] or 90.0]]},
                },
                "geovisio:status": s["status"] if userIdMatchesAccount else None,
            }
        )
        for s in collections.collections
    ]

    meta_collection.update(
        {
            "id": f"user:{userId}",
            "name": f"{userName}'s sequences",
            "account_name": userName,
        }
    )
    collection = dbSequenceToStacCollection(meta_collection, description=f"List of all sequences of user {userName}")

    additional_filters = None
    if collection_request.user_filter is not None:
        # if some filters were given, we continue to pass them to the pagination
        additional_filters = request.args.get("filter")

    pagination_links = get_pagination_links(
        route="stac_collections.getUserCollection",
        routeArgs={"userId": str(userId), "limit": collection_request.limit},
        field=sortBy.fields[0].field.stac,
        direction=sortBy.fields[0].direction,
        datasetBounds=Bounds(min=meta_collection["min_order"], max=meta_collection["max_order"]),
        dataBounds=collections.query_first_order_bounds,
        additional_filters=additional_filters,
    )

    # add all sub collections as links
    collection["links"].extend(pagination_links + sequences_links)

    # and we update the self link since it's not a collection mapped directly to a sequence
    self = next(l for l in collection["links"] if l["rel"] == "self")
    self["href"] = url_for("stac_collections.getUserCollection", _external=True, userId=str(userId))

    collection["stac_extensions"].append(
        "https://stac-extensions.github.io/timestamps/v1.1.0/schema.json"
    )  # for `updated`/`created` fields in links

    return (collection, 200, {"Content-Type": "application/json"})
