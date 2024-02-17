import os
import pytest
import mapbox_vector_tile

from geovisio.web import map
from geovisio import errors
from . import conftest


FIXTURE_DIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), "data")


@pytest.mark.parametrize(
    ("z", "x", "y", "format", "result"),
    (
        (6, 0, 0, "mvt", True),
        (6, 0, 1, "mvt", True),
        (6, 1, 0, "mvt", True),
        (6, 1, 1, "mvt", True),
        (-1, 0, 0, "mvt", 404),
        (16, 0, 0, "mvt", 404),
        (6, -1, 0, "mvt", 404),
        (6, 64, 0, "mvt", 404),
        (6, 0, -1, "mvt", 404),
        (6, 0, 64, "mvt", 404),
        (6, 0, 0, "jpg", 400),
        (None, 0, 0, "jpg", 400),
        (6, None, 0, "jpg", 400),
        (6, 0, None, "jpg", 400),
        (6, 0, 0, None, 400),
    ),
)
def test_isTileValid(z, x, y, format, result):
    if result is True:
        map.checkTileValidity(z, x, y, format)
    else:
        with pytest.raises(errors.InvalidAPIUsage) as e_info:
            map.checkTileValidity(z, x, y, format)
            assert e_info.value.status_code == result


@conftest.SEQ_IMGS
@pytest.mark.parametrize(
    ("z", "x", "y", "layersCount"),
    (
        (14, 8279, 5626, {"pictures": 5, "sequences": 1}),
        (11, 1034, 703, {"sequences": 1}),
        (11, 0, 0, {}),
        (6, 32, 21, {}),  # No sequences due to simplification
        (0, 0, 0, {}),  # No sequences due to simplification
    ),
)
def test_getTile(datafiles, initSequence, z, x, y, layersCount):
    client = initSequence(datafiles, preprocess=False)

    response = client.get(f"/api/map/{z}/{x}/{y}.mvt")

    assert response.status_code == 200
    data = mapbox_vector_tile.decode(response.get_data())

    for layerName, layerCount in layersCount.items():
        assert layerName in data
        assert len(data[layerName]["features"]) == layerCount
        # all pictures and sequence should be set as visible
        for f in data[layerName]["features"]:
            assert "hidden" not in f["properties"]  # if hidden is not in properties, it means it's visible
            # all pictures and sequence should have an accountId
            assert "account_id" in f["properties"]
            assert f["properties"].get("model") == "GoPro Max"
            assert f["properties"].get("type") == "equirectangular"

            if layerName == "sequences":
                assert f["properties"].get("date") == "2021-07-29"
            else:
                assert f["properties"].get("ts").startswith("2021-07-29")


def _get_prop_by_id(geoj):
    res = {}
    for t in ["pictures", "sequences"]:
        res[t] = {t["properties"]["id"]: t["properties"] for t in geoj.get(t, {}).get("features", [])}
    return res


def _get_tiles_data(response):
    assert response.status_code == 200
    data = mapbox_vector_tile.decode(response.get_data())
    return data, {
        "nb_pic": len(data.get("pictures", {}).get("features", [])),
        "nb_seq": len(data.get("sequences", {}).get("features", [])),
    }


