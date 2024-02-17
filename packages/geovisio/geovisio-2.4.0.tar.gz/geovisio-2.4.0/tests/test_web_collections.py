from pystac import Collection
from dateutil.parser import parse as dateparser
import geovisio.web.collections
from geovisio.workers import runner_pictures
from geovisio.utils.fields import Bounds
from geovisio.utils.sequences import SQLDirection
from tests import conftest
from tests.conftest import STAC_VERSION
import os
from pystac import Collection
from datetime import date, datetime
from uuid import UUID
from geovisio import create_app
from PIL import Image
import pytest
import time
import io
import psycopg


def test_dbSequenceToStacCollection(client):
    dbSeq = {
        "id": UUID("{12345678-1234-5678-1234-567812345678}"),
        "name": "Test sequence",
        "minx": -1.0,
        "maxx": 1.0,
        "miny": -2.0,
        "maxy": 2.0,
        "mints": datetime.fromisoformat("2020-01-01T12:50:37+00:00"),
        "maxts": datetime.fromisoformat("2020-01-01T13:30:42+00:00"),
        "created": datetime.fromisoformat("2023-01-01T12:42:00+02:00"),
        "updated": datetime.fromisoformat("2023-01-01T13:42:00+02:00"),
        "account_name": "Default account",
        "nbpic": 10,
    }

    res = geovisio.web.collections.dbSequenceToStacCollection(dbSeq)

    assert res
    assert res["type"] == "Collection"
    assert res["stac_version"] == STAC_VERSION
    assert res["id"] == "12345678-1234-5678-1234-567812345678"
    assert res["title"] == "Test sequence"
    assert res["description"] == "A sequence of geolocated pictures"
    assert res["providers"] == [
        {"name": "Default account", "roles": ["producer"]},
    ]
    assert res["keywords"] == ["pictures", "Test sequence"]
    assert res["license"] == "etalab-2.0"
    assert res["created"] == "2023-01-01T10:42:00+00:00"
    assert res["updated"] == "2023-01-01T11:42:00+00:00"
    assert res["extent"]["spatial"]["bbox"] == [[-1.0, -2.0, 1.0, 2.0]]
    assert res["extent"]["temporal"]["interval"] == [["2020-01-01T12:50:37+00:00", "2020-01-01T13:30:42+00:00"]]
    assert res["stats:items"]["count"] == 10
    assert len(res["links"]) == 5
    l = next(l for l in res["links"] if l["rel"] == "license")
    assert l["title"] == "License for this object (etalab-2.0)"
    assert l["href"] == "https://raw.githubusercontent.com/DISIC/politique-de-contribution-open-source/master/LICENSE"


def test_dbSequenceToStacCollectionEmptyTemporalInterval(client):
    dbSeq = {
        "id": UUID("{12345678-1234-5678-1234-567812345678}"),
        "name": "Test sequence",
        "minx": -1.0,
        "maxx": 1.0,
        "miny": -2.0,
        "maxy": 2.0,
        "mints": None,
        "created": datetime.fromisoformat("2023-01-01T12:42:00+02:00"),
        "account_name": "Default account",
    }

    res = geovisio.web.collections.dbSequenceToStacCollection(dbSeq)

    assert res
    assert res["type"] == "Collection"
    assert res["stac_version"] == STAC_VERSION
    assert res["id"] == "12345678-1234-5678-1234-567812345678"
    assert res["title"] == "Test sequence"
    assert res["description"] == "A sequence of geolocated pictures"
    assert res["providers"] == [
        {"name": "Default account", "roles": ["producer"]},
    ]
    assert res["keywords"] == ["pictures", "Test sequence"]
    assert res["license"] == "etalab-2.0"
    assert res["created"] == "2023-01-01T10:42:00+00:00"
    assert res["extent"]["spatial"]["bbox"] == [[-1.0, -2.0, 1.0, 2.0]]
    assert res["extent"]["temporal"]["interval"] == [[None, None]]
    assert len(res["links"]) == 5


def test_dbSequenceToStacCollectionEmptyBbox(client):
    dbSeq = {
        "id": UUID("{12345678-1234-5678-1234-567812345678}"),
        "name": "Test sequence",
        "minx": None,
        "maxx": None,
        "miny": None,
        "maxy": None,
        "mints": datetime.fromisoformat("2020-01-01T12:50:37+00:00"),
        "maxts": datetime.fromisoformat("2020-01-01T13:30:42+00:00"),
        "created": datetime.fromisoformat("2023-01-01T12:42:00+02:00"),
        "updated": datetime.fromisoformat("2023-01-01T12:42:00+02:00"),
        "account_name": "Default account",
    }

    res = geovisio.web.collections.dbSequenceToStacCollection(dbSeq)

    assert res
    assert res["type"] == "Collection"
    assert res["stac_version"] == STAC_VERSION
    assert res["id"] == "12345678-1234-5678-1234-567812345678"
    assert res["title"] == "Test sequence"
    assert res["description"] == "A sequence of geolocated pictures"
    assert res["providers"] == [
        {"name": "Default account", "roles": ["producer"]},
    ]
    assert res["keywords"] == ["pictures", "Test sequence"]
    assert res["license"] == "etalab-2.0"
    assert res["created"] == "2023-01-01T10:42:00+00:00"
    assert res["extent"]["spatial"]["bbox"] == [[-180.0, -90.0, 180.0, 90.0]]

    l = next(l for l in res["links"] if l["rel"] == "license")
    assert l["title"] == "License for this object (etalab-2.0)"
    assert l["href"] == "https://raw.githubusercontent.com/DISIC/politique-de-contribution-open-source/master/LICENSE"


def test_dbSequenceToStacCollectionNoLicense(no_license_app_client):
    dbSeq = {
        "id": UUID("{12345678-1234-5678-1234-567812345678}"),
        "name": "Test sequence",
        "minx": -1.0,
        "maxx": 1.0,
        "miny": -2.0,
        "maxy": 2.0,
        "mints": datetime.fromisoformat("2020-01-01T12:50:37+00:00"),
        "maxts": datetime.fromisoformat("2020-01-01T13:30:42+00:00"),
        "created": datetime.fromisoformat("2023-01-01T12:42:00+02:00"),
        "updated": datetime.fromisoformat("2023-01-01T13:42:00+02:00"),
        "account_name": "Default account",
    }

    res = geovisio.web.collections.dbSequenceToStacCollection(dbSeq)

    assert res
    assert res["type"] == "Collection"
    assert res["stac_version"] == STAC_VERSION
    assert res["id"] == "12345678-1234-5678-1234-567812345678"
    assert res["title"] == "Test sequence"
    assert res["description"] == "A sequence of geolocated pictures"
    assert res["providers"] == [
        {"name": "Default account", "roles": ["producer"]},
    ]
    assert res["keywords"] == ["pictures", "Test sequence"]
    assert res["license"] == "proprietary"
    assert res["created"] == "2023-01-01T10:42:00+00:00"
    assert res["updated"] == "2023-01-01T11:42:00+00:00"
    assert res["extent"]["spatial"]["bbox"] == [[-1.0, -2.0, 1.0, 2.0]]
    assert res["extent"]["temporal"]["interval"] == [["2020-01-01T12:50:37+00:00", "2020-01-01T13:30:42+00:00"]]
    assert len(res["links"]) == 4
    rels = [l for l in res["links"] if l["rel"] == "license"]
    assert not rels


def test_collectionsEmpty(client):
    response = client.get("/api/collections")

    assert response.status_code == 200
    assert len(response.json["collections"]) == 0
    assert set((l["rel"] for l in response.json["links"])) == {"root", "parent", "self"}


@conftest.SEQ_IMGS
def test_collections(datafiles, initSequence):
    client = initSequence(datafiles, preprocess=False)

    response = client.get("/api/collections")
    data = response.json

    assert response.status_code == 200

    assert len(data["collections"]) == 1
    assert data["links"] == [
        {"href": "http://localhost/api/", "rel": "root", "title": "Instance catalog", "type": "application/json"},
        {"href": "http://localhost/api/", "rel": "parent", "type": "application/json"},
        {"href": "http://localhost/api/collections", "rel": "self", "type": "application/json"},
    ]

    Collection.from_dict(data["collections"][0])

    assert data["collections"][0]["type"] == "Collection"
    assert data["collections"][0]["stac_version"] == STAC_VERSION
    assert len(data["collections"][0]["id"]) > 0
    assert len(data["collections"][0]["title"]) > 0
    assert data["collections"][0]["description"] == "A sequence of geolocated pictures"
    assert len(data["collections"][0]["keywords"]) > 0
    assert len(data["collections"][0]["license"]) > 0
    assert len(data["collections"][0]["extent"]["spatial"]["bbox"][0]) == 4
    assert len(data["collections"][0]["extent"]["temporal"]["interval"][0]) == 2
    assert len(data["collections"][0]["links"]) == 4
    assert data["collections"][0]["created"].startswith(date.today().isoformat())
    assert data["collections"][0]["stats:items"]["count"] == 5


