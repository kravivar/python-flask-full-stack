# Statement for enabling the development environment
DEBUG = True

# Define the application directory
import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))  

class BaseConfig():
	# Application threads. A common general assumption is
	# using 2 per available processor cores - to handle
	# incoming requests using one and performing background
	# operations using the other.

	THREADS_PER_PAGE = 2

	# Enable protection agains *Cross-site Request Forgery (CSRF)*
	CSRF_ENABLED     = True

	# Use a secure, unique and absolutely secret key for
	# signing the data. 
	CSRF_SESSION_KEY = "secret"

	# Secret key for signing cookies
	SECRET_KEY = "secret"

	ENABLED_MODULES = {
		'developer'
	}
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	JSONIFY_PRETTYPRINT_REGULAR = False


class DevelopmentConfig(BaseConfig):
	DEBUG = True
	SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/flask.db'
	DATABASE_CONNECT_OPTIONS = {}

class StageConfig(BaseConfig):
	# Define the database - we are working with
	# SQLite for this example

	DATABASE_USER = 'root'
	DATABASE_PASSWORD = 'password'
	DATABASE_DB = 'flask'
	DATABASE_HOST = 'mysql'
	SQLALCHEMY_DATABASE_URI = 'mysql+pymysql' + '://' + DATABASE_USER + ':' + DATABASE_PASSWORD + '@' + DATABASE_HOST + '/' + DATABASE_DB
