from flask import Blueprint
from flask_restx import Api
import os
from app import app

# Define api blueprint
api_blueprint = Blueprint('api', __name__, url_prefix='/api')

# Define restful api for blueprint
api = Api(api_blueprint,
	title='python flask full stack',
	version='1.0',
	description='An API list for python stack',
)

# Auto register api blueprint under app/api
# Import a module / component using its blueprint handler variable (mod_auth)
# dl = next(os.walk('app/api'))[1]
mod_api = app.config['ENABLED_API_MODULES']

for i in mod_api:
	if app.config['ENABLED_API_MODULES'][i]:
		temp_controller = 'app.api.' + i + '.controller'
		temp_blueprint = i + '_namespace'
		temp_import = 'from ' + temp_controller + ' import ' + temp_blueprint
		temp_blueprint_register = 'api.add_namespace(' + temp_blueprint + ')'

		# Import controllers
		exec(temp_import)

		# regiser blueprint
		exec(temp_blueprint_register)