@conftest.SEQ_IMGS
def test_collections_rss(datafiles, initSequence):
    client = initSequence(datafiles, preprocess=False)

    # With query string
    response = client.get("/api/collections", query_string={"format": "rss"})
    assert response.status_code == 200
    assert response.data.startswith(b"""<?xml version="1.0" encoding="UTF-8"?>\n<rss version="2.0" """)

    # With Accept header
    response = client.get("/api/collections", headers={"Accept": "application/rss+xml"})
    assert response.status_code == 200
    assert response.data.startswith(b"""<?xml version="1.0" encoding="UTF-8"?>\n<rss version="2.0" """)


@conftest.SEQ_IMGS
def test_collections_rss_pages(datafiles, dburl, tmp_path, fsesUrl):
    app = create_app(
        {
            "TESTING": True,
            "DB_URL": dburl,
            "FS_URL": None,
            "FS_TMP_URL": fsesUrl.tmp,
            "FS_PERMANENT_URL": fsesUrl.permanent,
            "FS_DERIVATES_URL": fsesUrl.derivates,
            "SERVER_NAME": "localhost:5000",
            "PICTURE_PROCESS_DERIVATES_STRATEGY": "ON_DEMAND",
            "SECRET_KEY": "a very secret key",
            "API_MAIN_PAGE": "https://panoramax.osm.fr/",
            "API_VIEWER_PAGE": "https://panoramax.osm.fr/a-cool-viewer/",
        }
    )
    with app.app_context(), app.test_client() as client:
        conftest.uploadSequence(client, datafiles, wait=True)
        response = client.get("/api/collections", query_string={"format": "rss"})
        assert response.status_code == 200
        d = response.data
        assert d.startswith(b"""<?xml version="1.0" encoding="UTF-8"?>\n<rss version="2.0" """)
        assert b"""href="https://panoramax.osm.fr/a-cool-viewer/#focus""" in d
        assert b"<link>https://panoramax.osm.fr/</link>" in d


@conftest.SEQ_IMGS
def test_collections_pagination_outalimit(datafiles, initSequence):
    client = initSequence(datafiles, preprocess=False)

    response = client.get("/api/collections?limit=50&created_after=2100-01-01T10:00:00Z")
    assert response.status_code == 400
    assert response.json == {"message": "There is no collection created after 2100-01-01 10:00:00+00:00", "status_code": 400}

    response = client.get("/api/collections?limit=50&created_before=2000-01-01T10:00:00Z")
    assert response.status_code == 400
    assert response.json == {"message": "There is no collection created before 2000-01-01 10:00:00+00:00", "status_code": 400}

    response = client.get("/api/collections?limit=-1")
    assert response.status_code == 400
    assert response.json == {"message": "limit parameter should be an integer between 1 and 1000", "status_code": 400}

    response = client.get("/api/collections?limit=1001")
    assert response.status_code == 400
    assert response.json == {"message": "limit parameter should be an integer between 1 and 1000", "status_code": 400}


@conftest.SEQ_IMGS
def test_collections_invalid_created_after(datafiles, initSequence):
    client = initSequence(datafiles, preprocess=False)

    response = client.get("/api/collections?limit=50&created_after=pouet")
    assert response.status_code == 400
    assert response.json == {
        "details": {"error": "Unknown string format: pouet"},
        "message": "Invalid `created_after` argument",
        "status_code": 400,
    }


@conftest.SEQ_IMGS
def test_collections_hidden(datafiles, initSequence, dburl):
    client = initSequence(datafiles, preprocess=False)

    seqId, picId = conftest.getFirstPictureIds(dburl)

    with psycopg.connect(dburl) as conn:
        with conn.cursor() as cursor:
            cursor.execute("UPDATE sequences SET status = 'hidden'")
            conn.commit()

    response = client.get("/api/collections")
    assert response.status_code == 200
    assert len(response.json["collections"]) == 0


@conftest.SEQ_IMGS
def test_collections_bbox(datafiles, initSequence):
    client = initSequence(datafiles, preprocess=False)

    response = client.get("/api/collections?bbox=0,0,1,1")
    print(response.text)
    assert response.status_code == 200
    assert len(response.json["collections"]) == 0

    response = client.get("/api/collections?bbox=1.312864,48.004817,3.370054,49.357521")
    assert response.status_code == 200
    assert len(response.json["collections"]) == 1


@conftest.SEQ_IMGS
def test_collections_datetime(datafiles, initSequence):
    client = initSequence(datafiles, preprocess=False)

    response = client.get("/api/collections?datetime=../2021-01-01")
    print(response.text)
    assert response.status_code == 200
    assert len(response.json["collections"]) == 0

    response = client.get("/api/collections?datetime=2021-01-01/..")
    assert response.status_code == 200
    assert len(response.json["collections"]) == 1

    # Note that sequences are filtered by day, not time
    #   due to computed_capture_date field in sequences table
    response = client.get("/api/collections?datetime=2021-07-29T09:00:00Z/2021-07-29T10:00:00Z")
    assert response.status_code == 200
    assert len(response.json["collections"]) == 1


@conftest.SEQ_IMGS
def test_collections_filter(datafiles, initSequence):
    client = initSequence(datafiles, preprocess=False)

    response = client.get("/api/collections?filter=updated >= '2030-12-31'")
    assert response.status_code == 200
    assert len(response.json["collections"]) == 0

    response = client.get("/api/collections?filter=updated >= '2018-01-01'")
    assert response.status_code == 200
    assert len(response.json["collections"]) == 1

    response = client.get("/api/collections?filter=updated BETWEEN '2018-01-01' AND '2030-12-31'")
    assert response.status_code == 200
    assert len(response.json["collections"]) == 1

    response = client.get("/api/collections?filter=created >= '2023-01-01'")
    assert response.status_code == 200
    assert len(response.json["collections"]) == 1

    response = client.get("/api/collections?filter=created <= '2023-01-01' AND updated >= '2018-01-01'")
    assert response.status_code == 200
    assert len(response.json["collections"]) == 0

    response = client.get("/api/collections?filter=status == 'private'")  # Invalid operator
    assert response.status_code == 400

    response = client.get("/api/collections?filter=bad_field = 'private'")  # Not allowed field
    assert response.status_code == 400


def test_collectionMissing(client):
    response = client.get("/api/collections/00000000-0000-0000-0000-000000000000")
    assert response.status_code == 404


@conftest.SEQ_IMGS
def test_collectionById(datafiles, initSequence, dburl):
    client = initSequence(datafiles, preprocess=False)

    seqId, picId = conftest.getFirstPictureIds(dburl)

    response = client.get("/api/collections/" + str(seqId))
    data = response.json

    assert response.status_code == 200
    clc = Collection.from_dict(data)
    assert clc.extra_fields["stats:items"]["count"] == 5


@conftest.SEQ_IMGS
def test_get_hidden_sequence(datafiles, initSequenceApp, dburl, bobAccountToken):
    client, app = initSequenceApp(datafiles, withBob=True)
    sequence = conftest.getPictureIds(dburl)[0]
    assert len(sequence.pictures) == 5

    # hide sequence
    response = client.patch(
        f"/api/collections/{sequence.id}", data={"visible": "false"}, headers={"Authorization": f"Bearer {bobAccountToken(app)}"}
    )
    assert response.status_code == 200
    assert response.json["geovisio:status"] == "hidden"

    # status should be set to hidden in db
    with psycopg.connect(dburl) as conn, conn.cursor() as cursor:
        seqStatus = cursor.execute("SELECT status FROM sequences WHERE id = %s", [sequence.id]).fetchone()
        assert seqStatus
        assert seqStatus[0] == "hidden"

    # The sequence is hidden, public call cannot see it, only Bob
    r = client.get(f"/api/collections/{sequence.id}")
    assert r.status_code == 404
    r = client.get(f"/api/collections/{sequence.id}/items")
    assert r.status_code == 404

    # same for the list of items in the collection
    r = client.get(f"/api/collections/{sequence.id}", headers={"Authorization": f"Bearer {bobAccountToken(app)}"})
    assert r.status_code == 200
    r = client.get(f"/api/collections/{sequence.id}/items", headers={"Authorization": f"Bearer {bobAccountToken(app)}"})
    assert r.status_code == 200
    assert len(r.json["features"]) == 5

    for p in sequence.pictures:
        r = client.get(f"/api/collections/{sequence.id}/items/{p.id}")
        assert r.status_code == 404

        r = client.get(f"/api/collections/{sequence.id}/items/{p.id}", headers={"Authorization": f"Bearer {bobAccountToken(app)}"})
        assert r.status_code == 200

    # other sequence's routes are also unavailable for public access
    r = client.get(f"/api/collections/{sequence.id}/geovisio_status")
    assert r.status_code == 404
    r = client.get(f"/api/collections/{sequence.id}/geovisio_status", headers={"Authorization": f"Bearer {bobAccountToken(app)}"})
    assert r.status_code == 200

    # if we set the sequence back to public, it should be fine for everybody
    response = client.patch(
        f"/api/collections/{sequence.id}", data={"visible": "true"}, headers={"Authorization": f"Bearer {bobAccountToken(app)}"}
    )
    assert response.status_code == 200

    assert client.get(f"/api/collections/{sequence.id}").status_code == 200
    for p in sequence.pictures:
        assert client.get(f"/api/collections/{sequence.id}/items/{p.id}").status_code == 200


