from app import db
import datetime
from marshmallow_sqlalchemy import ModelSchema

# Base Schema for sqlAlchemy
class Base(db.Model):
	__abstract__  = True

	id = db.Column(db.Integer, primary_key=True)
	date_created  = db.Column(db.DateTime,  default=db.func.current_timestamp())
	date_modified = db.Column(db.DateTime,  default=db.func.current_timestamp(),
											onupdate=db.func.current_timestamp())

# Model Class for sqlAlchemy
class Developer(Base):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(20))
	hireDate = db.Column(db.DateTime,  default=db.func.current_timestamp())
	focus = db.Column(db.String(50))

	def __init__(self, name, hireDate, focus):
		self.name = name
		self.hireDate = datetime.datetime.strptime(hireDate, '%Y-%m-%d').date()
		self.focus = focus

# Model Class for marshmallows
class DeveloperSchema(ModelSchema):
	class Meta:
		model = Developer