@conftest.SEQ_IMGS
def test_getTile_hidden(datafiles, initSequenceApp, dburl, bobAccountToken, bobAccountID):
    client, app = initSequenceApp(datafiles, preprocess=False, withBob=True)
    sequence = conftest.getPictureIds(dburl)[0]

    def _get_general_tiles_features(asBob: bool):
        headers = {"Authorization": f"Bearer {bobAccountToken(app)}"} if asBob else {}
        response = client.get("/api/map/14/8279/5626.mvt", headers=headers)
        # the tiles can be cached by a shared cache as they do not contain any user data
        assert response.headers.get("Cache-Control") == "public"
        return _get_tiles_data(response)

    def _get_bob_tiles_features(asBob: bool):
        headers = {"Authorization": f"Bearer {bobAccountToken(app)}"} if asBob else {}
        response = client.get(f"/api/users/{bobAccountID}/map/14/8279/5626.mvt", headers=headers)
        if asBob:
            # the tiles cannot be cached by a shared cache as they do not contain user's specific data
            assert response.headers.get("Cache-Control") == "private"
        else:
            # the tiles can be cached by a shared cache as they do not contain any user data
            assert response.headers.get("Cache-Control") == "public"
        return _get_tiles_data(response)

    assert _get_general_tiles_features(asBob=False)[1] == {"nb_pic": 5, "nb_seq": 1}
    # since there are only bob's data, getting bob's tile should return all tiles
    assert _get_bob_tiles_features(asBob=False)[1] == {"nb_pic": 5, "nb_seq": 1}
    assert _get_bob_tiles_features(asBob=True)[1] == {"nb_pic": 5, "nb_seq": 1}

    # we hide a picture
    response = client.patch(
        f"/api/collections/{str(sequence.id)}/items/{str(sequence.pictures[0].id)}",
        data={"visible": "false"},
        headers={"Authorization": f"Bearer {bobAccountToken(app)}"},
    )
    assert response.status_code == 200

    assert _get_general_tiles_features(asBob=False)[1] == {"nb_pic": 4, "nb_seq": 1}
    # even the owner shouldn't see it in the generic tiles
    assert _get_general_tiles_features(asBob=True)[1] == {"nb_pic": 4, "nb_seq": 1}
    # but they should be in the user's tiles, only if it's bob whose asking
    assert _get_bob_tiles_features(asBob=False)[1] == {"nb_pic": 4, "nb_seq": 1}
    t, stats = _get_bob_tiles_features(asBob=True)
    assert stats == {"nb_pic": 5, "nb_seq": 1}
    all_props = _get_prop_by_id(t)
    assert all_props["pictures"][str(sequence.pictures[0].id)]["hidden"] is True
    for p in sequence.pictures[1:]:
        assert "hidden" not in all_props["pictures"][str(p.id)]

    # we hide the whole sequence
    response = client.patch(
        f"/api/collections/{str(sequence.id)}", data={"visible": "false"}, headers={"Authorization": f"Bearer {bobAccountToken(app)}"}
    )
    assert response.status_code == 200

    assert _get_general_tiles_features(asBob=False)[1] == {"nb_pic": 0, "nb_seq": 0}
    # same, even the owner shouldn't see it in the generic tiles
    assert _get_general_tiles_features(asBob=True)[1] == {"nb_pic": 0, "nb_seq": 0}
    # but they should be in the user's tiles, only if it's bob whose asking
    assert _get_bob_tiles_features(asBob=False)[1] == {"nb_pic": 0, "nb_seq": 0}
    t, stats = _get_bob_tiles_features(asBob=True)
    assert stats == {"nb_pic": 5, "nb_seq": 1}
    all_props = _get_prop_by_id(t)
    assert all_props["sequences"][str(sequence.id)]["hidden"] is True
    for p in sequence.pictures:
        assert all_props["pictures"][str(p.id)]["hidden"] is True

    # we unhide the sequence
    response = client.patch(
        f"/api/collections/{str(sequence.id)}", data={"visible": "true"}, headers={"Authorization": f"Bearer {bobAccountToken(app)}"}
    )

    assert _get_general_tiles_features(asBob=False)[1] == {"nb_pic": 4, "nb_seq": 1}
    assert _get_general_tiles_features(asBob=True)[1] == {"nb_pic": 4, "nb_seq": 1}
    # but they should be in the user's tiles, only if it's bob whose asking
    assert _get_bob_tiles_features(asBob=False)[1] == {"nb_pic": 4, "nb_seq": 1}
    t, stats = _get_bob_tiles_features(asBob=True)
    all_props = _get_prop_by_id(t)
    assert "hidden" not in all_props["sequences"][str(sequence.id)]
    assert all_props["pictures"][str(sequence.pictures[0].id)]["hidden"] is True
    for p in sequence.pictures[1:]:
        assert "hidden" not in all_props["pictures"][str(p.id)]

    # we unhide the picture
    response = client.patch(
        f"/api/collections/{str(sequence.id)}/items/{str(sequence.pictures[0].id)}",
        data={"visible": "true"},
        headers={"Authorization": f"Bearer {bobAccountToken(app)}"},
    )
    assert response.status_code == 200
    assert _get_general_tiles_features(asBob=False)[1] == {"nb_pic": 5, "nb_seq": 1}
    assert _get_general_tiles_features(asBob=True)[1] == {"nb_pic": 5, "nb_seq": 1}
    assert _get_bob_tiles_features(asBob=False)[1] == {"nb_pic": 5, "nb_seq": 1}
    assert _get_bob_tiles_features(asBob=True)[1] == {"nb_pic": 5, "nb_seq": 1}

    # if we delete the sequence, nobody should see nothing anymore
    response = client.delete(
        f"/api/collections/{str(sequence.id)}",
        data={"visible": "true"},
        headers={"Authorization": f"Bearer {bobAccountToken(app)}"},
    )
    assert response.status_code == 204
    assert _get_general_tiles_features(asBob=False)[1] == {"nb_pic": 0, "nb_seq": 0}
    assert _get_general_tiles_features(asBob=True)[1] == {"nb_pic": 0, "nb_seq": 0}
    assert _get_bob_tiles_features(asBob=False)[1] == {"nb_pic": 0, "nb_seq": 0}
    assert _get_bob_tiles_features(asBob=True)[1] == {"nb_pic": 0, "nb_seq": 0}


