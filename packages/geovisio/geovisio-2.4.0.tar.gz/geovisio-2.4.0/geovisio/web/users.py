import flask
from flask import request, current_app
from geovisio.utils import auth
from geovisio import errors
import psycopg
from psycopg.rows import dict_row
from psycopg.sql import SQL

bp = flask.Blueprint("user", __name__, url_prefix="/api/users")


def _get_user_info(id, name):
    userMapUrl = (
        flask.url_for("map.getUserTile", userId=id, x="111", y="222", z="333", format="mvt", _external=True)
        .replace("111", "{x}")
        .replace("222", "{y}")
        .replace("333", "{z}")
    )
    response = {
        "id": id,
        "name": name,
        "links": [
            {"rel": "catalog", "type": "application/json", "href": flask.url_for("stac.getUserCatalog", userId=id, _external=True)},
            {
                "rel": "collection",
                "type": "application/json",
                "href": flask.url_for("stac_collections.getUserCollection", userId=id, _external=True),
            },
            {
                "rel": "user-xyz",
                "type": "application/vnd.mapbox-vector-tile",
                "href": userMapUrl,
                "title": "Pictures and sequences vector tiles for a given user",
            },
        ],
    }
    return flask.jsonify(response)


@bp.route("/me")
@auth.login_required_with_redirect()
def getMyUserInfo(account):
    """Get current logged user informations
    ---
    tags:
        - Users
    responses:
        200:
            description: Information about the logged account
            content:
                application/json:
                    schema:
                        $ref: '#/components/schemas/GeoVisioUser'
    """
    return _get_user_info(account.id, account.name)


@bp.route("/<uuid:userId>")
def getUserInfo(userId):
    """Get user informations
    ---
    tags:
        - Users
    parameters:
        - name: userId
          in: path
          description: User ID
          required: true
          schema:
            type: string
    responses:
        200:
            description: Information about a user
            content:
                application/json:
                    schema:
                        $ref: '#/components/schemas/GeoVisioUser'
    """
    with psycopg.connect(current_app.config["DB_URL"], row_factory=dict_row) as conn, conn.cursor() as cursor:
        account = cursor.execute(SQL("SELECT name, id FROM accounts WHERE id = %s"), [userId]).fetchone()
        if not account:
            raise errors.InvalidAPIUsage("Impossible to find user", status_code=404)

        return _get_user_info(account["id"], account["name"])


@bp.route("/me/catalog")
@auth.login_required_with_redirect()
def getMyCatalog(account):
    """Get current logged user catalog
    ---
    tags:
        - Users
        - Sequences
    responses:
        200:
            description: the Catalog listing all sequences associated to given user. Note that it's similar to the user's colletion, but with less metadata since a STAC collection is an enhanced STAC catalog.
            content:
                application/json:
                    schema:
                        $ref: '#/components/schemas/GeoVisioCatalog'
    """
    return flask.redirect(flask.url_for("stac.getUserCatalog", userId=account.id, _external=True))


@bp.route("/me/collection")
@auth.login_required_with_redirect()
def getMyCollection(account):
    """Get current logged user collection
    ---
    tags:
        - Users
        - Sequences
    parameters:
        - $ref: '#/components/parameters/STAC_collections_limit'
        - $ref: '#/components/parameters/STAC_collections_filter'
        - $ref: '#/components/parameters/STAC_bbox'
        - $ref: '#/components/parameters/OGC_sortby'
    responses:
        200:
            description: the Collection listing all sequences associated to given user. Note that it's similar to the user's catalog, but with more metadata since a STAC collection is an enhanced STAC catalog.
            content:
                application/json:
                    schema:
                        $ref: '#/components/schemas/GeoVisioCollectionOfCollection'
    """

    return flask.redirect(
        flask.url_for(
            "stac_collections.getUserCollection",
            userId=account.id,
            filter=request.args.get("filter"),
            limit=request.args.get("limit"),
            sortby=request.args.get("sortby"),
            bbox=request.args.get("bbox"),
            _external=True,
        )
    )


@bp.route("/search")
def searchUser():
    """Search for a user
    ---
    tags:
        - Users
    responses:
        200:
            description: List of matching users
            content:
                application/json:
                    schema:
                        $ref: '#/components/schemas/GeoVisioUserSearch'
    """
    q = request.args.get("q")
    # for the moment, we can only search by string
    if not q:
        raise errors.InvalidAPIUsage("No search parameter given, you should provide `q=<pattern>` as query parameter", status_code=400)

    limit = request.args.get("limit", default=20, type=int)

    with psycopg.connect(current_app.config["DB_URL"], row_factory=dict_row) as conn, conn.cursor() as cursor:
        res = cursor.execute(
            SQL(
                """
WITH ranked AS (
    SELECT name, id, similarity({q}, name) AS similarity from accounts
)
SELECT * from ranked 
WHERE similarity > 0.1
ORDER BY similarity DESC
LIMIT {limit};
"""
            ).format(limit=limit, q=q)
        ).fetchall()
        return {
            "features": [
                {
                    "label": r["name"],
                    "id": r["id"],
                    "links": [
                        {
                            "rel": "user-info",
                            "type": "application/json",
                            "href": flask.url_for("user.getUserInfo", userId=r["id"], _external=True),
                        },
                        {
                            "rel": "collection",
                            "type": "application/json",
                            "href": flask.url_for("stac_collections.getUserCollection", userId=r["id"], _external=True),
                        },
                    ],
                }
                for r in res
            ]
        }


@bp.route("/")
def listUsers():
    """List all users
    ---
    tags:
        - Users
    responses:
        200:
            description: List of users
            content:
                application/json:
                    schema:
                        $ref: '#/components/schemas/GeoVisioUserList'
    """

    # no pagination yet, can be done when needed
    limit = min(request.args.get("limit", default=1000, type=int), 1000)

    with psycopg.connect(current_app.config["DB_URL"], row_factory=dict_row) as conn, conn.cursor() as cursor:
        res = cursor.execute(SQL("""SELECT name, id FROM accounts LIMIT {limit};""").format(limit=limit)).fetchall()
        return {
            "users": [
                {
                    "name": r["name"],
                    "id": r["id"],
                    "links": [
                        {
                            "rel": "user-info",
                            "type": "application/json",
                            "href": flask.url_for("user.getUserInfo", userId=r["id"], _external=True),
                        },
                        {
                            "rel": "collection",
                            "type": "application/json",
                            "href": flask.url_for("stac_collections.getUserCollection", userId=r["id"], _external=True),
                        },
                    ],
                }
                for r in res
            ],
            "links": [
                {
                    "rel": "user-search",
                    "type": "application/json",
                    "href": flask.url_for("user.searchUser", _external=True),
                    "title": "Search users",
                },
            ],
        }