@conftest.SEQ_IMGS
def test_get_hidden_sequence_and_pictures(datafiles, initSequenceApp, dburl, bobAccountToken):
    """
    If we:
            * hide the pictures n°1
            * hide the sequence
            * un-hide the sequence

    The pictures n°1 should stay hidden
    """
    client, app = initSequenceApp(datafiles, withBob=True)
    sequence = conftest.getPictureIds(dburl)[0]
    assert len(sequence.pictures) == 5

    # hide pic
    response = client.patch(
        f"/api/collections/{sequence.id}/items/{sequence.pictures[0].id}",
        data={"visible": "false"},
        headers={"Authorization": f"Bearer {bobAccountToken(app)}"},
    )

    r = client.get(f"/api/collections/{sequence.id}/items/{sequence.pictures[0].id}")
    assert r.status_code == 404

    # hide sequence
    response = client.patch(
        f"/api/collections/{sequence.id}", data={"visible": "false"}, headers={"Authorization": f"Bearer {bobAccountToken(app)}"}
    )
    assert response.status_code == 200

    r = client.get(f"/api/collections/{sequence.id}")
    assert r.status_code == 404

    # set the sequence to visible
    response = client.patch(
        f"/api/collections/{sequence.id}", data={"visible": "true"}, headers={"Authorization": f"Bearer {bobAccountToken(app)}"}
    )
    assert response.status_code == 200
    r = client.get(f"/api/collections/{sequence.id}")
    assert r.status_code == 200

    # but the pic is still hidden
    r = client.get(f"/api/collections/{sequence.id}/items/{sequence.pictures[0].id}")
    assert r.status_code == 404


@conftest.SEQ_IMGS
def test_invalid_sequence_hide(datafiles, initSequenceApp, dburl, bobAccountToken):
    client, app = initSequenceApp(datafiles, withBob=True)
    sequence = conftest.getPictureIds(dburl)[0]

    # hide pic
    response = client.patch(
        f"/api/collections/{sequence.id}", data={"visible": "invalid_value"}, headers={"Authorization": f"Bearer {bobAccountToken(app)}"}
    )
    assert response.status_code == 400


@conftest.SEQ_IMGS
def test_hide_unexisting_seq(datafiles, initSequenceApp, dburl, bobAccountToken):
    client, app = initSequenceApp(datafiles, withBob=True)

    response = client.patch(
        "/api/collections/00000000-0000-0000-0000-000000000000",
        data={"visible": "false"},
        headers={"Authorization": f"Bearer {bobAccountToken(app)}"},
    )
    assert response.status_code == 404
    assert response.json == {"message": "Sequence 00000000-0000-0000-0000-000000000000 wasn't found in database", "status_code": 404}


@conftest.SEQ_IMGS
def test_empty_sequence_patch(datafiles, initSequenceApp, dburl, bobAccountToken):
    client, app = initSequenceApp(datafiles, withBob=True)
    sequence = conftest.getPictureIds(dburl)[0]

    response = client.patch(
        f"/api/collections/{sequence.id}/items/{sequence.pictures[0].id}", headers={"Authorization": f"Bearer {bobAccountToken(app)}"}
    )
    # changing no value is valid, and should result if the same thing as a get
    assert response.status_code == 200


@conftest.SEQ_IMGS
def test_anomynous_sequence_patch(datafiles, initSequenceApp, dburl):
    """Patching a sequence as an unauthentified user should result in an error"""
    client, app = initSequenceApp(datafiles, withBob=True)
    sequence = conftest.getPictureIds(dburl)[0]

    response = client.patch(
        f"/api/collections/{sequence.id}",
    )
    assert response.status_code == 401
    assert response.json == {"message": "Authentication is mandatory"}


@conftest.SEQ_IMGS
def test_set_already_visible_sequence(datafiles, initSequenceApp, dburl, bobAccountToken):
    """Setting an already visible sequence to visible is valid, and change nothing"""
    client, app = initSequenceApp(datafiles, withBob=True)
    sequence = conftest.getPictureIds(dburl)[0]

    # hide sequence
    p = client.patch(
        f"/api/collections/{sequence.id}", data={"visible": "true"}, headers={"Authorization": f"Bearer {bobAccountToken(app)}"}
    )
    assert p.status_code == 200
    r = client.get(f"/api/collections/{sequence.id}")
    assert r.status_code == 200


@conftest.SEQ_IMGS
def test_not_owned_sequence_patch(datafiles, initSequenceApp, dburl, defaultAccountToken):
    """Patching a sequence that does not belong to us should result in an error"""
    client, app = initSequenceApp(datafiles, withBob=True)  # the sequence belongs to Bob
    sequence = conftest.getPictureIds(dburl)[0]

    response = client.patch(
        f"/api/collections/{sequence.id}", data={"visible": "true"}, headers={"Authorization": f"Bearer {defaultAccountToken(app)}"}
    )
    assert response.status_code == 403


@conftest.SEQ_IMGS
def test_patch_sequence_title(datafiles, initSequenceApp, dburl, bobAccountToken):
    client, app = initSequenceApp(datafiles, withBob=True)
    sequence = conftest.getPictureIds(dburl)[0]

    with psycopg.connect(dburl) as conn, conn.cursor() as cursor:
        # Add custom metadata in sequence
        cursor.execute('UPDATE sequences SET metadata = \'{"bla": "bloub"}\'::jsonb WHERE id = %s', [sequence.id])
        conn.commit()

        # Change sequence title
        newTitle = "Un tout nouveau titre STYLÉÉÉ"
        response = client.patch(
            f"/api/collections/{sequence.id}", data={"title": newTitle}, headers={"Authorization": f"Bearer {bobAccountToken(app)}"}
        )
        assert response.status_code == 200
        assert response.json["title"] == newTitle

        # Check title in DB
        seqMeta = cursor.execute("SELECT metadata FROM sequences WHERE id = %s", [sequence.id]).fetchone()[0]
        assert seqMeta["title"] == newTitle
        assert seqMeta["bla"] == "bloub"  # Check it didn't erase other metadata

        # Check title in classic GET response
        r = client.get(f"/api/collections/{sequence.id}")
        assert r.status_code == 200
        assert r.json.get("title") == newTitle


@conftest.SEQ_IMGS
def test_patch_sequence_title_status(datafiles, initSequenceApp, dburl, bobAccountToken):
    client, app = initSequenceApp(datafiles, withBob=True)
    sequence = conftest.getPictureIds(dburl)[0]

    # Change sequence title
    newTitle = "Un tout nouveau titre STYLÉÉÉ"
    response = client.patch(
        f"/api/collections/{sequence.id}",
        data={"visible": "false", "title": newTitle},
        headers={"Authorization": f"Bearer {bobAccountToken(app)}"},
    )
    assert response.status_code == 200
    assert response.json["title"] == newTitle
    assert response.json["geovisio:status"] == "hidden"

    # Check title in DB
    with psycopg.connect(dburl) as conn, conn.cursor() as cursor:
        seqMeta, seqStatus = cursor.execute("SELECT metadata, status FROM sequences WHERE id = %s", [sequence.id]).fetchone()
        assert seqMeta["title"] == newTitle
        assert seqStatus == "hidden"

    # Check title in classic GET response
    r = client.get(f"/api/collections/{sequence.id}", headers={"Authorization": f"Bearer {bobAccountToken(app)}"})
    assert r.status_code == 200
    assert r.json.get("title") == newTitle
    assert r.json.get("geovisio:status") == "hidden"