def test_get_user_Tiles(app, client, dburl, bobAccountToken, bobAccountID, defaultAccountID, defaultAccountToken):
    """Load 1 sequence as a 'bob' and one as 'default_account' and check that each user's tile correctly return only owned data"""

    import pathlib

    datadir = pathlib.Path(FIXTURE_DIR)

    conftest.uploadSequenceFromPics(
        test_client=client,
        title="bob's sequence",
        wait=True,
        jwtToken=bobAccountToken(app),
        pics=[
            datadir / "1.jpg",
            datadir / "2.jpg",
            datadir / "3.jpg",
        ],
    )
    conftest.uploadSequenceFromPics(
        test_client=client,
        title="default account sequence",
        wait=True,
        jwtToken=defaultAccountToken(app),
        pics=[
            datadir / "4.jpg",
            datadir / "5.jpg",
        ],
    )

    def _get_general_tiles_features(asBob: bool):
        headers = {"Authorization": f"Bearer {bobAccountToken(app)}"} if asBob else {}
        response = client.get("/api/map/14/8279/5626.mvt", headers=headers)
        return _get_tiles_data(response)

    def _get_user_tiles_features(id, token_func=None, query_params=""):
        headers = {"Authorization": f"Bearer {token_func(app)}"} if token_func else {}
        response = client.get(f"/api/users/{id}/map/14/8279/5626.mvt{query_params}", headers=headers)
        return _get_tiles_data(response)

    assert _get_general_tiles_features(asBob=False)[1] == {"nb_pic": 5, "nb_seq": 2}
    assert _get_user_tiles_features(bobAccountID, None)[1] == {"nb_pic": 3, "nb_seq": 1}
    assert _get_user_tiles_features(bobAccountID, bobAccountToken)[1] == {"nb_pic": 3, "nb_seq": 1}
    assert _get_user_tiles_features(defaultAccountID, None)[1] == {"nb_pic": 2, "nb_seq": 1}
    assert _get_user_tiles_features(defaultAccountID, defaultAccountToken)[1] == {"nb_pic": 2, "nb_seq": 1}

    # we can also hide bob's seqence and 1 pic from the default account's sequence
    sequence = conftest.getPictureIds(dburl)
    response = client.patch(
        f"/api/collections/{str(sequence[0].id)}",
        data={"visible": "false"},
        headers={"Authorization": f"Bearer {bobAccountToken(app)}"},
    )
    assert response.status_code == 200
    response = client.patch(
        f"/api/collections/{str(sequence[1].id)}/items/{str(sequence[1].pictures[0].id)}",
        data={"visible": "false"},
        headers={"Authorization": f"Bearer {defaultAccountToken(app)}"},
    )
    assert response.status_code == 200

    # only one sequence is visible for everybody
    assert _get_general_tiles_features(asBob=False)[1] == {"nb_pic": 1, "nb_seq": 1}
    assert _get_user_tiles_features(bobAccountID, None)[1] == {"nb_pic": 0, "nb_seq": 0}
    assert _get_user_tiles_features(bobAccountID, bobAccountToken)[1] == {"nb_pic": 3, "nb_seq": 1}
    assert _get_user_tiles_features(defaultAccountID, None)[1] == {"nb_pic": 1, "nb_seq": 1}
    assert _get_user_tiles_features(defaultAccountID, defaultAccountToken)[1] == {"nb_pic": 2, "nb_seq": 1}

    # and we can only get the hidden pic when adding the `?filter=status=hidden` if queried by the author
    # the query param is only available for user's specific tiles
    only_hidden = "?filter=status='hidden'"

    assert _get_user_tiles_features(bobAccountID, None, query_params=only_hidden)[1] == {"nb_pic": 0, "nb_seq": 0}
    assert _get_user_tiles_features(bobAccountID, bobAccountToken, query_params=only_hidden)[1] == {"nb_pic": 3, "nb_seq": 1}
    # asking for only hidden when we don't have the rights to see them result in 0 pics shown
    assert _get_user_tiles_features(defaultAccountID, None, query_params=only_hidden)[1] == {"nb_pic": 0, "nb_seq": 0}

    assert _get_user_tiles_features(defaultAccountID, defaultAccountToken, query_params=only_hidden)[1] == {"nb_pic": 1, "nb_seq": 0}

    # there are also shortcut to get one's tiles
    response = client.get(f"/api/users/me/map/14/8279/5626.mvt", headers={"Authorization": f"Bearer {defaultAccountToken(app)}"})
    assert response.status_code == 200
    assert _get_tiles_data(response)[1] == {"nb_pic": 2, "nb_seq": 1}
    response = client.get(
        f"/api/users/me/map/14/8279/5626.mvt{only_hidden}", headers={"Authorization": f"Bearer {defaultAccountToken(app)}"}
    )
    assert response.status_code == 200
    assert _get_tiles_data(response)[1] == {"nb_pic": 1, "nb_seq": 0}


