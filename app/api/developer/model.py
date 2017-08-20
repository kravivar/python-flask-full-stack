# Defining Developer model for table

from app import db
from app.api import api
import datetime
from flask_restplus import fields
from flask_marshmallow import Marshmallow

ma = Marshmallow()

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
class DeveloperSchema(ma.ModelSchema):
	class Meta:
		model = Developer

# Model for restplus
DeveloperRestSchema=api.model('Developer',{
	'id': fields.Integer(),
	'date_created': fields.Date(),
	'data_modified': fields.Date(),
	'name': fields.String(),
	'hireDate': fields.Date(),
	'focus': fields.String(),
})
