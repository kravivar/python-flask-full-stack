# Importing Flask and dependencies
from flask import Blueprint, jsonify, request, make_response
from flask_restx import Resource, abort
from app.api import api
import os

# Import model and db
from app import db
from app.api.developer.model import Developer, DeveloperSchema, DeveloperRestSchema

# Defining namespace
developer_namespace = api.namespace(os.path.basename(os.path.dirname(os.path.realpath(__file__))), 
									description='Manage developers.')

## Defining reoutes
@developer_namespace.route('/<int:id>')
class DeveloperApiOne(Resource):
	def get(self, id):
		if id is None:
			abort(400)
		developer_data = Developer.query.get(id)
		developer_schema = DeveloperSchema()
		retval = developer_schema.dump(developer_data)
		return jsonify(retval)

	@api.expect(DeveloperRestSchema)
	def put(self, id):
		if id is None:
			abort(400)
		
		if not request.json or not 'name' in request.json:
			abort(400)

		input_data = request.json
		developer_data = Developer.query.get(id)

		for i in input_data:
			eval_update = 'developer_data.' + i + ' = input_data["' + i + '"]'
			exec(eval_update)

		db.session.commit()
		return jsonify( { 'result': True } )

	def delete(self, id):
		if id is None:
			abort(400)		
		db.session.delete(Developer.query.get(id))
		db.session.commit()
		return jsonify( { 'result': True } )

@developer_namespace.route('/')
class DeveloperApi(Resource):
	def get(self):
		id = None
		if not request.args:
			developer_data = Developer.query.all()
		else:
			kwargs = request.args
			developer_data = Developer.query.filter_by(**kwargs)

		developer_schema = DeveloperSchema(many=True)
		retval = developer_schema.dump(developer_data)
		return jsonify(retval)

	@api.expect(DeveloperRestSchema)
	def post(self):
		kwargs = request.json
		if not request.json or not 'name' in request.json:
			abort(400)
		# developer_data = Developer(request.json.get('name'), request.json.get('hireDate', ''), request.json.get('focus',''))
		developer_data = Developer(**kwargs)
		db.session.add(developer_data)
		db.session.commit()

		developer_schema = DeveloperSchema()
		retval = developer_schema.dump(developer_data)
		return make_response(jsonify(retval), 201)