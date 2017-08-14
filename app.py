#!/usr/bin/env python

from flask import Flask
from flask_restful import Api, reqparse, abort, Resource, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./main.db'

db = SQLAlchemy(app)

api = Api(app)

parser = reqparse.RequestParser()

class Todo(db.Model):
    __tablename__ = 'todos'

    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(255))

todo_fields = {
    'id': fields.Integer,
    'task': fields.String,
    'uri': fields.Url('todo', absolute=True),
}

parser.add_argument('task', type=str)

class TodoResource(Resource):
    @marshal_with(todo_fields)
    def get(self, id):
        todo = db.session.query(Todo).filter(Todo.id == id).first()
        if not todo:
            abort(404, message="Todo {} doesn't exist".format(id))
        return todo

    def delete(self, id):
        todo = db.session.query(Todo).filter(Todo.id == id).first()
        if not todo:
            abort(404, message="Todo {} doesn't exist".format(id))
        db.session.delete(todo)
        db.session.commit()
        return {}, 204

    @marshal_with(todo_fields)
    def put(self, id):
        parsed_args = parser.parse_args()
        todo = db.session.query(Todo).filter(Todo.id == id).first()
        todo.task = parsed_args['task']
        db.session.add(todo)
        db.session.commit()
        return todo, 201


class TodoListResource(Resource):
    @marshal_with(todo_fields)
    def get(self):
        todos = db.session.query(Todo).all()
        return todos

    @marshal_with(todo_fields)
    def post(self):
        parsed_args = parser.parse_args()
        todo = Todo(task=parsed_args['task'])
        db.session.add(todo)
        db.session.commit()
        return todo, 201


api.add_resource(TodoListResource, '/todos', endpoint='todos')
api.add_resource(TodoResource, '/todos/<string:id>', endpoint='todo')

if __name__ == '__main__':
	db.create_all()
	app.run(debug=True, host='0.0.0.0')