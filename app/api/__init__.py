from flask import Blueprint
from flask_restplus import Api
import os

# Define api blueprint
api_blueprint = Blueprint('api', __name__, url_prefix='/api')

# Define restful api for blueprint
api = Api(api_blueprint,
	title='python flask full stack',
	version='1.0',
	description='An API list for python stack',
)

# Import api_namespace
from app.api.developer.controller import namespace_developer

# Add namespace to blueprint
api.add_namespace(namespace_developer)