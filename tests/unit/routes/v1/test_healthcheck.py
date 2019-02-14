"""
Module with unit tests of the healthcheck route.
"""
from unittest import mock

import flask
import pytest
from flask.testing import FlaskClient

from app import app


@pytest.fixture(scope="module")
def client() -> FlaskClient:
    """
    Starts flask testing client.
    """
    app.config["TESTING"] = True
    return app.test_client()


@mock.patch("PROJECT_NAME.routes.v1.healthcheck.run_healthchecks")
def test_healthcheck_ok(mocked_run_healthchecks: mock.MagicMock, client: FlaskClient):
    """
    Unit: healthcheck unit test.
    """
    health_dict = {}
    mocked_run_healthchecks.return_value = health_dict

    # route invocation
    response: flask.Response = client.get("/healthcheck")
    response_payload = response.get_json()

    mocked_run_healthchecks.assert_called_once_with()

    assert response_payload == health_dict
    assert response.status_code == 200
