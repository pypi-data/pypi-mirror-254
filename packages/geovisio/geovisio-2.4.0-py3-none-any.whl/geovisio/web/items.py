import io
import json
import logging
import os
import re
from typing import Dict, Optional, Any
from urllib.parse import unquote
from psycopg.types.json import Jsonb
from werkzeug.datastructures import MultiDict
from uuid import UUID
from geovisio import errors, utils
from geovisio.utils import auth
from geovisio.web.params import (
    as_latitude,
    as_longitude,
    as_uuid,
    parse_datetime,
    parse_datetime_interval,
    parse_bbox,
    parse_list,
)
from geovisio.utils.fields import Bounds

import psycopg
from datetime import datetime
from psycopg.rows import dict_row
from psycopg.sql import SQL
from geovisio.web.utils import (
    accountIdOrDefault,
    cleanNoneInList,
    dbTsToStac,
    get_license_link,
    get_root_link,
    removeNoneInDict,
    STAC_VERSION,
)
from flask import current_app, request, url_for, Blueprint
from geopic_tag_reader.writer import writePictureMetadata, PictureMetadata

from geovisio.workers import runner_pictures

bp = Blueprint("stac_items", __name__, url_prefix="/api")

RGX_BINARY_KEY = re.compile(".+\..+\.0x[0-f]+")
RGX_BINARY_VAL = re.compile("(\d{1,3} ){20,}\d{1,3}")  # At least 21 blocks of 1-3 digits values


def dbPictureToStacItem(seqId, dbPic):
    """Transforms a picture extracted from database into a STAC Item

    Parameters
    ----------
    seqId : uuid
        Associated sequence ID
    dbSeq : dict
        A row from pictures table in database (with id, geojson, ts, heading, cols, rows, width, height, prevpic, nextpic, prevpicgeojson, nextpicgeojson, exif fields)

    Returns
    -------
    object
        The equivalent in STAC Item format
    """

    item = removeNoneInDict(
        {
            "type": "Feature",
            "stac_version": STAC_VERSION,
            "stac_extensions": [
                "https://stac-extensions.github.io/view/v1.0.0/schema.json",  # "view:" fields
                "https://stac-extensions.github.io/perspective-imagery/v1.0.0/schema.json",  # "pers:" fields
            ],
            "id": str(dbPic["id"]),
            "geometry": dbPic["geojson"],
            "bbox": dbPic["geojson"]["coordinates"] + dbPic["geojson"]["coordinates"],
            "providers": cleanNoneInList(
                [
                    {"name": dbPic["account_name"], "roles": ["producer"]},
                    (
                        {"name": dbPic["exif"]["Exif.Image.Artist"], "roles": ["producer"]}
                        if dbPic["exif"].get("Exif.Image.Artist") is not None
                        else None
                    ),
                ]
            ),
            "properties": {
                "datetime": dbTsToStac(dbPic["ts"]),
                "created": dbTsToStac(dbPic["inserted_at"]),
                # TODO : add "updated" TS for last edit time of metadata
                "license": current_app.config["API_PICTURES_LICENSE_SPDX_ID"],
                "view:azimuth": dbPic["heading"],
                "pers:interior_orientation": (
                    removeNoneInDict(
                        {
                            "camera_manufacturer": dbPic["metadata"].get("make"),
                            "camera_model": dbPic["metadata"].get("model"),
                            "focal_length": dbPic["metadata"].get("focal_length"),
                            "field_of_view": dbPic["metadata"].get("field_of_view"),
                        }
                    )
                    if "metadata" in dbPic
                    and any(True for f in dbPic["metadata"] if f in ["make", "model", "focal_length", "field_of_view"])
                    else {}
                ),
                "geovisio:status": dbPic.get("status"),
                "geovisio:producer": dbPic["account_name"],
                "original_file:size": dbPic["metadata"].get("originalFileSize"),
                "original_file:name": dbPic["metadata"].get("originalFileName"),
                "geovisio:image": _getHDJpgPictureURL(dbPic["id"], dbPic.get("status")),
                "geovisio:thumbnail": _getThumbJpgPictureURL(dbPic["id"], dbPic.get("status")),
                "exif": removeNoneInDict(cleanupExif(dbPic["exif"])),
            },
            "links": cleanNoneInList(
                [
                    get_root_link(),
                    {
                        "rel": "parent",
                        "type": "application/json",
                        "href": url_for("stac_collections.getCollection", _external=True, collectionId=seqId),
                    },
                    {
                        "rel": "self",
                        "type": "application/geo+json",
                        "href": url_for("stac_items.getCollectionItem", _external=True, collectionId=seqId, itemId=dbPic["id"]),
                    },
                    {
                        "rel": "collection",
                        "type": "application/json",
                        "href": url_for("stac_collections.getCollection", _external=True, collectionId=seqId),
                    },
                    get_license_link(),
                ]
            ),
            "assets": {
                "hd": {
                    "title": "HD picture",
                    "description": "Highest resolution available of this picture",
                    "roles": ["data"],
                    "type": "image/jpeg",
                    "href": _getHDJpgPictureURL(dbPic["id"], status=dbPic.get("status")),
                },
                "sd": {
                    "title": "SD picture",
                    "description": "Picture in standard definition (fixed width of 2048px)",
                    "roles": ["visual"],
                    "type": "image/jpeg",
                    "href": _getSDJpgPictureURL(dbPic["id"], status=dbPic.get("status")),
                },
                "thumb": {
                    "title": "Thumbnail",
                    "description": "Picture in low definition (fixed width of 500px)",
                    "roles": ["thumbnail"],
                    "type": "image/jpeg",
                    "href": _getThumbJpgPictureURL(dbPic["id"], status=dbPic.get("status")),
                },
            },
            "collection": str(seqId),
        }
    )

    # Next / previous links if any
    if "nextpic" in dbPic and dbPic["nextpic"] is not None:
        item["links"].append(
            {
                "rel": "next",
                "type": "application/geo+json",
                "geometry": dbPic["nextpicgeojson"],
                "id": dbPic["nextpic"],
                "href": url_for("stac_items.getCollectionItem", _external=True, collectionId=seqId, itemId=dbPic["nextpic"]),
            }
        )

    if "prevpic" in dbPic and dbPic["prevpic"] is not None:
        item["links"].append(
            {
                "rel": "prev",
                "type": "application/geo+json",
                "geometry": dbPic["prevpicgeojson"],
                "id": dbPic["prevpic"],
                "href": url_for("stac_items.getCollectionItem", _external=True, collectionId=seqId, itemId=dbPic["prevpic"]),
            }
        )

    if dbPic.get("related_pics") is not None:
        for rp in dbPic["related_pics"]:
            repSeq, rpId, rpGeom, rpTs = rp
            item["links"].append(
                {
                    "rel": "related",
                    "type": "application/geo+json",
                    "geometry": json.loads(rpGeom),
                    "datetime": rpTs,
                    "id": rpId,
                    "href": url_for("stac_items.getCollectionItem", _external=True, collectionId=repSeq, itemId=rpId),
                }
            )

    #
    # Picture type-specific properties
    #

    # Equirectangular
    if dbPic["metadata"]["type"] == "equirectangular":
        item["stac_extensions"].append("https://stac-extensions.github.io/tiled-assets/v1.0.0/schema.json")  # "tiles:" fields

        item["properties"]["tiles:tile_matrix_sets"] = {
            "geovisio": {
                "type": "TileMatrixSetType",
                "title": "GeoVisio tile matrix for picture " + str(dbPic["id"]),
                "identifier": "geovisio-" + str(dbPic["id"]),
                "tileMatrix": [
                    {
                        "type": "TileMatrixType",
                        "identifier": "0",
                        "scaleDenominator": 1,
                        "topLeftCorner": [0, 0],
                        "tileWidth": dbPic["metadata"]["width"] / dbPic["metadata"]["cols"],
                        "tileHeight": dbPic["metadata"]["height"] / dbPic["metadata"]["rows"],
                        "matrixWidth": dbPic["metadata"]["cols"],
                        "matrixHeight": dbPic["metadata"]["rows"],
                    }
                ],
            }
        }

        item["asset_templates"] = {
            "tiles": {
                "title": "HD tiled picture",
                "description": "Highest resolution available of this picture, as tiles",
                "roles": ["data"],
                "type": "image/jpeg",
                "href": _getTilesJpgPictureURL(dbPic["id"], status=dbPic.get("status")),
            }
        }

    return item


