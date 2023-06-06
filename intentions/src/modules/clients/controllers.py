
from flask import jsonify, request
from flask_restx import Namespace, Resource, fields
from  modules.clients.services.create_client import CreateClient
from  modules.addresses.services.create_address import CreateAddress

ns = Namespace('Clients', description='Rotas relacionadas para processar clientes')

address = ns.model(
  "Address",
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

create_client_request_body = ns.model(
  "CreateClientRequestBody",
  {
    "name": fields.String(example='Fulano', required=True, description="Nome do cliente"),
    "address": fields.Nested(address, required=True, description="Endereço do cliente")
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
    json_data = request.get_json()

    if not json_data:
      return {"message": "O corpo não pode ser um objeto vazio!"}, 400

    client_data = request.get_json(force=True)
    if client_data.get("name") is None:
      return {"message": "Campo 'name' é obrigatório!"}, 400

    if client_data.get("address") is None:
      return {"message": "Campo 'address' é obrigatório!"}, 400

    client_name = client_data.get("name")
    client_return = CreateClient.execute(client_name)

    if client_return["status"] != True:
      return jsonify(client_return)

    client_address = client_data.get("address")
    client_address_without_null_values = {key: value for key, value in client_address.items() if value is not None}
    client_id = client_return["data"]["client_id"]
    address_return = CreateAddress.execute(client_address_without_null_values, client_id)

    client_return["data"]["address"] = address_return["data"]

    return jsonify(client_return)
