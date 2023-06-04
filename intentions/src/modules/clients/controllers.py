
from flask import jsonify
from flask_restx import Namespace, Resource, fields
from  modules.clients.services.create_client import CreateClient

ns = Namespace('Clients', description='Rotas relacionadas para processar clientes')

create_client_request_body = ns.model(
  "CreateClientRequestBody",
  {
    "name": fields.String(example='Fulano', required=True, description="Nome do cliente"),
    "country": fields.String(example='Brasil', required=True, description="País em que o cliente reside"),
    "state": fields.String(example='Bahia', required=True, description="Estado em que o cliente reside"),
    "city": fields.String(example='Salvador', required=True, description="Cidade em que o cliente reside"),
    "street": fields.String(example='Rua E', required=True, description="Rua em que o cliente reside"),
    "number": fields.Integer(example=54, required=True, description="Número da casa/prédio em que o cliente reside"),
    "apartment": fields.Integer(example=201, required=False, description="Número do apartamento em que o cliente reside"),
    "complement": fields.String(example='Perto da padaria Empadaria', required=False, description="Complemento"),
  }
)

return_client_response = ns.model(
  "ReturnClientResponse",
  {
    "client_id": fields.String(example=1, required=True, description="Identificador do cliente"),
    "name": fields.String(example='Fulano', required=True, description="Nome do cliente"),
  }
)

@ns.route('/')
class Clients(Resource):
  @ns.doc(body=create_client_request_body)
  def post(self):
    client_created = CreateClient.execute()
    return jsonify(client_created)
