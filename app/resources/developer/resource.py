# Importing Flask and dependencies
from flask import jsonify, request, make_response
from flask_restful import Resource, abort, reqparse
from app import db

# Import model
from app.resources.developer.model import Developer, DeveloperSchema

class DeveloperApi(Resource):
	"""
	This is the language awesomeness API
	Call this api passing a language name and get back its features
	---
	tags:
	  - Awesomeness Language API
	parameters:
	  - name: language
	    in: path
	    type: string
	    required: true
	    description: The language name
	  - name: size
	    in: query
	    type: integer
	    description: size of awesomeness
	responses:
	  500:
	    description: Error The language is not awesome!
	  200:
	    description: A language with its awesomeness
	    schema:
	      id: awesome
	      properties:
	        language:
	          type: string
	          description: The language name
	          default: Lua
	        features:
	          type: array
	          description: The awesomeness list
	          items:
	            type: string
	          default: ["perfect", "simple", "lovely"]

	"""
	def get(self):
		id = None
		if not request.args:
			developer_data = Developer.query.all()
		else:
			kwargs = request.args
			developer_data = Developer.query.filter_by(**kwargs)

		developer_schema = DeveloperSchema(many=True)
		retval = developer_schema.dump(developer_data).data
		return jsonify({'retval':retval,'args':request.args})

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