def cleanupExif(exif: Optional[Dict[str, str]]) -> Optional[Dict[str, str]]:
    """Removes things from EXIF dictionnary that should not land in STAC responses
    >>> cleanupExif({'A': 'B', 'Exif.Sony.0x0102': 'Blablabla'})
    {'A': 'B'}
    >>> cleanupExif({'A': 'B', 'Exif.Photo.MakerNote': 'Blablabla'})
    {'A': 'B'}
    >>> cleanupExif({'A': 'B', 'Exif.Sony.Whatever': '1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21'})
    {'A': 'B'}
    >>> cleanupExif({'A': 'B', 'Exif.Sony.Whatever': '1 2 3 4 5'})
    {'A': 'B', 'Exif.Sony.Whatever': '1 2 3 4 5'}
    """

    if exif is None:
        return None

    cleanExif = {}

    for k, v in exif.items():
        if not (k in ["Exif.Photo.MakerNote"] or RGX_BINARY_KEY.match(k) or RGX_BINARY_VAL.match(v)):
            cleanExif[k] = v

    return cleanExif


def get_first_rank_of_page(rankToHave: int, limit: Optional[int]) -> int:
    """if there is a limit, we try to emulate a page, so we'll return the nth page that should contain this picture
    Note: the ranks starts from 1
    >>> get_first_rank_of_page(3, 2)
    3
    >>> get_first_rank_of_page(4, 2)
    3
    >>> get_first_rank_of_page(3, None)
    3
    >>> get_first_rank_of_page(123, 10)
    121
    >>> get_first_rank_of_page(10, 10)
    1
    >>> get_first_rank_of_page(10, 100)
    1
    """
    if not limit:
        return rankToHave

    return int((rankToHave - 1) / limit) * limit + 1


