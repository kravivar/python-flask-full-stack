from flask import Flask, jsonify, abort, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

# Import api blueprint
from app.api import api_blueprint

# register 
app.register_blueprint(api_blueprint)

# Create corresponding tables
db.create_all()