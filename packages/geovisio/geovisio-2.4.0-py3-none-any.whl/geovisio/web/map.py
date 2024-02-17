# Some parts of code here are heavily inspired from Paul Ramsey's work
# See for reference : https://github.com/pramsey/minimal-mvt

import psycopg
import io
from typing import Optional, Dict, Any, Tuple, List
from uuid import UUID
from flask import Blueprint, current_app, send_file, request
from geovisio.utils import auth
from geovisio.utils.auth import Account
from geovisio.web import params
from geovisio.web.utils import user_dependant_response
from geovisio import errors
from psycopg import sql

bp = Blueprint("map", __name__, url_prefix="/api")


def checkTileValidity(z, x, y, format):
    """Check if tile parameters are valid

    Parameters
    ----------
    z : number
            Zoom level
    x : number
            X coordinate
    y : number
            Y coordinate
    format : string
            Tile format

    Exception
    ---------
    raises InvalidAPIUsage exceptions if parameters are not OK
    """
    if z is None or x is None or y is None or format is None:
        raise errors.InvalidAPIUsage("One of required parameter is empty", status_code=404)
    if format not in ["pbf", "mvt"]:
        raise errors.InvalidAPIUsage("Tile format is invalid, should be either pbf or mvt", status_code=400)

    size = 2**z
    if x >= size or y >= size:
        raise errors.InvalidAPIUsage("X or Y parameter is out of bounds", status_code=404)
    if x < 0 or y < 0:
        raise errors.InvalidAPIUsage("X or Y parameter is out of bounds", status_code=404)
    if z < 0 or z > 14:
        raise errors.InvalidAPIUsage("Z parameter is out of bounds (should be 0-14)", status_code=404)


def _getTile(z: int, x: int, y: int, format: str, onlyForUser: Optional[UUID] = None, filter: Optional[sql.SQL] = None):
    checkTileValidity(z, x, y, format)

    with psycopg.connect(current_app.config["DB_URL"], options="-c statement_timeout=10000") as conn:
        with conn.cursor() as cursor:
            query, params = _get_query(z, x, y, onlyForUser, additional_filter=filter)
            res = cursor.execute(query, params).fetchone()

            if not res:
                raise errors.InternalError("Impossible to get tile")

            res = res[0]
            return send_file(io.BytesIO(res), mimetype="application/vnd.mapbox-vector-tile")


@bp.route("/map/<int:z>/<int:x>/<int:y>.<format>")
@user_dependant_response(False)
def getTile(z: int, x: int, y: int, format: str):
    """Get pictures and sequences as vector tiles

    Vector tiles contains possibly two layers : sequences and pictures.

    Layer "sequences":
      - Available on all zoom levels
      - Available properties (all levels)
        - id (sequence ID)
      - Other properties (available on zoom levels >= 13)
        - account_id
        - model (camera make and model)
        - type (flat or equirectangular)
        - date (capture date, as YYYY-MM-DD)

    Layer "pictures":
      - Available on zoom levels >= 13
      - Available properties:
        - id (picture ID)
        - account_id
        - ts (picture date/time)
        - heading (picture heading in degrees)
            - sequences (list of sequences ID this pictures belongs to)
        - type (flat or equirectangular)
        - model (camera make and model)
    ---
    tags:
        - Map
        - Pictures
        - Sequences
    parameters:
        - name: z
          in: path
          description: Zoom level (6 to 14)
          required: true
          schema:
            type: number
        - name: x
          in: path
          description: X coordinate
          required: true
          schema:
            type: number
        - name: y
          in: path
          description: Y coordinate
          required: true
          schema:
            type: number
        - name: format
          in: path
          description: Tile format (mvt, pbf)
          required: true
          schema:
            type: string
    responses:
        200:
            description: Sequences vector tile
            content:
                application/vnd.mapbox-vector-tile:
                    schema:
                        type: string
                        format: binary
    """
    return _getTile(z, x, y, format, onlyForUser=None)