@bp.route("/collections/<uuid:collectionId>/items", methods=["GET"])
def getCollectionItems(collectionId):
    """List items of a single collection
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
        - name: limit
          in: query
          description: Number of items that should be present in response. Unlimited by default.
          required: false
          schema:
            type: integer
            minimum: 1
            maximum: 10000
        - name: startAfterRank
          in: query
          description: Position of last received picture in sequence. Response will start with the following picture.
          required: false
          schema:
            type: integer
            minimum: 1
        - name: withPicture
          in: query
          description: Used in the pagination context, if present, the api will return the given picture in the results.
            Can be used in the same time as the `limit` parameter, but not with the `startAfterRank` parameter.
          required: false
          schema:
            type: string
            format: uuid
    responses:
        200:
            description: the items list
            content:
                application/geo+json:
                    schema:
                        $ref: '#/components/schemas/GeoVisioCollectionItems'
    """

    account = auth.get_current_account()

    params = {
        "seq": collectionId,
        # Only the owner of an account can view pictures not 'ready'
        "account": account.id if account is not None else None,
    }

    args = request.args
    limit = args.get("limit")
    startAfterRank = args.get("startAfterRank")
    withPicture = args.get("withPicture")

    filters = [
        SQL("sp.seq_id = %(seq)s"),
        SQL("(p.status = 'ready' OR p.account_id = %(account)s)"),
        SQL("(is_sequence_visible_by_user(s, %(account)s))"),
    ]

    # Check if limit is valid
    sql_limit = SQL("")
    if limit is not None:
        try:
            limit = int(limit)
            if limit < 1 or limit > 10000:
                raise errors.InvalidAPIUsage("limit parameter should be an integer between 1 and 10000", status_code=400)
        except ValueError:
            raise errors.InvalidAPIUsage("limit parameter should be a valid, positive integer (between 1 and 10000)", status_code=400)
        sql_limit = SQL("LIMIT %(limit)s")
        params["limit"] = limit

    if withPicture and startAfterRank:
        raise errors.InvalidAPIUsage(f"`startAfterRank` and `withPicture` are mutually exclusive parameters")

    # Check if rank is valid
    if startAfterRank is not None:
        try:
            startAfterRank = int(startAfterRank)
            if startAfterRank < 1:
                raise errors.InvalidAPIUsage("startAfterRank parameter should be a positive integer (starting from 1)", status_code=400)
        except ValueError:
            raise errors.InvalidAPIUsage("startAfterRank parameter should be a valid, positive integer", status_code=400)

        filters.append(SQL("rank > %(start_after_rank)s"))
        params["start_after_rank"] = startAfterRank

    paginated = startAfterRank is not None or limit is not None or withPicture is not None

    with psycopg.connect(current_app.config["DB_URL"], row_factory=dict_row) as conn:
        with conn.cursor() as cursor:
            # check on sequence
            seqMeta = cursor.execute(
                "SELECT s.id "
                + (", MAX(sp.rank) AS max_rank, MIN(sp.rank) AS min_rank " if paginated else "")
                + "FROM sequences s "
                + ("LEFT JOIN sequences_pictures sp ON sp.seq_id = s.id " if paginated else "")
                + "WHERE s.id = %(seq)s AND (is_sequence_visible_by_user(s, %(account)s)) "
                + ("GROUP BY s.id" if paginated else ""),
                params,
            ).fetchone()

            if seqMeta is None:
                raise errors.InvalidAPIUsage("Collection doesn't exist", status_code=404)

            maxRank = seqMeta.get("max_rank")

            if startAfterRank is not None and startAfterRank >= maxRank:
                raise errors.InvalidAPIUsage(f"No more items in this collection (last available rank is {maxRank})", status_code=404)

            if withPicture is not None:
                withPicture = as_uuid(withPicture, "withPicture should be a valid UUID")
                pic = cursor.execute(
                    "SELECT rank FROM pictures p JOIN sequences_pictures sp ON sp.pic_id = p.id WHERE p.id = %(id)s AND sp.seq_id = %(seq)s",
                    params={"id": withPicture, "seq": collectionId},
                ).fetchone()
                if not pic:
                    raise errors.InvalidAPIUsage(f"Picture with id {withPicture} does not exists")
                rank = get_first_rank_of_page(pic["rank"], limit)

                filters.append(SQL("rank >= %(start_after_rank)s"))
                params["start_after_rank"] = rank

            query = SQL(
                """
				SELECT
					p.id, p.ts, p.heading, p.metadata, p.inserted_at, p.status,
					ST_AsGeoJSON(p.geom)::json AS geojson,
					a.name AS account_name,
                    sp.rank, p.exif,
					CASE WHEN LAG(p.status) OVER othpics = 'ready' THEN LAG(p.id) OVER othpics END AS prevpic,
					CASE WHEN LAG(p.status) OVER othpics = 'ready' THEN ST_AsGeoJSON(LAG(p.geom) OVER othpics)::json END AS prevpicgeojson,
					CASE WHEN LEAD(p.status) OVER othpics = 'ready' THEN LEAD(p.id) OVER othpics END AS nextpic,
					CASE WHEN LEAD(p.status) OVER othpics = 'ready' THEN ST_AsGeoJSON(LEAD(p.geom) OVER othpics)::json END AS nextpicgeojson
				FROM sequences_pictures sp
				JOIN pictures p ON sp.pic_id = p.id
				JOIN accounts a ON a.id = p.account_id
				JOIN sequences s ON s.id = sp.seq_id
				WHERE
    				{filter}
				WINDOW othpics AS (PARTITION BY sp.seq_id ORDER BY sp.rank)
				ORDER BY rank
                {limit}
                """
            ).format(filter=SQL(" AND ").join(filters), limit=sql_limit)

            records = cursor.execute(query, params)

            bounds: Optional[Bounds] = None
            items = []
            for dbPic in records:
                if not bounds:
                    bounds = Bounds(min=dbPic["rank"], max=dbPic["rank"])
                else:
                    bounds.update(dbPic["rank"])

                items.append(dbPictureToStacItem(collectionId, dbPic))

            links = [
                get_root_link(),
                {
                    "rel": "parent",
                    "type": "application/json",
                    "href": url_for("stac_collections.getCollection", _external=True, collectionId=collectionId),
                },
                {
                    "rel": "self",
                    "type": "application/geo+json",
                    "href": url_for(
                        "stac_items.getCollectionItems",
                        _external=True,
                        collectionId=collectionId,
                        limit=limit,
                        startAfterRank=startAfterRank,
                    ),
                },
            ]

            if paginated and items and bounds:
                if bounds.min:
                    has_item_before = bounds.min > seqMeta["min_rank"]
                    if has_item_before:
                        links.append(
                            {
                                "rel": "first",
                                "type": "application/geo+json",
                                "href": url_for("stac_items.getCollectionItems", _external=True, collectionId=collectionId, limit=limit),
                            }
                        )
                        # Previous page link
                        #   - If limit is set, rank is current - limit -1
                        #   - If no limit is set, rank is 0 (none)
                        prevRank = bounds.min - limit - 1 if limit is not None else 0
                        if prevRank < 1:
                            prevRank = None
                        links.append(
                            {
                                "rel": "prev",
                                "type": "application/geo+json",
                                "href": url_for(
                                    "stac_items.getCollectionItems",
                                    _external=True,
                                    collectionId=collectionId,
                                    limit=limit,
                                    startAfterRank=prevRank,
                                ),
                            }
                        )

                has_item_after = bounds.max < seqMeta["max_rank"]
                if has_item_after:
                    links.append(
                        {
                            "rel": "next",
                            "type": "application/geo+json",
                            "href": url_for(
                                "stac_items.getCollectionItems",
                                _external=True,
                                collectionId=collectionId,
                                limit=limit,
                                startAfterRank=bounds.max,
                            ),
                        }
                    )

                    # Last page link
                    #   - If this page is the last one, rank equals to rank given by user
                    #   - Otherwise, rank equals max rank - limit

                    lastPageRank = startAfterRank
                    if limit is not None:
                        if seqMeta["max_rank"] > bounds.max:
                            lastPageRank = seqMeta["max_rank"] - limit
                            if lastPageRank < bounds.max:
                                lastPageRank = bounds.max

                    links.append(
                        {
                            "rel": "last",
                            "type": "application/geo+json",
                            "href": url_for(
                                "stac_items.getCollectionItems",
                                _external=True,
                                collectionId=collectionId,
                                limit=limit,
                                startAfterRank=lastPageRank,
                            ),
                        }
                    )

            return (
                {
                    "type": "FeatureCollection",
                    "features": items,
                    "links": links,
                },
                200,
                {"Content-Type": "application/geo+json"},
            )