def test_post_collection_body_form(client):
    response = client.post("/api/collections", data={"title": "Séquence"})

    assert response.status_code == 200
    assert response.headers.get("Location").startswith("http://localhost:5000/api/collections/")
    seqId = UUID(response.headers.get("Location").split("/").pop())
    assert seqId != ""

    # Check if JSON is a valid STAC collection
    assert response.json["type"] == "Collection"
    assert response.json["id"] == str(seqId)
    assert response.json["title"] == "Séquence"


def test_post_collection_body_json(client):
    response = client.post("/api/collections", json={"title": "Séquence"})

    assert response.status_code == 200
    assert response.headers.get("Location").startswith("http://localhost:5000/api/collections/")
    seqId = UUID(response.headers.get("Location").split("/").pop())
    assert seqId != ""

    # Check if JSON is a valid STAC collection
    assert response.json["type"] == "Collection"
    assert response.json["id"] == str(seqId)
    assert response.json["title"] == "Séquence"


def test_post_collection_body_json_charset(client):
    response = client.post("/api/collections", headers={"Content-Type": "application/json;charset=uft8"}, json={"title": "Séquence"})

    assert response.status_code == 200
    assert response.headers.get("Location").startswith("http://localhost:5000/api/collections/")
    seqId = UUID(response.headers.get("Location").split("/").pop())
    assert seqId != ""

    # Check if JSON is a valid STAC collection
    assert response.json["type"] == "Collection"
    assert response.json["id"] == str(seqId)
    assert response.json["title"] == "Séquence"


def test_getCollectionImportStatus_noseq(client):
    response = client.get("/api/collections/00000000-0000-0000-0000-000000000000/geovisio_status")
    assert response.status_code == 404


def test_getCollectionImportStatus_empty_collection(client):
    response = client.post("/api/collections", json={"title": "Séquence"})

    assert response.status_code == 200
    assert response.headers.get("Location").startswith("http://localhost:5000/api/collections/")
    seqId = UUID(response.headers.get("Location").split("/").pop())
    assert seqId != ""
    status = client.get(f"/api/collections/{seqId}/geovisio_status")

    assert status.status_code == 200
    # the empty item in the response is not pretty, but a bother to remove
    assert status.json == {"items": [{}], "status": "waiting-for-process"}


@conftest.SEQ_IMGS_FLAT
def test_getCollectionImportStatus_ready(datafiles, initSequence, dburl):
    client = initSequence(datafiles, preprocess=False)
    seqId, picId = conftest.getFirstPictureIds(dburl)

    response = client.get(f"/api/collections/{seqId}/geovisio_status")

    assert response.status_code == 200
    assert len(response.json["items"]) == 2

    for i in response.json["items"]:
        assert len(i) == 6
        assert UUID(i["id"]) is not None
        assert i["rank"] > 0
        assert i["status"] == "ready"
        assert i["processed_at"].startswith(date.today().isoformat())
        assert i["nb_errors"] == 0
        assert i["processing_in_progress"] is False


@conftest.SEQ_IMGS_FLAT
def test_getCollectionImportStatus_hidden(datafiles, initSequence, dburl):
    client = initSequence(datafiles, preprocess=False)
    seqId, picId = conftest.getFirstPictureIds(dburl)

    with psycopg.connect(dburl) as conn:
        with conn.cursor() as cursor:
            cursor.execute("UPDATE pictures SET status = 'hidden' WHERE id = %s", [picId])
            conn.commit()

            response = client.get(f"/api/collections/{seqId}/geovisio_status")

            assert response.status_code == 200
            assert len(response.json["items"]) == 1
            assert response.json["items"][0]["id"] != picId
            assert response.json["items"][0]["status"] == "ready"


@conftest.SEQ_IMGS_FLAT
def test_upload_sequence(datafiles, client, dburl):
    # Create sequence
    resPostSeq = client.post("/api/collections")
    assert resPostSeq.status_code == 200
    seqId = resPostSeq.json["id"]
    seqLocation = resPostSeq.headers["Location"]

    # add the cameras into the db to be able to have field_of_view
    with psycopg.connect(dburl) as conn:
        with conn.cursor() as cursor:
            cursor.execute("INSERT INTO cameras VALUES ('OLYMPUS IMAGING CORP. SP-720UZ', 6.16) ON CONFLICT DO NOTHING")
            conn.commit()
    # Create first image
    resPostImg1 = client.post(
        f"/api/collections/{seqId}/items",
        headers={"Content-Type": "multipart/form-data"},
        data={"position": 1, "picture": (datafiles / "b1.jpg").open("rb")},
    )

    assert resPostImg1.status_code == 202

    # Create second image
    resPostImg2 = client.post(
        f"/api/collections/{seqId}/items",
        headers={"Content-Type": "multipart/form-data"},
        data={"position": 2, "picture": (datafiles / "b2.jpg").open("rb")},
    )

    assert resPostImg2.status_code == 202

    # Check upload status
    conftest.waitForSequence(client, seqLocation)

    with psycopg.connect(dburl) as conn:
        with conn.cursor() as cursor:
            dbSeq = cursor.execute("SELECT status, geom FROM sequences where id = %s", [seqId]).fetchone()
            assert dbSeq
            # Check sequence is ready
            assert dbSeq[0] == "ready"
            # the sequence geometry should have been computed too
            assert dbSeq[1] is not None

    resGetSeq = client.get(f"/api/collections/{seqId}")
    assert resGetSeq.status_code == 200

    # the sequence should have some metadata computed
    seq = resGetSeq.json

    assert seq["extent"]["spatial"] == {"bbox": [[-1.9499731060073981, 48.13939279199841, -1.9491245819090675, 48.139852239480945]]}
    assert seq["extent"]["temporal"]["interval"] == [["2015-04-25T15:36:17+00:00", "2015-04-25T15:37:48+00:00"]]

    # 2 pictures should be in the collections
    r = client.get(f"/api/collections/{seqId}/items")
    assert r.status_code == 200

    assert len(r.json["features"]) == 2
    # both pictures should be ready
    assert r.json["features"][0]["properties"]["geovisio:status"] == "ready"
    assert r.json["features"][1]["properties"]["geovisio:status"] == "ready"

    # the pictures should have the original filename and size as metadata
    with psycopg.connect(dburl) as conn:
        with conn.cursor() as cursor:
            blurred = cursor.execute("SELECT id, metadata FROM pictures").fetchall()
            assert blurred and len(blurred) == 2
            blurred = {str(p[0]): p[1] for p in blurred}
            assert os.path.getsize(datafiles / "b1.jpg") == blurred[resPostImg1.json["id"]]["originalFileSize"]
            assert blurred[resPostImg1.json["id"]] == {
                "make": "OLYMPUS IMAGING CORP.",
                "type": "flat",
                "model": "SP-720UZ",
                "width": 4288,
                "height": 3216,
                "focal_length": 4.66,
                "field_of_view": 67,
                "blurredByAuthor": False,
                "originalFileName": "b1.jpg",
                "originalFileSize": 2731046,
                "crop": None,
                "altitude": None,
            }
            assert os.path.getsize(datafiles / "b2.jpg") == blurred[resPostImg2.json["id"]]["originalFileSize"]
            assert blurred[resPostImg2.json["id"]] == {
                "make": "OLYMPUS IMAGING CORP.",
                "type": "flat",
                "model": "SP-720UZ",
                "width": 4288,
                "height": 3216,
                "focal_length": 4.66,
                "field_of_view": 67,
                "blurredByAuthor": False,
                "originalFileName": "b2.jpg",
                "originalFileSize": 2896575,
                "crop": None,
                "altitude": None,
            }


@pytest.fixture()
def removeDefaultAccount(dburl):
    with psycopg.connect(dburl) as conn:
        with conn.cursor() as cursor:
            accountID = cursor.execute("UPDATE accounts SET is_default = false WHERE is_default = true RETURNING id").fetchone()
            assert accountID

            conn.commit()
            yield
            # put back the account at the end of the test
            cursor.execute("UPDATE accounts SET is_default = true WHERE id = %s", [accountID[0]])


def test_upload_sequence_noDefaultAccount(client, dburl, removeDefaultAccount):
    resPostSeq = client.post("/api/collections")
    assert resPostSeq.status_code == 500
    assert resPostSeq.json == {"message": "No default account defined, please contact your instance administrator", "status_code": 500}


