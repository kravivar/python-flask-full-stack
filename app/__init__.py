from flask import Flask, jsonify, abort, request
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api, Resource

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

# Route Definitions
# Import a module / component using its blueprint handler variable (mod_auth)
from app.developer.controller import app_developer

# Register blueprint(s)
app.register_blueprint(app_developer)

# Create corresponding tables
db.create_all()