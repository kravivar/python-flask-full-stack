from flask import Flask, jsonify, abort, request
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

# Configuration based on environment
CONFIG_NAME_MAPPER = {
    'development': 'config.DevelopmentConfig',
    'stage': 'config.StageConfig',
    'default': 'config.DevelopmentConfig',
}

flask_environment = os.getenv('FLASK_ENVIRONMENT');

if flask_environment is not None:
	app.config.from_object(CONFIG_NAME_MAPPER[flask_environment])
else:
	app.config.from_object(CONFIG_NAME_MAPPER['default'])

db = SQLAlchemy(app)

# Import api blueprint under app/api
from app.api import api_blueprint

# register api blueprint
app.register_blueprint(api_blueprint)

# Auto register ui blueprint under app/ui
# dl = next(os.walk('app/ui'))[1]
mod_ui = app.config['ENABLED_UI_MODULES']

for i in mod_ui:
	if app.config['ENABLED_UI_MODULES'][i]:
		temp_controller = 'app.ui.' + i + '.controller'
		temp_blueprint = i + '_blueprint'
		temp_import = 'from ' + temp_controller + ' import ' + temp_blueprint
		temp_blueprint_register = 'app.register_blueprint(' + temp_blueprint + ')'

		# Import ui controllers
		exec(temp_import)

		# regiser ui blueprint
		exec(temp_blueprint_register)

# Create corresponding tables
db.create_all()