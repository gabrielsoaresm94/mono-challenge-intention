import os
from dotenv import load_dotenv
from flask import Flask, Blueprint, jsonify
from flask_restx import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
from shared.infra.db.sqlalchemy import sqlalchemy as db

from modules.intentions.controllers import ns as intentions_ns
from modules.clients.controllers import ns as clients_ns
from modules.adresses.controllers import ns as adresses_ns

from modules.intentions.infra.sqlalchemy.client import Client
from modules.intentions.infra.sqlalchemy.address import Address
from modules.intentions.infra.sqlalchemy.intention import Intention
from modules.intentions.infra.sqlalchemy.intention_product import IntentionProduct

db_user = os.getenv("CHALLENGE_INTENTION_DB_USER")
db_password = os.getenv("CHALLENGE_INTENTION_DB_PASSWORD")
db_name = os.getenv("CHALLENGE_INTENTION_DB_NAME")

def create_app():
  app = Flask(__name__)
  load_dotenv()

  @app.route("/", methods=["GET"])
  def home():
    return jsonify({"success": True})

  app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{db_user}:{db_password}@challenge-intention-db:5432/{db_name}'
  app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
  app.secret_key = 'Codebrains'
  return app

app = create_app()

blueprint = Blueprint("/docs/", __name__)
api = Api(
  blueprint,
  doc='/docs/',
  version='1.0',
  title='Intentions Service API',
  description='A service of purchase intentions'
)

db.init_app(app)

migrate = Migrate(app, db)

api.add_namespace(intentions_ns, path="/intentions")
api.add_namespace(clients_ns, path="/clients")
api.add_namespace(adresses_ns, path="/adresses")

app.register_blueprint(blueprint, url_prefix="/v1")

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000, debug=True, use_reloader=True)