def test_get_user_Tiles_higher_zoom(app, client, dburl, bobAccountToken, bobAccountID):
    """Load 1 sequence with far points, not to simplified at higher zoom level"""

    import pathlib

    datadir = pathlib.Path(FIXTURE_DIR)

    seq_location = conftest.createSequence(client, "seq1", jwtToken=bobAccountToken(app))
    initial_lon = 1.7
    initial_lat = 46
    step = 2 / 11111  # roughly 20m
    pics = [
        datadir / "1.jpg",
        datadir / "2.jpg",
        datadir / "3.jpg",
        datadir / "4.jpg",
        datadir / "5.jpg",
    ]

    for i, p in enumerate(pics * 3):  # load 15 points to have a geometry even avec simplification
        conftest.uploadPicture(
            client,
            seq_location,
            open(p, "rb"),
            p.name,
            i + 1,
            jwtToken=bobAccountToken(app),
            overrides={"override_longitude": initial_lon + step * i, "override_latitude": initial_lat},
        )

    conftest.waitForSequence(client, seq_location)

    sequence = conftest.getPictureIds(dburl)[0]
    response = client.get("/api/map/6/32/22.mvt", headers={"Authorization": f"Bearer {bobAccountToken(app)}"})
    assert response.status_code == 200
    t, stats = _get_tiles_data(response)
    # high zoom tile should not contains picture info
    assert _get_tiles_data(response)[1] == {"nb_pic": 0, "nb_seq": 1}
    all_props = _get_prop_by_id(t)

    assert all_props["sequences"][str(sequence.id)] == {"id": sequence.id}

    response = client.get("/api/users/me/map/6/32/22.mvt", headers={"Authorization": f"Bearer {bobAccountToken(app)}"})
    assert response.status_code == 200
    t, stats = _get_tiles_data(response)
    # high zoom tile should not contains picture info
    assert _get_tiles_data(response)[1] == {"nb_pic": 0, "nb_seq": 1}
    all_props = _get_prop_by_id(t)

    # we get more info, even at higher zoom
    assert all_props["sequences"][str(sequence.id)] == {
        "id": sequence.id,
        "account_id": str(bobAccountID),
        "date": "2021-07-29",
        "model": "GoPro Max",
        "type": "equirectangular",
    }
