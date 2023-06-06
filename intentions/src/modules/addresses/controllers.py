
from flask import Blueprint, jsonify
from flask_restx import Namespace, Resource, fields
from  modules.addresses.services.create_address import CreateAddress

ns = Namespace('Addresses', description='Rotas relacionadas para processar endereços')

create_address_request_body = ns.model(
  "CreateAddressRequestBody",
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

update_address_request_body = ns.model(
  "UpdateAddressRequestBody",
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
class Addresses(Resource):
  @ns.doc(body=create_address_request_body)
  def post(self):
    address_created = CreateAddress.execute()
    return jsonify(address_created)