def _getPictureItemById(collectionId, itemId):
    """Get a picture metadata by its ID and collection ID

    ---
    tags:
        - Pictures
    parameters:
        - name: collectionId
          in: path
          description: ID of collection to retrieve
          required: true
          schema:
            type: string
        - name: itemId
          in: path
          description: ID of item to retrieve
          required: true
          schema:
            type: string
    """
    with psycopg.connect(current_app.config["DB_URL"], row_factory=dict_row) as conn:
        with conn.cursor() as cursor:
            # Check if there is a logged user
            account = auth.get_current_account()
            accountId = account.id if account else None

            # Get rank + position of wanted picture
            record = cursor.execute(
                """
				SELECT
    				p.id, sp.rank, ST_AsGeoJSON(p.geom)::json AS geojson, p.heading, p.ts, p.metadata,
                    p.inserted_at, p.status, accounts.name AS account_name,
					spl.prevpic, spl.prevpicgeojson, spl.nextpic, spl.nextpicgeojson, p.exif,
                    relp.related_pics
				FROM pictures p
				JOIN sequences_pictures sp ON sp.pic_id = p.id
				JOIN accounts ON p.account_id = accounts.id
				JOIN sequences s ON sp.seq_id = s.id
				LEFT JOIN (
					SELECT
						p.id,
						LAG(p.id) OVER othpics AS prevpic,
						ST_AsGeoJSON(LAG(p.geom) OVER othpics)::json AS prevpicgeojson,
						LEAD(p.id) OVER othpics AS nextpic,
						ST_AsGeoJSON(LEAD(p.geom) OVER othpics)::json AS nextpicgeojson
					FROM pictures p
					JOIN sequences_pictures sp ON p.id = sp.pic_id
					WHERE
						sp.seq_id = %(seq)s
						AND (p.account_id = %(acc)s OR p.status != 'hidden')
					WINDOW othpics AS (PARTITION BY sp.seq_id ORDER BY sp.rank)
				) spl ON p.id = spl.id
                LEFT JOIN (
                    SELECT array_agg(ARRAY[seq_id::text, id::text, geom, tstxt]) AS related_pics
                    FROM (
                        SELECT DISTINCT ON (relsp.seq_id)
                            relsp.seq_id, relp.id,
                            ST_AsGeoJSON(relp.geom) as geom,
                            to_char(relp.ts at time zone 'UTC', 'YYYY-MM-DD"T"HH24:MI:SS"Z"') AS tstxt
                        FROM
                            pictures relp,
                            pictures p,
                            sequences_pictures relsp
                        WHERE
                            -- Related pictures are retrieved based on:
                            --   > Proximity (15m)
                            --   > Status (publicly available or from current user)
                            --   > Sequence (only one per sequence, the nearest one)
                            --   > Pic ID (not the current picture)
                            --   > Heading (either 360° or in less than 100° of diff with current picture)
                            p.id = %(pic)s
                            AND ST_Intersects(ST_Buffer(p.geom::geography, 15)::geometry, relp.geom)
                            AND (relp.account_id = %(acc)s OR relp.status = 'ready')
                            AND relp.status != 'waiting-for-delete'
                            AND relp.id != p.id
                            AND relsp.pic_id = relp.id
                            AND relsp.seq_id != %(seq)s
                            AND (
                                p.metadata->>'type' = 'equirectangular'
                                OR (relp.heading IS NULL OR p.heading IS NULL)
                                OR (
                                    relp.heading IS NOT NULL
                                    AND p.heading IS NOT NULL
                                    AND ABS(relp.heading - p.heading) <= 100
                                )
                            )
                        ORDER BY relsp.seq_id, p.geom <-> relp.geom
                    ) a
                ) relp ON TRUE
				WHERE sp.seq_id = %(seq)s
					AND p.id = %(pic)s
					AND (p.account_id = %(acc)s OR p.status != 'hidden')
					AND (s.status != 'hidden' OR s.account_id = %(acc)s)
                    AND s.status != 'deleted'
				""",
                {"seq": collectionId, "pic": itemId, "acc": accountId},
            ).fetchone()

            if record is None:
                return None

            return dbPictureToStacItem(collectionId, record)


