
from flask import Blueprint, jsonify
from flask_restx import Namespace, Resource, fields

ns = Namespace('Adresses', description='Rotas relacionadas para processar endereços')

create_adress_request_body = ns.model(
  "CreateAdressRequestBody",
  {
    "country": fields.String(example='Brasil', required=True, description="País em que o cliente reside"),
    "state": fields.String(example='Bahia', required=True, description="Estado em que o cliente reside"),
    "city": fields.String(example='Salvador', required=True, description="Cidade em que o cliente reside"),
    "street": fields.String(example='Rua E', required=True, description="Rua em que o cliente reside"),
    "number": fields.Integer(example=54, required=True, description="Número da casa/prédio em que o cliente reside"),
    "apartment": fields.Integer(example=201, required=False, description="Número do apartamento em que o cliente reside"),
    "complement": fields.String(example='Perto da padaria Empadaria', required=False, description="Complemento"),
  }
)

update_adress_request_body = ns.model(
  "UpdateAdressRequestBody",
  {
    "country": fields.String(example='Brasil', required=False, description="País em que o cliente reside"),
    "state": fields.String(example='Bahia', required=False, description="Estado em que o cliente reside"),
    "city": fields.String(example='Salvador', required=False, description="Cidade em que o cliente reside"),
    "street": fields.String(example='Rua E', required=False, description="Rua em que o cliente reside"),
    "number": fields.Integer(example=54, required=False, description="Número da casa/prédio em que o cliente reside"),
    "apartment": fields.Integer(example=201, required=False, description="Número do apartamento em que o cliente reside"),
    "complement": fields.String(example='Perto da padaria Empadaria', required=False, description="Complemento"),
  }
)

@ns.route('/')
class Adresses(Resource):
  @ns.doc(body=create_adress_request_body)
  def post(self):
    data = {
      'message': 'Hello World!',
    }
    return jsonify(data)

@ns.route('/<adress_id>/')
class Adress(Resource):
  @ns.doc(body=update_adress_request_body)
  def put(self):
    data = {
      'message': 'Hello World!',
    }
    return jsonify(data)