def _get_query(z: int, x: int, y: int, onlyForUser: Optional[UUID], additional_filter: Optional[sql.SQL]) -> Tuple[sql.Composed, Dict]:
    """Returns appropriate SQL query according to given zoom"""

    sequences_filter: List[sql.Composable] = [sql.SQL("s.geom && ST_Transform(ST_TileEnvelope(%(z)s, %(x)s, %(y)s), 4326)")]
    pictures_filter: List[sql.Composable] = [sql.SQL("p.geom && ST_Transform(ST_TileEnvelope(%(z)s, %(x)s, %(y)s), 4326)")]
    params: Dict[str, Any] = {"x": x, "y": y, "z": z}

    account = auth.get_current_account()
    accountId = account.id if account is not None else None
    # we never want to display deleted sequences on the map
    sequences_filter.append(sql.SQL("s.status != 'deleted'"))
    pictures_filter.append(sql.SQL("p.status != 'waiting-for-delete'"))

    if onlyForUser:
        sequences_filter.append(sql.SQL("s.account_id = %(account)s"))
        pictures_filter.append(sql.SQL("p.account_id = %(account)s"))
        params["account"] = onlyForUser

    # we want to show only 'ready' collection to the general users
    if not onlyForUser or accountId != str(onlyForUser):
        sequences_filter.append(sql.SQL("s.status = 'ready'"))
        pictures_filter.append(sql.SQL("p.status = 'ready'"))
        pictures_filter.append(sql.SQL("s.status = 'ready'"))

    if additional_filter:
        sequences_filter.append(additional_filter)
        filter_str = additional_filter.as_string(None)
        if "status" in filter_str:
            # hack to have a coherent filter between the APIs
            # if asked for status='hidden', we want both hidden pics and hidden sequences
            pic_additional_filter_str = filter_str.replace("s.status", "p.status")
            pic_additional_filter = sql.SQL(pic_additional_filter_str)  # type: ignore
            pictures_filter.append(sql.SQL("(") + sql.SQL(" OR ").join([pic_additional_filter, additional_filter]) + sql.SQL(")"))

    sequences_fields = [
        sql.SQL("ST_AsMVTGeom(ST_Transform(geom, 3857), ST_TileEnvelope(%(z)s, %(x)s, %(y)s)) AS geom"),
        sql.SQL("id"),
    ]
    simplified_sequence_fields = [
        sql.SQL("ST_Simplify(geom, 0.01) AS geom"),
        sql.SQL("id"),
        sql.SQL("status"),
    ]
    if z >= 7 or onlyForUser:
        sequences_fields.extend(
            [
                sql.SQL("account_id"),
                sql.SQL("NULLIF(status != 'ready', FALSE) AS hidden"),
                sql.SQL("computed_model AS model"),
                sql.SQL("computed_type AS type"),
                sql.SQL("computed_capture_date AS date"),
            ]
        )
        simplified_sequence_fields.extend(
            [
                sql.SQL("account_id"),
                sql.SQL("computed_model"),
                sql.SQL("computed_type"),
                sql.SQL("computed_capture_date"),
            ]
        )
    if z >= 13:
        query = sql.SQL(
            """
SELECT mvtsequences.mvt || mvtpictures.mvt
FROM (
    SELECT ST_AsMVT(mvtgeomseqs.*, 'sequences') AS mvt
    FROM (
	SELECT
	    {sequences_fields}
	FROM sequences s
	WHERE
	    {sequences_filter}
    ) mvtgeomseqs
) mvtsequences,
(
    SELECT ST_AsMVT(mvtgeompics.*, 'pictures') AS mvt
    FROM (
	SELECT
	    ST_AsMVTGeom(ST_Transform(p.geom, 3857), ST_TileEnvelope(%(z)s, %(x)s, %(y)s)) AS geom,
	    p.id, p.ts, p.heading, p.account_id,
	    NULLIF(p.status != 'ready' OR s.status != 'ready', FALSE) AS hidden,
	    array_to_json(ARRAY_AGG(sp.seq_id)) AS sequences,
        p.metadata->>'type' AS type,
        TRIM(CONCAT(p.metadata->>'make', ' ', p.metadata->>'model')) AS model
	FROM pictures p
	LEFT JOIN sequences_pictures sp ON p.id = sp.pic_id
	LEFT JOIN sequences s ON s.id = sp.seq_id
	WHERE
	    {pictures_filter} 
	GROUP BY 1, 2, 3, 4, 5, 6
    ) mvtgeompics
) mvtpictures
"""
        ).format(
            sequences_filter=sql.SQL(" AND ").join(sequences_filter),
            pictures_filter=sql.SQL(" AND ").join(pictures_filter),
            sequences_fields=sql.SQL(", ").join(sequences_fields),
        )

    elif z >= 7:
        query = sql.SQL(
            """
SELECT ST_AsMVT(mvtsequences.*, 'sequences') AS mvt
FROM (
    SELECT
	    {sequences_fields}
    FROM sequences s
    WHERE
        {sequences_filter}
) mvtsequences
"""
        ).format(sequences_filter=sql.SQL(" AND ").join(sequences_filter), sequences_fields=sql.SQL(", ").join(sequences_fields))
    else:
        query = sql.SQL(
            """
SELECT ST_AsMVT(mvtsequences.*, 'sequences') AS mvt
FROM (
    SELECT
	    {sequences_fields}
    FROM (
        SELECT {simplified_sequence_fields}
        FROM sequences s
        WHERE
            {sequences_filter}
    ) s
    WHERE geom IS NOT NULL
) mvtsequences
"""
        ).format(
            sequences_filter=sql.SQL(" AND ").join(sequences_filter),
            sequences_fields=sql.SQL(", ").join(sequences_fields),
            simplified_sequence_fields=sql.SQL(", ").join(simplified_sequence_fields),
        )

    return query, params