@bp.route("/collections/<uuid:collectionId>/items/<uuid:itemId>")
def getCollectionItem(collectionId, itemId):
    """Get a single item from a collection
    ---
    tags:
        - Pictures
    parameters:
        - name: collectionId
          in: path
          description: ID of collection to retrieve
          required: true
          schema:
            type: string
        - name: itemId
          in: path
          description: ID of item to retrieve
          required: true
          schema:
            type: string
    responses:
        102:
            description: the item (which is still under process)
            content:
                application/geo+json:
                    schema:
                        $ref: '#/components/schemas/GeoVisioItem'
        200:
            description: the wanted item
            content:
                application/geo+json:
                    schema:
                        $ref: '#/components/schemas/GeoVisioItem'
    """

    stacItem = _getPictureItemById(collectionId, itemId)
    if stacItem is None:
        raise errors.InvalidAPIUsage("Item doesn't exist", status_code=404)

    account = auth.get_current_account()
    picStatusToHttpCode = {
        "waiting-for-process": 102,
        "ready": 200,
        "hidden": 200 if account else 404,
        "broken": 500,
    }
    return stacItem, picStatusToHttpCode[stacItem["properties"]["geovisio:status"]], {"Content-Type": "application/geo+json"}


@bp.route("/search", methods=["GET", "POST"])
def searchItems():
    """Search through all available items

    Note: when searching with a bounding box or a geometry, the items will be sorted by proximity of the center of this bounding box / geometry
    Else the items will not be sorted.
    ---
    tags:
        - Pictures
    get:
        parameters:
            - $ref: '#/components/parameters/STAC_bbox'
            - $ref: '#/components/parameters/STAC_intersects'
            - $ref: '#/components/parameters/STAC_datetime'
            - $ref: '#/components/parameters/STAC_limit'
            - $ref: '#/components/parameters/STAC_ids'
            - $ref: '#/components/parameters/STAC_collectionsArray'
    post:
        requestBody:
            required: true
            content:
              application/json:
                schema:
                  $ref: '#/components/schemas/STACItemSearchBody'
    responses:
        200:
            $ref: '#/components/responses/STAC_search'
    """

    account = auth.get_current_account()
    accountId = account.id if account is not None else None
    sqlWhere = [SQL("(p.status = 'ready' OR p.account_id = %(account)s)"), SQL("(is_sequence_visible_by_user(s, %(account)s))")]
    sqlParams: Dict[str, Any] = {"account": accountId}
    sqlSubQueryWhere = [SQL("(p.status = 'ready' OR p.account_id = %(account)s)")]

    order_by = SQL("")

    #
    # Parameters parsing and verification
    #

    # Method + content-type
    args: MultiDict[str, str]
    if request.method == "POST":
        if request.headers.get("Content-Type") != "application/json":
            raise errors.InvalidAPIUsage("Search using POST method should have a JSON body", status_code=400)
        args = MultiDict(request.json)
    else:
        args = request.args

    # Limit
    if args.get("limit") is not None:
        limit = args.get("limit", type=int)
        if limit is None or limit < 1 or limit > 10000:
            raise errors.InvalidAPIUsage("Parameter limit must be either empty or a number between 1 and 10000", status_code=400)
        else:
            sqlParams["limit"] = limit
    else:
        sqlParams["limit"] = 10

    # Bounding box
    bboxarg = parse_bbox(args.getlist("bbox"))
    if bboxarg is not None:
        sqlWhere.append(SQL("p.geom && ST_MakeEnvelope(%(minx)s, %(miny)s, %(maxx)s, %(maxy)s, 4326)"))
        sqlParams["minx"] = bboxarg[0]
        sqlParams["miny"] = bboxarg[1]
        sqlParams["maxx"] = bboxarg[2]
        sqlParams["maxy"] = bboxarg[3]
        # if we search by bbox, we'll give first the items near the center of the bounding box
        order_by = SQL("ORDER BY p.geom <-> ST_Centroid(ST_MakeEnvelope(%(minx)s, %(miny)s, %(maxx)s, %(maxy)s, 4326))")

    # Datetime
    min_dt, max_dt = parse_datetime_interval(args.get("datetime"))
    if min_dt is not None:
        sqlWhere.append(SQL("p.ts >= %(mints)s::timestamp with time zone"))
        sqlParams["mints"] = min_dt

    if max_dt is not None:
        sqlWhere.append(SQL("p.ts <= %(maxts)s::timestamp with time zone"))
        sqlParams["maxts"] = max_dt

    # Intersects
    if args.get("intersects") is not None:
        try:
            intersects = json.loads(args["intersects"])
        except:
            raise errors.InvalidAPIUsage("Parameter intersects should contain a valid GeoJSON Geometry (not a Feature)", status_code=400)
        if intersects["type"] == "Point":
            sqlWhere.append(SQL("p.geom && ST_Expand(ST_GeomFromGeoJSON(%(geom)s), 0.000001)"))
        else:
            sqlWhere.append(SQL("p.geom && ST_GeomFromGeoJSON(%(geom)s)"))
            sqlWhere.append(SQL("ST_Intersects(p.geom, ST_GeomFromGeoJSON(%(geom)s))"))
        sqlParams["geom"] = Jsonb(intersects)
        # if we search by bbox, we'll give first the items near the center of the bounding box
        order_by = SQL("ORDER BY p.geom <-> ST_Centroid(ST_GeomFromGeoJSON(%(geom)s))")

    # Ids
    if args.get("ids") is not None:
        sqlWhere.append(SQL("p.id = ANY(%(ids)s)"))
        try:
            sqlParams["ids"] = [UUID(j) for j in parse_list(args.get("ids"), paramName="ids")]
        except:
            raise errors.InvalidAPIUsage("Parameter ids should be a JSON array of strings", status_code=400)

    # Collections
    if args.get("collections") is not None:
        sqlWhere.append(SQL("sp.seq_id = ANY(%(collections)s)"))

        # custom subquery filtering to help PG query plan
        sqlSubQueryWhere.append(SQL("sp.seq_id = ANY(%(collections)s)"))

        try:
            sqlParams["collections"] = [UUID(j) for j in parse_list(args["collections"], paramName="collections")]
        except:
            raise errors.InvalidAPIUsage("Parameter collections should be a JSON array of strings", status_code=400)

    # To speed up search, if it's a search by id and on only one id, we use the same code as /collections/:cid/items/:id
    if args.get("ids") is not None and args:
        ids = parse_list(args.get("ids"), paramName="ids")
        if ids and len(ids) == 1:
            picture_id = ids[0]

            with psycopg.connect(current_app.config["DB_URL"]) as conn, conn.cursor() as cursor:
                seq = cursor.execute("SELECT seq_id FROM sequences_pictures WHERE pic_id = %s", [picture_id]).fetchone()
                if not seq:
                    raise errors.InvalidAPIUsage("Picture doesn't exist", status_code=404)

                item = _getPictureItemById(seq[0], UUID(picture_id))
                features = [item] if item else []
                return (
                    {"type": "FeatureCollection", "features": features, "links": [get_root_link()]},
                    200,
                    {"Content-Type": "application/geo+json"},
                )

    #
    # Database query
    #

    with psycopg.connect(current_app.config["DB_URL"], row_factory=dict_row, options="-c statement_timeout=30000") as conn:
        with conn.cursor() as cursor:
            query = SQL(
                """
            SELECT * FROM (
				SELECT
					p.id, p.ts, p.heading, p.metadata, p.inserted_at,
					ST_AsGeoJSON(p.geom)::json AS geojson,
					sp.seq_id, sp.rank AS rank,
					accounts.name AS account_name, p.exif
				FROM pictures p
				LEFT JOIN sequences_pictures sp ON p.id = sp.pic_id
				LEFT JOIN sequences s ON s.id = sp.seq_id
				LEFT JOIN accounts ON p.account_id = accounts.id
				WHERE {sqlWhere}
				{orderBy}
				LIMIT %(limit)s
    ) pic
LEFT JOIN LATERAL (
    SELECT
    p.id AS prevpic, ST_AsGeoJSON(p.geom)::json AS prevpicgeojson
    FROM sequences_pictures sp
    JOIN pictures p ON sp.pic_id = p.id
    WHERE pic.seq_id = sp.seq_id AND {sqlSubQueryWhere} AND sp.rank < pic.rank 
    ORDER BY sp.rank DESC 
    LIMIT 1
) prev on true
LEFT JOIN LATERAL (
    SELECT
    p.id AS nextpic, ST_AsGeoJSON(p.geom)::json AS nextpicgeojson
    FROM sequences_pictures sp
    JOIN pictures p ON sp.pic_id = p.id
    WHERE pic.seq_id = sp.seq_id AND {sqlSubQueryWhere} AND sp.rank > pic.rank 
    ORDER BY sp.rank ASC 
    LIMIT 1
) next on true
;
			"""
            ).format(sqlWhere=SQL(" AND ").join(sqlWhere), sqlSubQueryWhere=SQL(" AND ").join(sqlSubQueryWhere), orderBy=order_by)
            records = cursor.execute(query, sqlParams)

            items = [dbPictureToStacItem(str(dbPic["seq_id"]), dbPic) for dbPic in records]

            return (
                {
                    "type": "FeatureCollection",
                    "features": items,
                    "links": [
                        get_root_link(),
                    ],
                },
                200,
                {"Content-Type": "application/geo+json"},
            )