@conftest.SEQ_IMGS
def test_get_collection_thumbnail(datafiles, initSequenceApp, dburl):
    client, _ = initSequenceApp(datafiles)
    seqId, picId = conftest.getFirstPictureIds(dburl)

    response = client.get(f"/api/collections/{str(seqId)}/thumb.jpg")
    assert response.status_code == 200
    assert response.content_type == "image/jpeg"
    img = Image.open(io.BytesIO(response.get_data()))
    assert img.size == (500, 300)

    first_pic_thumb = client.get(f"/api/pictures/{str(picId)}/thumb.jpg")
    assert first_pic_thumb.data == response.data


@conftest.SEQ_IMGS
def test_get_collection_thumbnail_first_pic_hidden(datafiles, initSequenceApp, dburl, bobAccountToken, defaultAccountToken):
    """ "
    If the first pic is hidden, the owner of the sequence should still be able to see it as the thumbnail,
    but all other users should see another pic as the thumbnail
    """
    client, app = initSequenceApp(datafiles, preprocess=False, withBob=True)
    sequence = conftest.getPictureIds(dburl)[0]

    # change the first pic visibility
    response = client.patch(
        f"/api/collections/{sequence.id}/items/{sequence.pictures[0].id}",
        data={"visible": "false"},
        headers={"Authorization": f"Bearer {bobAccountToken(app)}"},
    )
    assert response.status_code == 200

    response = client.get(f"/api/collections/{sequence.id}/thumb.jpg")
    assert response.status_code == 200
    assert response.content_type == "image/jpeg"
    img = Image.open(io.BytesIO(response.get_data()))
    assert img.size == (500, 300)

    # non logged users should not see the same picture
    first_pic_thumb = client.get(f"/api/pictures/{sequence.pictures[0].id}/thumb.jpg")
    assert first_pic_thumb.status_code == 403  # this picture should not be visible to the other users

    second_pic_thumb = client.get(f"/api/pictures/{str(sequence.pictures[1].id)}/thumb.jpg")
    assert second_pic_thumb.status_code == 200  # the second picture is not hidden and should be visible and be the thumbnail
    assert response.data == second_pic_thumb.data

    # same thing for a logged user that is not the owner
    first_pic_thumb = client.get(
        f"/api/pictures/{sequence.pictures[0].id}/thumb.jpg", headers={"Authorization": f"Bearer {defaultAccountToken(app)}"}
    )
    assert first_pic_thumb.status_code == 403

    second_pic_thumb = client.get(
        f"/api/pictures/{str(sequence.pictures[1].id)}/thumb.jpg", headers={"Authorization": f"Bearer {defaultAccountToken(app)}"}
    )
    assert second_pic_thumb.status_code == 200
    assert response.data == second_pic_thumb.data

    owner_thumbnail = client.get(f"/api/collections/{sequence.id}/thumb.jpg", headers={"Authorization": f"Bearer {bobAccountToken(app)}"})
    assert owner_thumbnail.status_code == 200
    assert owner_thumbnail.content_type == "image/jpeg"
    owner_first_pic_thumbnail = client.get(
        f"/api/pictures/{sequence.pictures[0].id}/thumb.jpg", headers={"Authorization": f"Bearer {bobAccountToken(app)}"}
    )
    assert owner_first_pic_thumbnail.status_code == 200
    assert owner_thumbnail.data == owner_first_pic_thumbnail.data  # the owner should see the first pic


@conftest.SEQ_IMGS
def test_get_collection_thumbnail_all_pics_hidden(datafiles, initSequenceApp, dburl, bobAccountToken, defaultAccountToken):
    """ "
    If the all pics are hidden, the owner of the sequence should still be able to see a the thumbnail,
    but all other users should not have any thumbnails
    """
    client, app = initSequenceApp(datafiles, preprocess=False, withBob=True)
    sequence = conftest.getPictureIds(dburl)[0]

    # change the first pic visibility
    for p in sequence.pictures:
        response = client.patch(
            f"/api/collections/{sequence.id}/items/{str(p.id)}",
            data={"visible": "false"},
            headers={"Authorization": f"Bearer {bobAccountToken(app)}"},
        )
        assert response.status_code == 200

    # non logged users should not see a thumbnail
    response = client.get(f"/api/collections/{sequence.id}/thumb.jpg")
    assert response.status_code == 404

    for p in sequence.pictures:
        # the pictures should not be visible to the any other users, logged or not
        # specific hidden pictures will result on 403, not 404
        first_pic_thumb = client.get(f"/api/pictures/{str(p.id)}/thumb.jpg")
        assert first_pic_thumb.status_code == 403
        first_pic_thumb = client.get(
            f"/api/pictures/{sequence.pictures[0].id}/thumb.jpg", headers={"Authorization": f"Bearer {defaultAccountToken(app)}"}
        )
        assert first_pic_thumb.status_code == 403

    # but the owner should see it
    owner_thumbnail = client.get(f"/api/collections/{sequence.id}/thumb.jpg", headers={"Authorization": f"Bearer {bobAccountToken(app)}"})
    assert owner_thumbnail.status_code == 200
    assert owner_thumbnail.content_type == "image/jpeg"
    owner_first_pic_thumbnail = client.get(
        f"/api/pictures/{sequence.pictures[0].id}/thumb.jpg", headers={"Authorization": f"Bearer {bobAccountToken(app)}"}
    )
    assert owner_first_pic_thumbnail.status_code == 200
    assert owner_thumbnail.data == owner_first_pic_thumbnail.data  # the owner should see the first pic


@conftest.SEQ_IMGS
def test_get_collection_thumbnail_sequence_hidden(datafiles, initSequenceApp, dburl, bobAccountToken, defaultAccountToken):
    """ "
    If the sequence is hidden, the owner of the sequence should still be able to see a the thumbnail,
    but all other users should not have any thumbnails
    """
    client, app = initSequenceApp(datafiles, preprocess=False, withBob=True)
    sequence = conftest.getPictureIds(dburl)[0]

    # change the sequence visibility
    response = client.patch(
        f"/api/collections/{sequence.id}", data={"visible": "false"}, headers={"Authorization": f"Bearer {bobAccountToken(app)}"}
    )
    assert response.status_code == 200

    # non logged users should not see a thumbnail
    response = client.get(f"/api/collections/{sequence.id}/thumb.jpg")
    assert response.status_code == 404

    for p in sequence.pictures:
        # the pictures should not be visible to the any other users, logged or not
        # specific hidden pictures will result on 403, not 404
        first_pic_thumb = client.get(f"/api/pictures/{str(p.id)}/thumb.jpg")
        assert first_pic_thumb.status_code == 403
        first_pic_thumb = client.get(
            f"/api/pictures/{sequence.pictures[0].id}/thumb.jpg", headers={"Authorization": f"Bearer {defaultAccountToken(app)}"}
        )
        assert first_pic_thumb.status_code == 403

    # but the owner should see it
    owner_thumbnail = client.get(f"/api/collections/{sequence.id}/thumb.jpg", headers={"Authorization": f"Bearer {bobAccountToken(app)}"})
    assert owner_thumbnail.status_code == 200
    assert owner_thumbnail.content_type == "image/jpeg"
    owner_first_pic_thumbnail = client.get(
        f"/api/pictures/{sequence.pictures[0].id}/thumb.jpg", headers={"Authorization": f"Bearer {bobAccountToken(app)}"}
    )
    assert owner_first_pic_thumbnail.status_code == 200
    assert owner_thumbnail.data == owner_first_pic_thumbnail.data  # the owner should see the first pic


def _wait_for_pics_deletion(pics_id, dburl):
    with psycopg.connect(dburl) as conn:
        waiting_time = 0.1
        total_time = 0
        nb_pics = 0
        while total_time < 10:
            nb_pics = conn.execute("SELECT count(*) FROM pictures WHERE id = ANY(%(pics)s)", {"pics": pics_id}).fetchone()

            # we wait for the collection and all its pictures to be ready
            if nb_pics and not nb_pics[0]:
                return
            time.sleep(waiting_time)
            total_time += waiting_time
        assert False, f"All pictures not deleted ({nb_pics} remaining)"


