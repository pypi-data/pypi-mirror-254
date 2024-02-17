import pytest


def test_unlogged_user_retrieval_without_oauth(client):
    """it should be impossible to access current user info if the instance has no oauth"""
    response = client.get("/api/users/me")
    assert response.status_code == 403


@pytest.fixture
def client_app_with_lots_of_users(dburl, client):
    import psycopg
    from psycopg.sql import SQL

    users = [
        "bobette",
        "bobito",
        "onésime",
        "elie",
        "elise",
        "eloïse",
        "armand",
        "paul",
        "zeline",
        "Loïs",
        "Buenaventura",
        "Mohamed",
        "He-Yin",
    ]
    with psycopg.connect(dburl) as conn, conn.cursor() as cursor:
        for u in users:
            accountID = cursor.execute("SELECT id from accounts WHERE name = %s", [u]).fetchone()
            if accountID:
                continue
            cursor.execute("INSERT INTO accounts (name) VALUES  (%s)", [u])
            conn.commit()

        yield client
        for u in users:
            cursor.execute("DELETE FROM accounts where name = %s", [u])
            conn.commit()


@pytest.mark.parametrize(
    ("query"),
    (
        [
            ("b"),
            ("ob"),
            ("bob"),
        ]
    ),
)
def test_user_search_bob(client, bobAccountID, query):
    r = client.get(f"/api/users/search?q={query}")

    assert r.status_code == 200
    assert r.json == {
        "features": [
            {
                "id": str(bobAccountID),
                "label": "bob",
                "links": [
                    {
                        "href": f"http://localhost:5000/api/users/{bobAccountID}",
                        "rel": "user-info",
                        "type": "application/json",
                    },
                    {
                        "href": f"http://localhost:5000/api/users/{bobAccountID}/collection",
                        "rel": "collection",
                        "type": "application/json",
                    },
                ],
            }
        ],
    }


def test_user_search_limit(client_app_with_lots_of_users, bobAccountID, dburl):
    r = client_app_with_lots_of_users.get(f"/api/users/search?q=el")

    assert len(set((f["label"] for f in r.json["features"]))) > 2
    r = client_app_with_lots_of_users.get(f"/api/users/search?q=el&limit=2")

    assert len([f["label"] for f in r.json["features"]]) == 2


def test_unknonw_user_search(client_app_with_lots_of_users, bobAccountID):
    r = client_app_with_lots_of_users.get("/api/users/search?q=some_unknown_user_name")
    assert r.status_code == 200
    assert r.json == {"features": []}


@pytest.mark.parametrize(
    ("query"),
    (
        [
            (""),
            ("?q="),
        ]
    ),
)
def test_bad_user_search(client_app_with_lots_of_users, query):
    r = client_app_with_lots_of_users.get(f"/api/users/search{query}")
    assert r.json == {"message": "No search parameter given, you should provide `q=<pattern>` as query parameter", "status_code": 400}
    assert r.status_code == 400


def test_user_info(client_app_with_lots_of_users, bobAccountID):
    r = client_app_with_lots_of_users.get(f"/api/users/{bobAccountID}")
    assert r.status_code == 200
    assert r.json == {
        "id": str(bobAccountID),
        "name": "bob",
        "links": [
            {"href": f"http://localhost:5000/api/users/{bobAccountID}/catalog/", "rel": "catalog", "type": "application/json"},
            {"href": f"http://localhost:5000/api/users/{bobAccountID}/collection", "rel": "collection", "type": "application/json"},
            {
                "href": f"http://localhost:5000/api/users/{bobAccountID}" + "/map/{z}/{x}/{y}.mvt",
                "rel": "user-xyz",
                "title": "Pictures and sequences vector tiles for a given user",
                "type": "application/vnd.mapbox-vector-tile",
            },
        ],
    }


def test_unknown_user_info(client_app_with_lots_of_users):
    r = client_app_with_lots_of_users.get(f"/api/users/00000000-0000-0000-0000-000000000000")
    assert r.status_code == 404
    assert r.json == {"message": "Impossible to find user", "status_code": 404}


def test_user_list(client_app_with_lots_of_users, bobAccountID):
    r = client_app_with_lots_of_users.get(f"/api/users")
    assert r.status_code == 200

    assert r.json["links"] == [
        {"href": f"http://localhost:5000/api/users/search", "rel": "user-search", "title": "Search users", "type": "application/json"},
    ]
    users = r.json["users"]
    users_by_name = {
        r["name"]: r
        for r in users
        if r["name"] not in ("elysee", "elie_reclus")  # those name are added by another test, we don't want them to interfere with this one
    }
    assert set(users_by_name.keys()) == {
        "Default account",
        "bob",
        "bobette",
        "bobito",
        "onésime",
        "elie",
        "elise",
        "eloïse",
        "armand",
        "paul",
        "zeline",
        "Loïs",
        "Buenaventura",
        "Mohamed",
        "He-Yin",
    }

    # test one users
    assert users_by_name["bob"] == {
        "id": str(bobAccountID),
        "name": "bob",
        "links": [
            {
                "href": f"http://localhost:5000/api/users/{str(bobAccountID)}",
                "rel": "user-info",
                "type": "application/json",
            },
            {
                "href": f"http://localhost:5000/api/users/{str(bobAccountID)}/collection",
                "rel": "collection",
                "type": "application/json",
            },
        ],
    }
