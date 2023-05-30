from flask import Flask
from flask import jsonify
from flask_restx import Api, Resource

app = Flask(__name__)
api = Api(
  app,
  version='1.0',
  title='Intentions Service API',
  description='A service of purchase intentions',
)

# ns = api.namespace('intentions')

@api.route('/v1/hello')
class HelloWorld(Resource):
  def get(self):
    data = {
      'message': 'Hello World!',
    }
    return jsonify(data)

# if __name__ == '__main__':
#     app.run(debug=True)

app.run(host='0.0.0.0', port=5000, debug=True, use_reloader=True)
