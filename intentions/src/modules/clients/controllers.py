
from flask import jsonify
from flask_restx import Namespace, Resource, fields

ns = Namespace('Clients', description='Rotas relacionadas para processar clientes')

client_request_body = ns.model(
  "ClientRequestBody",
  {
    "name": fields.String(required=True, description="Nome do cliente"),
  }
)

client_response = ns.model(
  "ClientResponse",
  {
    "client_id": fields.String(required=True, description="Identificador do cliente"),
    "name": fields.String(required=True, description="Nome do cliente"),
  }
)

@ns.route('/')
class Clients(Resource):
  @ns.doc(body=client_request_body)
  def post(self):
    data = {
      'message': 'Hello World!',
    }
    return jsonify(data)
