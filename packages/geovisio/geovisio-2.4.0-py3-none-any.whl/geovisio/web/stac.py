import psycopg
from psycopg.sql import SQL
from flask import Blueprint, current_app, request, url_for
from geovisio import errors
from geovisio.utils import auth
from psycopg.rows import dict_row
from geovisio.utils.fields import Bounds
from geovisio.web.utils import (
    STAC_VERSION,
    cleanNoneInList,
    cleanNoneInDict,
    dbTsToStac,
    get_license_link,
    get_root_link,
    removeNoneInDict,
    user_dependant_response,
)
from geovisio.utils.sequences import (
    get_collections,
    CollectionsRequest,
    SortBy,
    SortByField,
    SQLDirection,
    STAC_FIELD_MAPPINGS,
    get_pagination_links,
)
from geovisio.web.params import (
    parse_filter,
    parse_collections_limit,
)

CONFORMANCE_LIST = [
    "http://www.opengis.net/spec/ogcapi-features-1/1.0/conf/core",
    "http://www.opengis.net/spec/ogcapi-features-1/1.0/conf/geojson",
    "http://www.opengis.net/spec/ogcapi-common-2/1.0/conf/simple-query",
    f"https://api.stacspec.org/v{STAC_VERSION}/core",
    f"https://api.stacspec.org/v{STAC_VERSION}/browseable",
    f"https://api.stacspec.org/v{STAC_VERSION}/collections",
    f"https://api.stacspec.org/v{STAC_VERSION}/ogcapi-features",
    f"https://api.stacspec.org/v{STAC_VERSION}/item-search",
    f"https://api.stacspec.org/v{STAC_VERSION}/collection-search",
]

bp = Blueprint("stac", __name__, url_prefix="/api")


