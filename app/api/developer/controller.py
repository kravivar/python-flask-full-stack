# Importing Flask and dependencies
from flask import Blueprint, jsonify, request, make_response
from flask_restplus import Resource, abort
from app.api import api
import os

# Import model and db
from app import db
from app.api.developer.model import Developer, DeveloperSchema, DeveloperRestSchema

# Defining namespace
namespace_developer = api.namespace(os.path.basename(os.path.dirname(os.path.realpath(__file__))), 
									description='Manage developers.')

## Defining reoutes
@namespace_developer.route('/')
class DeveloperApi(Resource):
	def get(self):
		id = None
		if not request.args:
			developer_data = Developer.query.all()
		else:
			kwargs = request.args
			developer_data = Developer.query.filter_by(**kwargs)

		developer_schema = DeveloperSchema(many=True)
		retval = developer_schema.dump(developer_data).data
		return jsonify(retval)

	def post(self):
		json_data = request.json
		if not request.json or not 'name' in request.json:
			abort(400)
		developer_data = Developer(request.json.get('name'), request.json.get('hireDate', ''), request.json.get('focus',''))
		db.session.add(developer_data)
		db.session.commit()

		developer_schema = DeveloperSchema()
		retval = developer_schema.dump(developer_data)
		return make_response(jsonify(retval), 201)

	def put(self):
		id = None
		if request.args:
			id = request.args['id']
		if id is None:
			abort(400)

		return True

	def delete(self):
		id = None
		if request.args:
			id = request.args['id']
		if id is None:
			abort(400)		
		db.session.delete(Developer.query.get(id))
		db.session.commit()
		return jsonify( { 'result': True } )