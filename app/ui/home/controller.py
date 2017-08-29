from flask import Blueprint, render_template, jsonify
from app import app

# Define api blueprint
home_blueprint = Blueprint('home_blueprint', __name__)

@home_blueprint.route("/static/<filename>")
def index():
	return send_from_directory(app.config["BOWER_STATIC"], filename)

@home_blueprint.route("/")
def home():
	# return jsonify(app.config["BOWER_STATIC"])
	return render_template("home.html")	