@bp.route("/users/<uuid:userId>/map/<int:z>/<int:x>/<int:y>.<format>")
def getUserTile(userId: UUID, z: int, x: int, y: int, format: str):
    """Get pictures and sequences as vector tiles for a specific user.
    This tile will contain the same layers as the generic tiles (from `/map/z/x/y.format` route), but with sequences properties on all levels

    ---
    tags:
        - Map
        - Pictures
        - Sequences
        - Users
    parameters:
        - name: userId
          in: path
          description: User ID
          required: true
          schema:
            type: string
        - name: z
          in: path
          description: Zoom level (6 to 14)
          required: true
          schema:
            type: number
        - name: x
          in: path
          description: X coordinate
          required: true
          schema:
            type: number
        - name: y
          in: path
          description: Y coordinate
          required: true
          schema:
            type: number
        - name: format
          in: path
          description: Tile format (mvt, pbf)
          required: true
          schema:
            type: string
        - $ref: '#/components/parameters/tiles_filter'
    responses:
        200:
            description: Sequences vector tile
            content:
                application/vnd.mapbox-vector-tile:
                    schema:
                        type: string
                        format: binary
    """

    filter = params.parse_filter(request.args.get("filter"))
    return _getTile(z, x, y, format, onlyForUser=userId, filter=filter)


@bp.route("/users/me/map/<int:z>/<int:x>/<int:y>.<format>")
@auth.login_required_with_redirect()
def getMyTile(account: Account, z: int, x: int, y: int, format: str):
    """Get pictures and sequences as vector tiles for a specific logged user.
    This tile will contain the same layers as the generic tiles (from `/map/z/x/y.format` route), but with sequences properties on all levels

    ---
    tags:
        - Map
        - Pictures
        - Sequences
        - Users
    parameters:
        - name: z
          in: path
          description: Zoom level (6 to 14)
          required: true
          schema:
            type: number
        - name: x
          in: path
          description: X coordinate
          required: true
          schema:
            type: number
        - name: y
          in: path
          description: Y coordinate
          required: true
          schema:
            type: number
        - name: format
          in: path
          description: Tile format (mvt, pbf)
          required: true
          schema:
            type: string
        - $ref: '#/components/parameters/tiles_filter'
    responses:
        200:
            description: Sequences vector tile
            content:
                application/vnd.mapbox-vector-tile:
                    schema:
                        type: string
                        format: binary
    """
    filter = params.parse_filter(request.args.get("filter"))
    return _getTile(z, x, y, format, onlyForUser=UUID(account.id), filter=filter)
