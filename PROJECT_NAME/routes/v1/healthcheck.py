"""
Module with the healthcheck routes.
"""
import logging

from flask import Blueprint
from flask import jsonify
from flask import make_response

from PROJECT_NAME.services.healthcheck import run_healthchecks

# routes adding to blueprint
healthcheck_routes = Blueprint("healthcheck_routes", __name__)

logger = logging.getLogger(__name__)


@healthcheck_routes.route("/healthcheck")
def healthcheck_route() -> None:
    """
    healthcheck to be monitored.
    """
    health_dict = run_healthchecks()
    status_code = 200

    return make_response(jsonify(health_dict), status_code)
