# Defining Developer model for table

from app import db
from app.api import api
import datetime
from flask_restx import fields
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
	focus = db.Column(db.String(50))

	def __init__(self, name, focus):
		self.name = name
		self.focus = focus

# Model Class for marshmallows
class DeveloperSchema(ma.SQLAlchemyAutoSchema):
	class Meta:
		model = Developer

class DeveloperReturnSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Developer
        # Exclude date_created because we're aliasing it below
        exclude = ("name", "focus")		

# Model for restplus
DeveloperRestSchema=api.model('Developer',{
	'name': fields.String(),
	'focus': fields.String(),
})
