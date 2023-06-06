
from flask import Blueprint, jsonify
from flask_restx import Namespace, Resource, fields
from  modules.intentions.services.create_intention import CreateIntention
from  modules.intentions.services.list_intentions import ListIntentions

ns = Namespace('Intentions', description='Rotas relacionadas para processar intenções')

create_intention_request_body = ns.model(
  "CreateIntentionsRequestBody",
  {
    "client_id": fields.Integer(example=1, required=True, description="Identificador do cliente"),
    "address_id": fields.Integer(example=1, required=True, description="Identificador do endereço"),
    'products': fields.List(fields.Integer, example=[1, 2, 3], required=True, description="Identificadores dos produtos, vindos da fake_api")
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
    "name": fields.String(example='Fulano', required=True, description="Nome do cliente"),
    "status": fields.String(example='SELECIONADO', required=True, description="Status da intenção de compra"),
    "country": fields.String(example='Brasil', required=True, description="País em que o cliente reside"),
    "state": fields.String(example='Bahia', required=True, description="Estado em que o cliente reside"),
    "city": fields.String(example='Salvador', required=True, description="Cidade em que o cliente reside"),
    "street": fields.String(example='Rua E', required=True, description="Rua em que o cliente reside"),
    "number": fields.Integer(example=54, required=True, description="Número da casa/prédio em que o cliente reside"),
    "apartment": fields.Integer(example=201, required=False, description="Número do apartamento em que o cliente reside"),
    "complement": fields.String(example='Perto da padaria Empadaria', required=False, description="Complemento"),
    "products": fields.List(fields.Nested(product), required=True, description="Dados dos produtos da intenção de compra")
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
    intention_created = CreateIntention.execute()
    return jsonify(intention_created)

# @ns.route('/<intention_id>/')
# class Intention(Resource):
#   def put(self):
#     data = {
#       'message': 'Hello World!',
#     }
#     return jsonify(data)
