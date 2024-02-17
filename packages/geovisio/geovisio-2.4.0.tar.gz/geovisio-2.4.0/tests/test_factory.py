import pytest
import os
from geovisio import create_app, config_app


def test_index(client):
    response = client.get("/")
    assert b"GeoVisio" in response.data


@pytest.mark.parametrize(
    ("readEnv", "cpu", "expected"),
    (
        ("10", 20, 10),
        ("10", 5, 5),
        ("-1", 10, 10),
    ),
)
def test_get_threads_limit(monkeypatch, readEnv, cpu, expected):
    monkeypatch.setattr(os, "cpu_count", lambda: cpu)
    res = config_app._get_threads_limit(readEnv)
    assert res == expected
    assert res >= 1


@pytest.mark.parametrize(
    ("forceAuth", "oauth", "expected"),
    (
        ("true", True, True),
        ("", True, False),
        ("false", True, False),
        (None, True, False),
        (None, False, False),
        ("true", False, True),
        ("false", False, False),
    ),
)
def test_config_app_forceAuthUpload(dburl, tmp_path, forceAuth, oauth, expected):
    config = {
        "TESTING": True,
        "DB_URL": dburl,
        "FS_URL": str(tmp_path),
        "FS_TMP_URL": None,
        "FS_PERMANENT_URL": None,
        "FS_DERIVATES_URL": None,
        "API_FORCE_AUTH_ON_UPLOAD": forceAuth,
    }

    if oauth:
        config["OAUTH_PROVIDER"] = "oidc"
        config["OAUTH_OIDC_URL"] = "https://bla.net"
        config["OAUTH_CLIENT_ID"] = "bla"
        config["OAUTH_CLIENT_SECRET"] = "bla"

    if expected == "fail":
        with pytest.raises(Exception):
            app = create_app(config)
    else:
        app = create_app(config)
        assert app.config["API_FORCE_AUTH_ON_UPLOAD"] == expected


@pytest.mark.parametrize(
    ("license_spdx_id", "license_url", "expected"),
    (
        ("etalab-2.0", "https://www.etalab.gouv.fr/licence-ouverte-open-licence/", True),
        (None, None, True),
        ("etalab-2.0", None, False),
        (None, "https://www.etalab.gouv.fr/licence-ouverte-open-licence/", False),
    ),
)
def test_config_app_license(dburl, tmp_path, license_spdx_id, license_url, expected):
    config = {
        "TESTING": True,
        "DB_URL": dburl,
        "FS_URL": str(tmp_path),
        "FS_TMP_URL": None,
        "FS_PERMANENT_URL": None,
        "FS_DERIVATES_URL": None,
        "API_PICTURES_LICENSE_SPDX_ID": license_spdx_id,
        "API_PICTURES_LICENSE_URL": license_url,
    }
    if not expected:
        with pytest.raises(Exception):
            app = create_app(config)
    else:
        app = create_app(config)
        if license_url is None:
            assert app.config["API_PICTURES_LICENSE_SPDX_ID"] == "proprietary"


@pytest.mark.parametrize(
    ("main", "viewer", "fails"),
    (
        (None, None, None),
        ("https://panoramax.fr", "https://panoramax.fr", None),
        ("", None, "API_MAIN_PAGE environment variable is not defined"),
        ("main.html", "", "API_VIEWER_PAGE environment variable is not defined"),
        ("prout", None, "API_MAIN_PAGE variable points to invalid template"),
        (None, "prout", "API_VIEWER_PAGE variable points to invalid template"),
    ),
)
def test_config_app_pages(dburl, tmp_path, main, viewer, fails):
    config = {
        "TESTING": True,
        "DB_URL": dburl,
        "FS_URL": str(tmp_path),
        "FS_TMP_URL": None,
        "FS_PERMANENT_URL": None,
        "FS_DERIVATES_URL": None,
    }

    if main is not None:
        config["API_MAIN_PAGE"] = main
    if viewer is not None:
        config["API_VIEWER_PAGE"] = viewer

    if fails is not None:
        with pytest.raises(Exception) as e:
            app = create_app(config)

        assert str(e.value).startswith(fails)

    else:
        app = create_app(config)
        assert app.config["API_MAIN_PAGE"] == main or "main.html"
        assert app.config["API_VIEWER_PAGE"] == viewer or "viewer.html"
