"""
Main python file that contains the Flask application
which is used by Gunicorn WSGI application server.
"""
from flask import Flask

from PROJECT_NAME.setup import setup_app
from PROJECT_NAME.setup import setup_blueprints

# creates main app instance for Gunicorn
app = Flask(__name__)

# sets the flask application config
setup_app(app)

# adds all the blueprints to the application
setup_blueprints(app)