@conftest.SEQ_IMGS
def test_delete_sequence(datafiles, initSequenceApp, dburl, bobAccountToken, bobAccountID):
    client, app = initSequenceApp(datafiles, preprocess=False, withBob=True)
    sequence = conftest.getPictureIds(dburl)[0]
    first_pic_id = sequence.pictures[0].id

    # before the delete, we can query the seq
    response = client.get(f"/api/collections/{sequence.id}")
    assert response.status_code == 200

    response = client.get(f"/api/collections/{sequence.id}/items")
    assert len(response.json["features"]) == 5
    assert first_pic_id in [f["id"] for f in response.json["features"]]

    assert os.path.exists(
        datafiles / "derivates" / first_pic_id[0:2] / first_pic_id[2:4] / first_pic_id[4:6] / first_pic_id[6:8] / first_pic_id[9:]
    )
    assert os.path.exists(datafiles / "permanent" / first_pic_id[0:2] / first_pic_id[2:4] / first_pic_id[4:6] / first_pic_id[6:8])

    authorized_header = {"Authorization": f"Bearer {bobAccountToken(app)}"}
    response = client.delete(f"/api/collections/{sequence.id}", headers=authorized_header)
    assert response.status_code == 204

    # The sequence or its pictures should not be returned in any response
    response = client.get(f"/api/collections/{sequence.id}/items/{first_pic_id}")
    assert response.status_code == 404

    response = client.get(f"/api/collections/{sequence.id}")
    assert response.status_code == 404

    # even the user shoudn't see anything
    response = client.get(f"/api/collections/{sequence.id}", headers=authorized_header)
    assert response.status_code == 404
    response = client.get(f"/api/collections/{sequence.id}/items/{first_pic_id}", headers=authorized_header)
    assert response.status_code == 404
    response = client.get(f"/api/collections/{sequence.id}/thumbnail", headers=authorized_header)
    assert response.status_code == 404
    response = client.get(f"/api/collections/{sequence.id}/thumbnail")
    assert response.status_code == 404

    # we should't see this collection in the list of all collections (loggued or not)
    response = client.get(f"/api/collections")
    assert response.status_code == 200 and response.json["collections"] == []
    response = client.get(f"/api/collections", headers=authorized_header)
    assert response.status_code == 200 and response.json["collections"] == []

    # but we should still see it when asking for its status (this can be discussed, if it raises issues)
    status = client.get(f"/api/collections/{sequence.id}/geovisio_status")
    assert status.json["status"] == "deleted"
    assert all(p.get("status") in [None, "waiting-for-delete", "preparing"] for p in status.json["items"])

    with psycopg.connect(dburl) as conn:
        seq = conn.execute("SELECT status FROM sequences WHERE id = %s", [sequence.id]).fetchone()
        assert seq and seq[0] == "deleted"

        # Note: we shouldn't see this when filtering by the function, even for the user
        seq = conn.execute(
            "SELECT status FROM sequences WHERE id = %s AND is_sequence_visible_by_user(sequences, %s)", [sequence.id, bobAccountID]
        ).fetchone()
        assert not seq

        pic_status = conn.execute(
            "SELECT distinct(status) FROM pictures WHERE id = ANY(%(pics)s)", {"pics": [p.id for p in sequence.pictures]}
        ).fetchall()

        # pics are either already deleted or waiting deleting
        assert pic_status == [] or pic_status == [("waiting-for-delete",)]

    # async job should delete at one point all the pictures
    _wait_for_pics_deletion(pics_id=[p.id for p in sequence.pictures], dburl=dburl)

    # check that all files have correctly been deleted since it was the only sequence
    assert os.listdir(datafiles / "derivates") == []
    assert os.listdir(datafiles / "permanent") == []

    # even after pic delete, the sequence is still there, but marked as deleted
    status = client.get(f"/api/collections/{sequence.id}/geovisio_status")
    assert status.json == {"items": [{}], "status": "deleted"}


@conftest.SEQ_IMGS
@conftest.SEQ_IMGS_FLAT
def test_delete_1_sequence_over_2(datafiles, initSequenceApp, dburl, bobAccountToken, bobAccountID):
    """2 sequences available, and delete of them, we should not mess with the other sequence"""
    client, app = initSequenceApp(datafiles, preprocess=False, withBob=True)
    sequence = conftest.getPictureIds(dburl)
    assert len(sequence) == 2

    initial_updated_at = None
    with psycopg.connect(dburl) as conn:
        res = conn.execute("SELECT updated_at FROM sequences WHERE id = %s", [sequence[0].id]).fetchone()
        assert res
        initial_updated_at = res[0]

    # before the delete, we can query both seq
    for seq in sequence:
        response = client.get(f"/api/collections/{seq.id}")
        assert response.status_code == 200

        response = client.get(f"/api/collections/{seq.id}/items")
        assert response.status_code == 200

    for s in sequence:
        for p in s.pictures:
            assert os.path.exists(p.get_derivate_dir(datafiles))
            assert os.path.exists(p.get_permanent_file(datafiles))

    # we delete the first sequence
    response = client.delete(f"/api/collections/{sequence[0].id}", headers={"Authorization": f"Bearer {bobAccountToken(app)}"})
    assert response.status_code == 204

    # The sequence or its pictures should not be returned in any response
    response = client.get(f"/api/collections/{sequence[0].id}/items/{sequence[0].pictures[0].id}")
    assert response.status_code == 404

    response = client.get(f"/api/collections/{sequence[0].id}")
    assert response.status_code == 404

    # everything is still fine for the other sequence
    assert client.get(f"/api/collections/{sequence[1].id}/items/{sequence[1].pictures[0].id}").status_code == 200
    assert client.get(f"/api/collections/{sequence[1].id}").status_code == 200

    # the sequence shouldn't be returned when listing all sequences
    col_ids = lambda r: set([c["id"] for c in r.json["collections"]])
    response = client.get(f"/api/collections")
    assert response.status_code == 200 and col_ids(response) == {sequence[1].id}

    response = client.get(f"/api/collections", headers={"Authorization": f"Bearer {bobAccountToken(app)}"})
    assert response.status_code == 200 and col_ids(response) == {sequence[1].id}

    # nor in the user's collections
    response = client.get(f"/api/users/{bobAccountID}/collection")
    assert response.status_code == 200 and [c["id"] for c in response.json["links"] if c["rel"] == "child"] == [sequence[1].id]
    response = client.get(f"/api/users/{bobAccountID}/collection", headers={"Authorization": f"Bearer {bobAccountToken(app)}"})
    assert response.status_code == 200 and [c["id"] for c in response.json["links"] if c["rel"] == "child"] == [sequence[1].id]

    # but we should be able to see the collection when asking for deleted pictures
    response = client.get("/api/collections?filter=status='deleted' OR status='ready'")
    assert response.status_code == 200 and col_ids(response) == {sequence[0].id, sequence[1].id}
    first_col = next(c for c in response.json["collections"] if c["id"] == sequence[0].id)
    # even deleted col should be valid stac, but marked as deleted
    _ = Collection.from_dict(first_col)
    assert first_col["geovisio:status"] == "deleted"
    # not deleted collection shouldn't have the status
    not_deleted_col = next(c for c in response.json["collections"] if c["id"] == sequence[1].id)
    assert "geovisio:status" not in not_deleted_col

    # and by querying only for deleted collection, we should only have the deleted collection
    response = client.get("/api/collections?filter=status='deleted'")
    assert response.status_code == 200 and col_ids(response) == {sequence[0].id}
    assert response.json["collections"][0]["geovisio:status"] == "deleted"

    # the pagination links should also have the filter query param
    response = client.get(f"/api/collections?filter=status IN ('deleted','ready')&limit=1")
    assert response.status_code == 200
    pagination_links = {l["rel"]: l["href"] for l in response.json["links"] if l["rel"] in {"prev", "next", "first", "last"}}
    assert pagination_links.keys() == {"next", "last"}  # first page, so no prev/first
    for href in pagination_links.values():
        assert "status+IN+('deleted','ready')" in href

    # and the links should be valid
    response = client.get(pagination_links["next"])
    assert response.status_code == 200
    response = client.get(pagination_links["last"])
    assert response.status_code == 200

    with psycopg.connect(dburl) as conn:
        seq = conn.execute("SELECT status, updated_at FROM sequences WHERE id = %s", [sequence[0].id]).fetchone()
        assert seq and seq[0] == "deleted"
        assert seq[1] > initial_updated_at  # the updated_at should have been updated with the delete time

        pic_status = conn.execute(
            "SELECT distinct(status) FROM pictures WHERE id = ANY(%(pics)s)", {"pics": [p.id for p in sequence[0].pictures]}
        ).fetchall()

        # pics are either already deleted or waiting deleting
        assert pic_status == [] or pic_status == [("waiting-for-delete",)]

    # async job should delete at one point all the pictures
    _wait_for_pics_deletion(pics_id=[p.id for p in sequence[0].pictures], dburl=dburl)

    for p in sequence[0].pictures:
        assert not os.path.exists(p.get_derivate_dir(datafiles))
        assert not os.path.exists(p.get_permanent_file(datafiles))
    for p in sequence[1].pictures:
        assert os.path.exists(p.get_derivate_dir(datafiles))
        assert os.path.exists(p.get_permanent_file(datafiles))


