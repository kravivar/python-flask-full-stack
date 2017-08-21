from flask import Blueprint, render_template

# Define api blueprint
home_blueprint = Blueprint('home_blueprint', __name__, url_prefix='/home/')

@home_blueprint.route("/")
def home():
	return render_template("home.html")