
from flask import Blueprint, jsonify
from flask_restx import Namespace, Resource

ns = Namespace('Intentions', description='Rotas relacionadas para processar intenções')

@ns.route('/')
class Intentions(Resource):
  @ns.doc("list_intentions")
  def get(self):
    data = {
      'message': 'Hello World!',
    }
    return jsonify(data)
  def post(self):
    data = {
      'message': 'Hello World!',
    }
    return jsonify(data)

@ns.route('/<intention_id>/')
class Intention(Resource):
  def put(self):
    data = {
      'message': 'Hello World!',
    }
    return jsonify(data)