@bp.route("/")
@user_dependant_response(False)
def getLanding():
    """Retrieves API resources list
    ---
    tags:
        - Metadata
    responses:
        200:
            description: the Catalog listing resources available in this API. A non-standard "extent" property is also available (note that this may evolve in the future)
            content:
                application/json:
                    schema:
                        $ref: '#/components/schemas/GeoVisioLanding'
    """

    with psycopg.connect(current_app.config["DB_URL"]) as conn:
        with conn.cursor() as cursor:
            spatial_xmin, spatial_ymin, spatial_xmax, spatial_ymax, temporal_min, temporal_max = cursor.execute(
                """
				SELECT
					GREATEST(-180, ST_XMin(ST_EstimatedExtent('pictures', 'geom'))),
					GREATEST(-90, ST_YMin(ST_EstimatedExtent('pictures', 'geom'))),
					LEAST(180, ST_XMax(ST_EstimatedExtent('pictures', 'geom'))),
					LEAST(90, ST_YMax(ST_EstimatedExtent('pictures', 'geom'))),
					MIN(ts), MAX(ts)
				FROM pictures
			"""
            ).fetchone()

            extent = (
                cleanNoneInDict(
                    {
                        "spatial": (
                            {"bbox": [[spatial_xmin, spatial_ymin, spatial_xmax, spatial_ymax]]} if spatial_xmin is not None else None
                        ),
                        "temporal": (
                            {"interval": [[dbTsToStac(temporal_min), dbTsToStac(temporal_max)]]} if temporal_min is not None else None
                        ),
                    }
                )
                if spatial_xmin is not None or temporal_min is not None
                else None
            )

            sequences = [
                {"rel": "child", "title": f'User "{s[1]}" sequences', "href": url_for("stac.getUserCatalog", userId=s[0], _external=True)}
                for s in cursor.execute(
                    """
					SELECT DISTINCT s.account_id, a.name
					FROM sequences s
					JOIN accounts a ON s.account_id = a.id
				"""
                ).fetchall()
            ]

            catalog = dbSequencesToStacCatalog(
                "geovisio",
                "GeoVisio STAC API",
                "This catalog list all geolocated pictures available in this GeoVisio instance",
                sequences,
                request,
                extent,
            )

            mapUrl = (
                url_for("map.getTile", x="111", y="222", z="333", format="mvt", _external=True)
                .replace("111", "{x}")
                .replace("222", "{y}")
                .replace("333", "{z}")
            )
            userMapUrl = (
                url_for("map.getUserTile", userId="bob", x="111", y="222", z="333", format="mvt", _external=True)
                .replace("111", "{x}")
                .replace("222", "{y}")
                .replace("333", "{z}")
                .replace("bob", "{userId}")
            )

            if "stac_extensions" not in catalog:
                catalog["stac_extensions"] = []

            catalog["stac_extensions"] += ["https://stac-extensions.github.io/web-map-links/v1.0.0/schema.json"]

            catalog["links"] += cleanNoneInList(
                [
                    {"rel": "service-desc", "type": "application/json", "href": url_for("flasgger.swagger", _external=True)},
                    {"rel": "service-doc", "type": "text/html", "href": url_for("flasgger.apidocs", _external=True)},
                    {"rel": "conformance", "type": "application/json", "href": url_for("stac.getConformance", _external=True)},
                    {"rel": "data", "type": "application/json", "href": url_for("stac_collections.getAllCollections", _external=True)},
                    {
                        "rel": "data",
                        "type": "application/rss+xml",
                        "href": url_for("stac_collections.getAllCollections", _external=True, format="rss"),
                    },
                    {"rel": "search", "type": "application/geo+json", "href": url_for("stac_items.searchItems", _external=True)},
                    {
                        "rel": "xyz",
                        "type": "application/vnd.mapbox-vector-tile",
                        "href": mapUrl,
                        "title": "Pictures and sequences vector tiles",
                    },
                    {
                        "rel": "user-xyz",
                        "type": "application/vnd.mapbox-vector-tile",
                        "href": userMapUrl,
                        "title": "Pictures and sequences vector tiles for a given user",
                    },
                    {
                        "rel": "collection-preview",
                        "type": "image/jpeg",
                        "href": url_for("stac_collections.getCollectionThumbnail", collectionId="{id}", _external=True),
                        "title": "Thumbnail URL for a given sequence",
                    },
                    {
                        "rel": "item-preview",
                        "type": "image/jpeg",
                        "href": url_for("pictures.getPictureThumb", pictureId="{id}", format="jpg", _external=True),
                        "title": "Thumbnail URL for a given picture",
                    },
                    {
                        "rel": "users",
                        "type": "application/json",
                        "href": url_for("user.listUsers", _external=True),
                        "title": "List of users",
                    },
                    {
                        "rel": "user-search",
                        "type": "application/json",
                        "href": url_for("user.searchUser", _external=True),
                        "title": "Search users",
                    },
                    get_license_link(),
                ]
            )

            return catalog, 200, {"Content-Type": "application/json"}


@bp.route("/conformance")
@user_dependant_response(False)
def getConformance():
    """List definitions this API conforms to
    ---
    tags:
        - Metadata
    responses:
        200:
            description: the list of definitions this API conforms to
            content:
                application/json:
                    schema:
                        $ref: '#/components/schemas/STACConformance'
    """

    return {"conformsTo": CONFORMANCE_LIST}, 200, {"Content-Type": "application/json"}


def dbSequencesToStacCatalog(id, title, description, sequences, request, extent=None, **selfUrlValues):
    """Transforms a set of sequences into a STAC Catalog

    Parameters
    ----------
    id : str
        The catalog ID
    title : str
        The catalog name
    description : str
        The catalog description
    sequences : list
        List of sequences as STAC child links
    request
    current_app
    extent : dict
        Spatial and temporal extent of the catalog, in STAC format
    selfRoute : str
        API route to access this catalog (defaults to empty, for root catalog)

    Returns
    -------
    object
            The equivalent in STAC Catalog format
    """

    return removeNoneInDict(
        {
            "stac_version": STAC_VERSION,
            "id": id,
            "title": title,
            "description": description,
            "type": "Catalog",
            "conformsTo": CONFORMANCE_LIST,
            "extent": extent,
            "links": [
                {"rel": "self", "type": "application/json", "href": url_for(request.endpoint, _external=True, **selfUrlValues)},
                get_root_link(),
            ]
            + sequences,
        }
    )