@conftest.SEQ_IMGS
def test_delete_sequence_no_auth(datafiles, initSequenceApp, dburl):
    """A sequence cannot be deleted with authentication"""
    client, app = initSequenceApp(datafiles, preprocess=False, withBob=True)
    sequence = conftest.getPictureIds(dburl)
    response = client.delete(f"/api/collections/{sequence[0].id}")
    assert response.status_code == 401
    assert response.json == {"message": "Authentication is mandatory"}


@conftest.SEQ_IMGS
def test_delete_sequence_not_owned(datafiles, initSequenceApp, dburl, defaultAccountToken):
    """A sequence cannot be deleted with authentication"""
    client, app = initSequenceApp(datafiles, preprocess=False, withBob=True)
    sequence = conftest.getPictureIds(dburl)
    response = client.delete(f"/api/collections/{sequence[0].id}", headers={"Authorization": f"Bearer {defaultAccountToken(app)}"})
    assert response.status_code == 403
    assert response.json == {"message": "You're not authorized to edit this sequence", "status_code": 403}


@conftest.SEQ_IMGS
def test_delete_sequence_with_pic_still_waiting_for_process(datafiles, tmp_path, initSequenceApp, dburl, bobAccountToken):
    """Deleting a sequence with pictures that are still waiting to be processed should be fine (and the picture should be removed from the process queue)"""
    app = create_app(
        {
            "TESTING": True,
            "PICTURE_PROCESS_DERIVATES_STRATEGY": "PREPROCESS",
            "DB_URL": dburl,
            "FS_URL": str(tmp_path),
            "SECRET_KEY": "a very secret key",
            "FS_TMP_URL": None,
            "FS_PERMANENT_URL": None,
            "FS_DERIVATES_URL": None,
            "PICTURE_PROCESS_THREADS_LIMIT": 0,  # we run the API without any picture worker, so no pictures will be processed
        }
    )

    with app.app_context(), app.test_client() as client, psycopg.connect(dburl) as conn:
        token = bobAccountToken(app)
        seq_location = conftest.createSequence(client, os.path.basename(datafiles), jwtToken=token)
        pic_id = conftest.uploadPicture(client, seq_location, open(datafiles / "1.jpg", "rb"), "1.jpg", 1, jwtToken=token)
        sequence = conftest.getPictureIds(dburl)[0]

        r = conn.execute("SELECT count(*) FROM pictures_to_process").fetchone()
        assert r and r[0] == 1

        r = conn.execute("SELECT id, status FROM pictures").fetchall()
        assert r and list(r) == [(UUID(pic_id), "waiting-for-process")]

        assert not os.path.exists(sequence.pictures[0].get_derivate_dir(datafiles))
        assert os.path.exists(sequence.pictures[0].get_permanent_file(datafiles))

        response = client.delete(f"/api/collections/{sequence.id}", headers={"Authorization": f"Bearer {token}"})
        assert response.status_code == 204

        # since there are no background worker, the deletion is not happening, but the picture should be marked for deletion
        r = conn.execute("SELECT picture_id, task FROM pictures_to_process").fetchall()
        assert r and r == [(UUID(pic_id), "delete")]

        r = conn.execute("SELECT count(*) FROM pictures").fetchone()
        assert r and r[0] == 1

        # pic should not have been deleted, since we background worker is there
        assert os.path.exists(sequence.pictures[0].get_permanent_file(datafiles))

        # we start the runner picture as a separate process
        import multiprocessing

        def process():
            with app.app_context():
                w = runner_pictures.PictureProcessor(config=app.config, stop=False)
                w.process_next_pictures()

        p = multiprocessing.Process(target=process)
        p.start()
        p.join(timeout=3)  # wait 3 seconds before killing the process
        if p.is_alive():
            p.terminate()
        r = conn.execute("SELECT count(*) FROM pictures_to_process").fetchone()
        assert r and r[0] == 0
        r = conn.execute("SELECT count(*) FROM pictures").fetchone()
        assert r and r[0] == 0

        assert not os.path.exists(sequence.pictures[0].get_permanent_file(datafiles))
        assert not os.path.exists(sequence.pictures[0].get_derivate_dir(datafiles))


def _wait_for_pic_worker(pic_id, dburl):
    with psycopg.connect(dburl) as conn:
        waiting_time = 0.1
        total_time = 0
        pic_status = 0
        while total_time < 20:
            pic_status = conn.execute("SELECT 1 FROM job_history WHERE picture_id = %(pic)s", {"pic": pic_id}).fetchone()

            if pic_status:
                return
            time.sleep(waiting_time)
            total_time += waiting_time
        assert False, f"Pictures not 'preparing'"


@conftest.SEQ_IMG
@conftest.SEQ_IMG_BLURRED
def test_delete_sequence_with_pic_being_processed(datafiles, tmp_path, initSequenceApp, dburl, bobAccountToken, monkeypatch):
    """Deleting a sequence with pictures that are currently processed shoudn't be a problem, the picture should be deleted after the process is finished"""
    app = create_app(
        {
            "TESTING": True,
            "PICTURE_PROCESS_DERIVATES_STRATEGY": "PREPROCESS",
            "DB_URL": dburl,
            "FS_URL": str(tmp_path),
            "SECRET_KEY": "a very secret key",
            "FS_TMP_URL": None,
            "FS_PERMANENT_URL": None,
            "FS_DERIVATES_URL": None,
            "API_BLUR_URL": "https://geovisio-blurring.net",
        }
    )

    def mockCreateBlurredHDPictureFactory(datafiles):
        """Emulate a slow blur process"""

        def mockCreateBlurredHDPicture(fs, blurApi, pictureBytes, outputFilename):
            print("waiting for picture blurring")
            time.sleep(5)
            print("blurring picture")
            with open(datafiles + "/1_blurred.jpg", "rb") as f:
                fs.writebytes(outputFilename, f.read())
                return Image.open(str(datafiles + "/1_blurred.jpg"))

        return mockCreateBlurredHDPicture

    from geovisio import utils

    monkeypatch.setattr(utils.pictures, "createBlurredHDPicture", mockCreateBlurredHDPictureFactory(datafiles))

    with app.app_context(), app.test_client() as client, psycopg.connect(dburl) as conn:
        token = bobAccountToken(app)
        seq_location = conftest.createSequence(client, os.path.basename(datafiles), jwtToken=token)
        pic_id = conftest.uploadPicture(client, seq_location, open(datafiles / "1.jpg", "rb"), "1.jpg", 1, jwtToken=token)
        sequence = conftest.getPictureIds(dburl)[0]

        r = conn.execute("SELECT count(*) FROM pictures_to_process").fetchone()
        assert r and r[0] == 1

        _wait_for_pic_worker(pic_id, dburl)

        # there should be only one job, and it should not be finished yet
        r = conn.execute("SELECT task, finished_at FROM job_history WHERE picture_id = %s", [pic_id]).fetchall()
        assert r and len(r) == 1
        assert r[0][0] == "prepare" and r[0][1] is None

        response = client.delete(f"/api/collections/{sequence.id}", headers={"Authorization": f"Bearer {token}"})
        assert response.status_code == 204

        # The preparing process is quite long but the DELETE call should block until all tasks are finished
        r = conn.execute("SELECT picture_id, task FROM pictures_to_process").fetchall()
        assert r and r == [(UUID(pic_id), "delete")]

        r = conn.execute("SELECT status FROM pictures").fetchone()
        assert r and r[0] == "waiting-for-delete"

        time.sleep(2)  # waiting a bit for the deletion task

        # pic should have been deleted
        assert not os.path.exists(sequence.pictures[0].get_permanent_file(datafiles))
        assert not os.path.exists(sequence.pictures[0].get_derivate_dir(datafiles))

        r = conn.execute("SELECT count(*) FROM pictures_to_process").fetchone()
        assert r and r[0] == 0
        r = conn.execute("SELECT count(*) FROM pictures").fetchone()
        assert r and r[0] == 0