@bp.route("/collections/<uuid:collectionId>/items", methods=["POST"])
@auth.login_required_by_setting("API_FORCE_AUTH_ON_UPLOAD")
def postCollectionItem(collectionId, account=None):
    """Add a new picture in a given sequence
    ---
    tags:
        - Upload
    parameters:
        - name: collectionId
          in: path
          description: ID of sequence to add this picture into
          required: true
          schema:
            type: string
    requestBody:
        content:
            multipart/form-data:
                schema:
                    $ref: '#/components/schemas/GeoVisioPostItem'
    security:
        - bearerToken: []
        - cookieAuth: []
    responses:
        202:
            description: the added picture metadata
            content:
                application/geo+json:
                    schema:
                        $ref: '#/components/schemas/GeoVisioItem'
    """

    if not request.headers.get("Content-Type", "").startswith("multipart/form-data"):
        raise errors.InvalidAPIUsage("Content type should be multipart/form-data", status_code=415)

    # Check if position was given
    if request.form.get("position") is None:
        raise errors.InvalidAPIUsage('Missing "position" parameter', status_code=400)
    else:
        try:
            position = int(request.form["position"])
            if position <= 0:
                raise ValueError()
        except ValueError:
            raise errors.InvalidAPIUsage("Position in sequence should be a positive integer", status_code=400)

    # Check if datetime was given
    ext_mtd = PictureMetadata()
    if request.form.get("override_capture_time") is not None:
        ext_mtd.capture_time = parse_datetime(
            request.form.get("override_capture_time"),
            error="Parameter `override_capture_time` is not a valid datetime, it should be an iso formated datetime (like '2017-07-21T17:32:28Z').",
        )

    # Check if lat/lon were given
    lon, lat = request.form.get("override_longitude"), request.form.get("override_latitude")
    if lon is not None or lat is not None:
        if lat is None:
            raise errors.InvalidAPIUsage("Longitude cannot be overridden alone, override_latitude also needs to be set")
        if lon is None:
            raise errors.InvalidAPIUsage("Latitude cannot be overridden alone, override_longitude also needs to be set")
        lon = as_longitude(lon, error=f"For parameter `override_longitude`, `{lon}` is not a valid longitude")
        lat = as_latitude(lat, error=f"For parameter `override_latitude`, `{lat}` is not a valid latitude")
        ext_mtd.longitude = lon
        ext_mtd.latitude = lat

    # Check if others override elements were given
    override_elmts = {}
    for k, v in request.form.to_dict().items():
        if not (k.startswith("override_Exif.") or k.startswith("override_Xmp.")):
            continue
        exif_tag = k.replace("override_", "")
        override_elmts[exif_tag] = v

    if override_elmts:
        ext_mtd.additional_exif = override_elmts

    # Check if picture blurring status is valid
    if request.form.get("isBlurred") is None or request.form.get("isBlurred") in ["true", "false"]:
        isBlurred = request.form.get("isBlurred") == "true"
    else:
        raise errors.InvalidAPIUsage("Picture blur status should be either unset, true or false", status_code=400)

    # Check if a picture file was given
    if "picture" not in request.files:
        raise errors.InvalidAPIUsage("No picture file was sent", status_code=400)
    else:
        picture = request.files["picture"]

        # Check file validity
        if not (picture.filename != "" and "." in picture.filename and picture.filename.rsplit(".", 1)[1].lower() in ["jpg", "jpeg"]):
            raise errors.InvalidAPIUsage("Picture file is either missing or in an unsupported format (should be jpg)", status_code=400)

    with psycopg.connect(current_app.config["DB_URL"]) as conn:
        with conn.cursor() as cursor:
            # Check if sequence exists
            seq = cursor.execute("SELECT id FROM sequences WHERE id = %s", [collectionId]).fetchone()
            if not seq or len(seq) != 1:
                raise errors.InvalidAPIUsage(f"Sequence {collectionId} wasn't found in database", status_code=404)

            # Compute various metadata
            accountId = accountIdOrDefault(account)
            raw_pic = picture.read()
            filesize = len(raw_pic)

            additionalMetadata = {
                "blurredByAuthor": isBlurred,
                "originalFileName": os.path.basename(picture.filename),
                "originalFileSize": filesize,
            }

            # Update picture metadata if needed
            updated_picture = writePictureMetadata(raw_pic, ext_mtd)

            # Insert picture into database
            try:
                picId = utils.pictures.insertNewPictureInDatabase(
                    conn, collectionId, position, updated_picture, accountId, additionalMetadata
                )
            except utils.pictures.PicturePositionConflict:
                raise errors.InvalidAPIUsage("Picture at given position already exist", status_code=409)
            except utils.pictures.MetadataReadingError as e:
                raise errors.InvalidAPIUsage("Impossible to parse picture metadata", payload={"details": {"error": e.details}})

            # Save file into appropriate filesystem
            try:
                utils.pictures.saveRawPicture(picId, updated_picture, isBlurred)
            except:
                logging.exception("Picture wasn't correctly saved in filesystem")
                raise errors.InvalidAPIUsage("Picture wasn't correctly saved in filesystem", status_code=500)

            conn.commit()

            runner_pictures.background_processor.process_pictures()

            # Return picture metadata
            return (
                getCollectionItem(collectionId, picId)[0],
                202,
                {
                    "Content-Type": "application/json",
                    "Access-Control-Expose-Headers": "Location",  # Needed for allowing web browsers access Location header
                    "Location": url_for("stac_items.getCollectionItem", _external=True, collectionId=collectionId, itemId=picId),
                },
            )


