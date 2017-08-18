from flask import Flask, jsonify, abort, request
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api, Resource
import os

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

# Auto generate Route Definitions
# Import a module / component using its blueprint handler variable (mod_auth)
dl = next(os.walk('app'))[1]

for i in dl:
	temp_controller = 'app.' + i + '.controller'
	temp_blueprint = 'app_' + i
	temp_import = 'from ' + temp_controller + ' import ' + temp_blueprint
	temp_blueprint_register = 'app.register_blueprint(' + temp_blueprint + ')'

	# Import controllers
	exec(temp_import)

	# regiser blueprint
	exec(temp_blueprint_register)

# Create corresponding tables
db.create_all()