def dbSequencesToStacCollection(id, title, description, sequences, request, extent=None, **selfUrlValues):
    """Transforms a set of sequences into a STAC Collection

    Parameters
    ----------
    id : str
        The collection ID
    title : str
        The collection name
    description : str
        The collection description
    sequences : list
        List of sequences as STAC child links
    request
    current_app
    extent : dict
        Spatial and temporal extent of the catalog, in STAC format
    selfRoute : str
        API route to access this collection (defaults to empty, for root catalog)

    Returns
    -------
    object
            The equivalent in STAC Collection format
    """

    return removeNoneInDict(
        {
            "stac_version": STAC_VERSION,
            "id": id,
            "title": title,
            "description": description,
            "type": "Collection",
            "conformsTo": CONFORMANCE_LIST,
            "extent": extent,
            "links": [
                {"rel": "self", "type": "application/json", "href": url_for(request.endpoint, _external=True, **selfUrlValues)},
                get_root_link(),
            ]
            + sequences,
        }
    )


@bp.route("/users/<uuid:userId>/catalog/")
@auth.isUserIdMatchingCurrentAccount()
def getUserCatalog(userId, userIdMatchesAccount=False):
    """Retrieves an user list of sequences (catalog)
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
    responses:
        200:
            description: the Catalog listing all sequences associated to given user
            content:
                application/json:
                    schema:
                        $ref: '#/components/schemas/GeoVisioCatalog'
    """

    collection_request = CollectionsRequest(
        sort_by=SortBy(fields=[SortByField(field=STAC_FIELD_MAPPINGS["created"], direction=SQLDirection.ASC)]),
        user_id=userId,
        userOwnsAllCollections=userIdMatchesAccount,
    )
    collection_request.limit = parse_collections_limit(request.args.get("limit"))
    collection_request.pagination_filter = parse_filter(request.args.get("page"))

    userName = None
    meta_collection = None
    with psycopg.connect(current_app.config["DB_URL"], row_factory=dict_row) as conn, conn.cursor() as cursor:
        userName = cursor.execute("SELECT name FROM accounts WHERE id = %s", [userId]).fetchone()

        if not userName:
            raise errors.InvalidAPIUsage(f"Impossible to find user {userId}")
        userName = userName["name"]

        meta_collection = cursor.execute(
            SQL("SELECT MIN(inserted_at) AS min_order, MAX(inserted_at) AS max_order FROM sequences s WHERE account_id = %(account)s"),
            params={"account": userId},
        ).fetchone()

        if not meta_collection or meta_collection["min_order"] is None:
            # No data found, trying to give the most meaningfull error message
            raise errors.InvalidAPIUsage(f"No data loaded for user {userId}", 404)

    db_collections = get_collections(collection_request)

    links = [
        removeNoneInDict(
            {
                "id": c["id"],
                "title": c["name"],
                "rel": "child",
                "href": url_for("stac_collections.getCollection", _external=True, collectionId=c["id"]),
                "stats:items": {"count": c["nbpic"]},
                "extent": {
                    "temporal": {
                        "interval": [
                            [
                                dbTsToStac(c["mints"]),
                                dbTsToStac(c["maxts"]),
                            ]
                        ]
                    }
                },
                "geovisio:status": c["status"] if userIdMatchesAccount else None,
            }
        )
        for c in db_collections.collections
    ]

    pagination_links = get_pagination_links(
        route="stac.getUserCatalog",
        routeArgs={"userId": str(userId), "limit": collection_request.limit},
        field=collection_request.sort_by.fields[0].field.stac,
        direction=collection_request.sort_by.fields[0].direction,
        datasetBounds=Bounds(min=meta_collection["min_order"], max=meta_collection["max_order"]),
        dataBounds=db_collections.query_first_order_bounds,
        additional_filters=None,
    )

    links.extend(pagination_links)

    return (
        dbSequencesToStacCatalog(
            f"user:{userId}",
            f"{userName}'s sequences",
            f"List of all sequences of user {userName}",
            links,
            request,
            userId=str(userId),
        ),
        200,
        {"Content-Type": "application/json"},
    )