@bp.route("/collections/<uuid:collectionId>/items/<uuid:itemId>", methods=["PATCH"])
@auth.login_required()
def patchCollectionItem(collectionId, itemId, account):
    """Edits properties of an existing picture
    ---
    tags:
        - Editing
    parameters:
        - name: collectionId
          in: path
          description: ID of sequence the picture belongs to
          required: true
          schema:
            type: string
        - name: itemId
          in: path
          description: ID of picture to edit
          required: true
          schema:
            type: string
    requestBody:
        content:
            application/json:
                schema:
                    $ref: '#/components/schemas/GeoVisioPatchItem'
            application/x-www-form-urlencoded:
                schema:
                    $ref: '#/components/schemas/GeoVisioPatchItem'
            multipart/form-data:
                schema:
                    $ref: '#/components/schemas/GeoVisioPatchItem'
    security:
        - bearerToken: []
        - cookieAuth: []
    responses:
        200:
            description: the wanted item
            content:
                application/geo+json:
                    schema:
                        $ref: '#/components/schemas/GeoVisioItem'
    """

    # Parse received parameters
    metadata = {}
    content_type = (request.headers.get("Content-Type") or "").split(";")[0]
    if request.is_json:
        metadata["visible"] = request.json.get("visible")
    elif content_type in ["multipart/form-data", "application/x-www-form-urlencoded"]:
        metadata["visible"] = request.form.get("visible")

    # Check if visibility param is valid
    if metadata.get("visible") is None:
        # /!\ As visible is the only editable thing for now, we can return if it's null
        # The line below may be removed when other parameters will be available for patching
        # Otherwise, you might want to do: visible = None
        return getCollectionItem(collectionId, itemId)

    elif metadata.get("visible") in ["true", "false"]:
        visible = metadata.get("visible") == "true"
    else:
        raise errors.InvalidAPIUsage("Picture visibility parameter (visible) should be either unset, true or false", status_code=400)

    # Check if picture exists and if given account is authorized to edit
    with psycopg.connect(current_app.config["DB_URL"]) as conn:
        with conn.cursor() as cursor:
            pic = cursor.execute("SELECT status, account_id FROM pictures WHERE id = %s", [itemId]).fetchone()

            # Picture not found
            if not pic:
                raise errors.InvalidAPIUsage(f"Picture {itemId} wasn't found in database", status_code=404)

            # Account associated to picture doesn't match current user
            if account is not None and account.id != str(pic[1]):
                raise errors.InvalidAPIUsage("You're not authorized to edit this picture", status_code=403)

            # Let's edit this picture
            oldStatus = pic[0]
            newStatus = None

            if visible is not None:
                if visible is True and oldStatus == "hidden":
                    newStatus = "ready"
                elif visible is False and oldStatus == "ready":
                    newStatus = "hidden"
                elif (visible is True and oldStatus == "ready") or (visible is False and oldStatus == "hidden"):
                    newStatus = oldStatus

                    # /!\ As visible is the only editable thing for now, we can return if it's unchanged
                    # The line below may be removed when other parameters will be available for patching
                    return getCollectionItem(collectionId, itemId)

                else:
                    # Picture is in a preparing/broken/... state so no edit possible
                    raise errors.InvalidAPIUsage(
                        f"Picture {itemId} is in {oldStatus} state, its visibility can't be changed for now", status_code=400
                    )

            if newStatus:
                cursor.execute("UPDATE pictures SET status = %s WHERE id = %s", [newStatus, itemId])
                conn.commit()

            # Redirect response to a classic GET
            return getCollectionItem(collectionId, itemId)


