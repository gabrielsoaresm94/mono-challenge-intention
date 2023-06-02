
from flask import Blueprint, jsonify
from flask_restx import Api, Resource

intentions_module = Blueprint('/', __name__)
api = Api(
  intentions_module,
  version='1.0',
  title='Intentions Service API',
  description='A service of purchase intentions',
)

ns = api.namespace('')

@ns.route('/intentions/')
class HelloWorld(Resource):
  def get(self):
    data = {
      'message': 'Hello World!',
    }
    return jsonify(data)