@conftest.SEQ_IMGS
def test_user_collection(datafiles, initSequence, defaultAccountID):
    client = initSequence(datafiles, preprocess=False)

    # Get user ID
    response = client.get(f"/api/users/{defaultAccountID}/collection")
    data = response.json
    userName = "Default account"
    assert response.status_code == 200
    assert data["type"] == "Collection"
    ctl = Collection.from_dict(data)
    assert len(ctl.links) > 0
    assert ctl.title == userName + "'s sequences"
    assert ctl.id == f"user:{defaultAccountID}"
    assert ctl.description == "List of all sequences of user " + userName
    assert ctl.extent.spatial.to_dict() == {"bbox": [[1.9191854417991367, 49.00688961988304, 1.919199780601944, 49.00697341759938]]}
    assert ctl.extent.temporal.to_dict() == {"interval": [["2021-07-29T09:16:54Z", "2021-07-29T09:17:02Z"]]}
    assert ctl.get_links("self")[0].get_absolute_href() == f"http://localhost/api/users/{defaultAccountID}/collection"

    assert ctl.extra_fields["stats:items"]["count"] == 5
    assert data["providers"] == [{"name": "Default account", "roles": ["producer"]}]
    assert ctl.stac_extensions == [
        "https://stac-extensions.github.io/stats/v0.2.0/schema.json",
        "https://stac-extensions.github.io/timestamps/v1.1.0/schema.json",
    ]

    # both `updated` and `created` should be valid date
    dateparser(data["updated"])
    dateparser(data["created"])
    assert data["created"].startswith(date.today().isoformat())
    assert data["updated"].startswith(date.today().isoformat())

    # Check links
    childs = ctl.get_links("child")
    assert len(childs) == 1
    child = childs[0]
    assert child.title is not None
    assert child.extra_fields["id"] is not None
    assert child.get_absolute_href() == "http://localhost/api/collections/" + child.extra_fields["id"]
    assert child.extra_fields["extent"]["temporal"] == {"interval": [["2021-07-29T09:16:54+00:00", "2021-07-29T09:17:02+00:00"]]}
    assert child.extra_fields["extent"]["spatial"] == {
        "bbox": [[1.9191854417991367, 49.00688961988304, 1.919199780601944, 49.00697341759938]]
    }
    assert child.extra_fields["stats:items"]["count"] == 5
    # each collection also have an updated/created date
    assert child.extra_fields["updated"].startswith(date.today().isoformat())
    assert child.extra_fields["created"].startswith(date.today().isoformat())

    # Also test filter parameter works
    response = client.get(f"/api/users/{defaultAccountID}/collection?filter=created >= '2020-01-01' AND updated >= '2023-01-01'")
    data = response.json
    assert response.status_code == 200
    ctl = Collection.from_dict(data)
    childs = ctl.get_links("child")
    assert len(childs) == 1

    # No pagination links as there is no more data to display
    assert len(ctl.get_links("first")) == 0
    assert len(ctl.get_links("prev")) == 0
    assert len(ctl.get_links("next")) == 0
    assert len(ctl.get_links("last")) == 0


@conftest.SEQ_IMGS
def test_user_collection_pagination_outalimit(datafiles, initSequence, defaultAccountID):
    client = initSequence(datafiles, preprocess=False)

    response = client.get(f"/api/users/{defaultAccountID}/collection?limit=50&filter=created > '2100-01-01T10:00:00Z'")
    assert response.status_code == 404
    assert response.json == {"message": "No matching sequences found", "status_code": 404}

    response = client.get(f"/api/users/{defaultAccountID}/collection?limit=50&filter=created < '2000-01-01T10:00:00Z'")
    assert response.status_code == 404
    assert response.json == {"message": "No matching sequences found", "status_code": 404}

    response = client.get(f"/api/users/{defaultAccountID}/collection?limit=-1")
    assert response.status_code == 400
    assert response.json == {"message": "limit parameter should be an integer between 1 and 1000", "status_code": 400}

    response = client.get(f"/api/users/{defaultAccountID}/collection?limit=1001")
    assert response.status_code == 400
    assert response.json == {"message": "limit parameter should be an integer between 1 and 1000", "status_code": 400}


@conftest.SEQ_IMGS
def test_user_collection_filter_bbox(datafiles, initSequence, defaultAccountID):
    client = initSequence(datafiles, preprocess=False)

    response = client.get(f"/api/users/{defaultAccountID}/collection?bbox=0,0,1,1")
    assert response.status_code == 200
    assert [l for l in response.json["links"] if l["rel"] == "child"] == []

    response = client.get(f"/api/users/{defaultAccountID}/collection?bbox=1.312864,48.004817,3.370054,49.357521")
    assert response.status_code == 200

    childs = [l for l in response.json["links"] if l["rel"] == "child"]
    assert len(childs) == 1


@pytest.mark.parametrize(
    ("min", "max", "dmin", "dmax", "direction", "expected", "additional_filters"),
    (
        ##############################################
        # In ascending order
        #
        # In middle of dataset bounds
        [
            "2021-01-01",
            "2021-01-15",
            None,
            None,
            SQLDirection.ASC,
            {
                "first": "sortby=%2Bcreated",
                "prev": "sortby=%2Bcreated&page=created+%3C+'2021-01-01'",
                "next": "sortby=%2Bcreated&page=created+%3E+'2021-01-15'",
                "last": "sortby=%2Bcreated&page=created+%3C%3D+'2024-12-31'",
            },
            None,
        ],
        # Matches dataset bounds
        ["2020-01-01", "2024-12-31", None, None, SQLDirection.ASC, {}, None],
        # Starting on dataset bounds
        [
            "2020-01-01",
            "2021-01-15",
            None,
            None,
            SQLDirection.ASC,
            {"next": "sortby=%2Bcreated&page=created+%3E+'2021-01-15'", "last": "sortby=%2Bcreated&page=created+%3C%3D+'2024-12-31'"},
            None,
        ],
        # Ending on dataset bounds
        [
            "2021-01-01",
            "2024-12-31",
            None,
            None,
            SQLDirection.ASC,
            {
                "first": "sortby=%2Bcreated",
                "prev": "sortby=%2Bcreated&page=created+%3C+'2021-01-01'",
            },
            None,
        ],
        ##############################################
        # In descending order
        #
        # In middle of dataset bounds
        [
            "2021-01-01",
            "2021-01-15",
            None,
            None,
            SQLDirection.DESC,
            {
                "first": "sortby=-created",
                "prev": "sortby=-created&page=created+%3E+'2021-01-15'",
                "next": "sortby=-created&page=created+%3C+'2021-01-01'",
                "last": "sortby=-created&page=created+%3E%3D+'2020-01-01'",
            },
            None,
        ],
        # Matches dataset bounds
        ["2020-01-01", "2024-12-31", None, None, SQLDirection.DESC, {}, None],
        # Starting on dataset bounds
        [
            "2020-01-01",
            "2021-01-15",
            None,
            None,
            SQLDirection.DESC,
            {
                "first": "sortby=-created",
                "prev": "sortby=-created&page=created+%3E+'2021-01-15'",
            },
            None,
        ],
        # Ending on dataset bounds
        [
            "2021-01-01",
            "2024-12-31",
            None,
            None,
            SQLDirection.DESC,
            {"next": "sortby=-created&page=created+%3C+'2021-01-01'", "last": "sortby=-created&page=created+%3E%3D+'2020-01-01'"},
            None,
        ],
        # additional_filters
        [
            "2021-01-01",
            "2021-01-15",
            None,
            None,
            SQLDirection.ASC,
            {
                "first": "filter=status%3D'deleted'&sortby=%2Bcreated",
                "prev": "sortby=%2Bcreated&filter=status%3D'deleted'&page=created+%3C+'2021-01-01'",
                "next": "sortby=%2Bcreated&filter=status%3D'deleted'&page=created+%3E+'2021-01-15'",
                "last": "sortby=%2Bcreated&filter=status%3D'deleted'&page=created+%3C%3D+'2024-12-31'",
            },
            "status='deleted'",
        ],
    ),
)
def test_get_pagination_links(dburl, tmp_path, min, max, dmin, dmax, direction, expected, additional_filters):
    app = create_app(
        {
            "TESTING": True,
            "PICTURE_PROCESS_DERIVATES_STRATEGY": "ON_DEMAND",
            "DB_URL": dburl,
            "FS_URL": str(tmp_path),
            "SECRET_KEY": "a very secret key",
            "SERVER_NAME": "geovisio.fr",
            "FS_TMP_URL": None,
            "FS_PERMANENT_URL": None,
            "FS_DERIVATES_URL": None,
            "PICTURE_PROCESS_THREADS_LIMIT": 0,  # we run the API without any picture worker, so no pictures will be processed
        }
    )

    with app.app_context():
        res = geovisio.web.collections.get_pagination_links(
            "stac_collections.getUserCollection",
            {"limit": 50, "userId": "1234"},
            "created",
            direction,
            Bounds(min=dmin or "2020-01-01", max=dmax or "2024-12-31"),
            Bounds(min=min, max=max),
            additional_filters=additional_filters,
        )

        assert len(expected.items()) == len(res)

        for expectedRelType, expectedRelHref in expected.items():
            resRelHref = next(l["href"] for l in res if l["rel"] == expectedRelType)
            assert resRelHref == f"http://geovisio.fr/api/users/1234/collection?limit=50&{expectedRelHref}"
