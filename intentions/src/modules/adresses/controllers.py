
from flask import Blueprint, jsonify
from flask_restx import Namespace, Resource

ns = Namespace('Adresses', description='Rotas relacionadas para processar endereços')

@ns.route('/')
class Adresses(Resource):
  def post(self):
    data = {
      'message': 'Hello World!',
    }
    return jsonify(data)

@ns.route('/<adress_id>/')
class Adress(Resource):
  def put(self):
    data = {
      'message': 'Hello World!',
    }
    return jsonify(data)
