import json
from flask import Blueprint, jsonify, request
from flask_restx import Namespace, Resource, fields
from modules.intentions.services.create_intention import CreateIntention
from modules.intentions.services.list_intentions import ListIntentions
from modules.addresses.services.list_address_by_client_id import ListAddressesByClientId
from modules.intentions.services.list_intention_products import ListIntentionProducts
from modules.intentions.services.update_intention_status import UpdateIntentionStatus
from modules.intentions.services.create_intention_product import CreateIntentionProduct
from shared.providers.request_http_provider.request_provider import request_provider

ns = Namespace('Intentions', description='Rotas relacionadas para processar intenções')

create_intention_request_body = ns.model(
  "CreateIntentionsRequestBody",
  {
    "client_id": fields.Integer(example=1, required=True, description="Identificador do cliente"),
    "address_id": fields.Integer(example=1, required=True, description="Identificador do endereço"),
    "products_ids": fields.List(fields.Integer, example=[1, 2, 3], required=True, description="Identificadores dos produtos, vindos da fake_api"),
  }
)

product = ns.model(
  "Product",
  {
    "intention_product_id": fields.Integer(example=1, required=True, description="Identificador do produto relacionado com a intenção de compra"),
    "product_id": fields.Integer(example=1, required=True, description="Identificador do produto, vindo da fake_api"),
    "title": fields.String(example="Fjallraven - Foldsack No. 1 Backpack, Fits 15 Laptops", required=True, description="Título do produto"),
    "price": fields.Float(example=109.95, required=True, description="Preço do produto"),
    "category": fields.String(example="men's clothing", required=True, description="Categoria do produto"),
    "description": fields.String(example="Your perfect pack for everyday use and walks in the forest. Stash your laptop (up to 15 inches) in the padded sleeve, your everyday", required=True, description="Descrição do produto"),
    "image": fields.String(example="https://fakestoreapi.com/img/81fPKd-2AYL._AC_SL1500_.jpg", required=True, description="URL da imagem do produto"),
  }
)

return_intention_response = ns.model(
  "ReturnIntentionResponse",
  {
    "intention_id": fields.String(example=1, required=True, description="Identificador da intenção de compra"),
    "status": fields.String(example='SELECIONADO', required=True, description="Status da intenção de compra"),
    "address_id": fields.Integer(example=1, required=True, description="Identificador do endereço"),
  }
)

update_intention_request_body = ns.model(
  "UpdateIntentionsRequestBody",
  {
    "intention_status": fields.String(example="SELECIONADO", required=True, description="Campo para atualizar o status da intenção"),
    "intention_products": fields.List(fields.Nested(product), required=True, description="Dados dos produtos da intenção de compra"),
  }
)

@ns.route('/')
class Intentions(Resource):
  @ns.response(200, 'Success', [return_intention_response])
  def get(self):
    intentions_listed = ListIntentions.execute()
    return jsonify(intentions_listed)
  @ns.doc(body=create_intention_request_body)
  def post(self):
    json_data = request.get_json()

    if not json_data:
      return {"message": "O corpo não pode ser um objeto vazio!", "status": False}, 400

    intention_data = request.get_json(force=True)
    if intention_data.get("client_id") is None:
      return {"message": "Campo 'client_id' é obrigatório!", "status": False}, 400

    if intention_data.get("address_id") is None:
      return {"message": "Campo 'address_id' é obrigatório!", "status": False}, 400

    if intention_data.get("products_ids") is None:
      return {"message": "Campo 'products_ids' é obrigatório!", "status": False}, 400

    client_id = intention_data.get("client_id")
    address_id = intention_data.get("address_id")
    products_ids = intention_data.get("products_ids")

    address_by_client_id = ListAddressesByClientId.execute(client_id)
    address_by_client_id_data = address_by_client_id["data"]
    address_found =[address for address in address_by_client_id_data if address["address_id"] == address_id]
    if len(address_found) <= 0:
      return {"message": "Impossível salvar uma intenção para um endereço que não foi cadastrado pelo cliente!"}, 400

    intention_return = CreateIntention.execute(client_id, address_id, products_ids)

    return jsonify(intention_return)

@ns.route('/<intention_id>/')
class Intention(Resource):
  @ns.doc(body=update_intention_request_body)
  def patch(self, intention_id):
    json_data = request.get_json()

    if not json_data:
      return {"message": "O corpo não pode ser um objeto vazio!", "status": False}, 400

    intention_data = request.get_json(force=True)
    if intention_data.get("intention_status") is None:
      return {"message": "Campo 'intention_status' é obrigatório!", "status": False}, 400

    if intention_data.get("intention_products") is None:
      return {"message": "Campo 'intention_products' é obrigatório!", "status": False}, 400

    intention_status = intention_data.get("intention_status")
    intention_products = intention_data.get("intention_products")

    intention_return = UpdateIntentionStatus.execute(intention_id, intention_status)

    intention_products_return = []
    for intention_product in intention_products:
      intention_product_return = CreateIntentionProduct.execute(intention_id, intention_product)
      intention_products_return.append(intention_product_return["data"])

    data_return = {
      'message': "Produtos da intenção de compra selecionados com sucesso!",
      'status': True,
      'data': intention_products_return
    }
    return jsonify(data_return)

@ns.route('/<intention_id>/products')
class IntentionProducts(Resource):
  @ns.response(200, 'Success', [product])
  def get(self, intention_id):
    intentions_listed = ListIntentionProducts.execute(intention_id)
    return jsonify(intentions_listed)
