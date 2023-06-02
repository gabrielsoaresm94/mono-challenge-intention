import os
from dotenv import load_dotenv
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
from shared.infra.db.sqlalchemy import sqlalchemy as db
from modules.intentions.controllers import intentions_module

db_user = os.getenv("CHALLENGE_INTENTION_DB_USER")
db_password = os.getenv("CHALLENGE_INTENTION_DB_PASSWORD")
db_name = os.getenv("CHALLENGE_INTENTION_DB_NAME")

def create_app():
  app = Flask(__name__)
  load_dotenv()
  app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{db_user}:{db_password}@db:5432/{db_name}'
  app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
  app.secret_key = 'Codebrains'
  return app

app = create_app()

db.init_app(app)

migrate = Migrate(app, db)

app.register_blueprint(intentions_module)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000, debug=True, use_reloader=True)
