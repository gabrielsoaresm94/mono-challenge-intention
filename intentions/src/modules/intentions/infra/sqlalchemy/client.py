from datetime import datetime
from shared.infra.db.sqlalchemy import sqlalchemy as db

class Client(db.Model):
  client_id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(128), nullable=False)
  created_at = db.Column(db.DateTime, default=datetime.utcnow)
  updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
