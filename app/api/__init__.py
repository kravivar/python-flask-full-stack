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

# Auto generate Route Definitions for api
# Import a module / component using its blueprint handler variable (mod_auth)
dl = next(os.walk('app/api'))[1]

for i in dl:
	temp_controller = 'app.api.' + i + '.controller'
	temp_blueprint = i + '_namespace'
	temp_import = 'from ' + temp_controller + ' import ' + temp_blueprint
	temp_blueprint_register = 'api.add_namespace(' + temp_blueprint + ')'

	# Import controllers
	exec(temp_import)

	# regiser blueprint
	exec(temp_blueprint_register)