@bp.route("/collections/<uuid:collectionId>/items/<uuid:itemId>", methods=["DELETE"])
@auth.login_required()
def deleteCollectionItem(collectionId, itemId, account):
    """Delete an existing picture
    ---
    tags:
        - Editing
    parameters:
        - name: collectionId
          in: path
          description: ID of sequence the picture belongs to
          required: true
          schema:
            type: string
        - name: itemId
          in: path
          description: ID of picture to edit
          required: true
          schema:
            type: string
    security:
        - bearerToken: []
        - cookieAuth: []
    responses:
        204:
            description: The object has been correctly deleted
    """

    # Check if picture exists and if given account is authorized to edit
    with psycopg.connect(current_app.config["DB_URL"]) as conn:
        with conn.cursor() as cursor:
            pic = cursor.execute("SELECT status, account_id FROM pictures WHERE id = %s", [itemId]).fetchone()

            # Picture not found
            if not pic:
                raise errors.InvalidAPIUsage(f"Picture {itemId} wasn't found in database", status_code=404)

            # Account associated to picture doesn't match current user
            if account is not None and account.id != str(pic[1]):
                raise errors.InvalidAPIUsage("You're not authorized to edit this picture", status_code=403)

            cursor.execute("DELETE FROM pictures WHERE id = %s", [itemId])

            # delete images
            utils.pictures.removeAllFiles(itemId)

            conn.commit()

            return "", 204


def _getHDJpgPictureURL(picId: str, status: Optional[str]):
    external_url = utils.pictures.getPublicHDPictureExternalUrl(picId, format="jpg")
    if external_url and status == "ready":  # we always serve non ready pictures through the API to be able to check permission:
        return external_url
    return url_for("pictures.getPictureHD", _external=True, pictureId=picId, format="jpg")


def _getSDJpgPictureURL(picId: str, status: Optional[str]):
    external_url = utils.pictures.getPublicDerivatePictureExternalUrl(picId, format="jpg", derivateFileName="sd.jpg")
    if external_url and status == "ready":  # we always serve non ready pictures through the API to be able to check permission:
        return external_url
    return url_for("pictures.getPictureSD", _external=True, pictureId=picId, format="jpg")


def _getThumbJpgPictureURL(picId: str, status: Optional[str]):
    external_url = utils.pictures.getPublicDerivatePictureExternalUrl(picId, format="jpg", derivateFileName="thumb.jpg")
    if external_url and status == "ready":  # we always serve non ready pictures through the API to be able to check permission
        return external_url
    return url_for("pictures.getPictureThumb", _external=True, pictureId=picId, format="jpg")


def _getTilesJpgPictureURL(picId: str, status: Optional[str]):
    external_url = utils.pictures.getPublicDerivatePictureExternalUrl(picId, format="jpg", derivateFileName="tiles/{TileCol}_{TileRow}.jpg")
    if external_url and status == "ready":  # we always serve non ready pictures through the API to be able to check permission:
        return external_url
    return unquote(url_for("pictures.getPictureTile", _external=True, pictureId=picId, format="jpg", col="{TileCol}", row="{TileRow}"))
