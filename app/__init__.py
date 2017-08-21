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

# Import api blueprint
from app.api import api_blueprint
from app.ui.home.controller import home_blueprint

# register 
app.register_blueprint(api_blueprint)
app.register_blueprint(home_blueprint)

# Create corresponding tables
db.create_all()