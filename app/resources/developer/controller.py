# Importing Flask and dependencies
from flask import Blueprint
from flask_restful import Api

# Importing resources
from app.resources.developer.resource import DeveloperApi

# Defining home blueprint
app_developer = Blueprint('developer', __name__, url_prefix='/api/dev')
api_developer = Api(app_developer)

## Defining method for getting all developers
api_developer.add_resource(DeveloperApi, '/') 