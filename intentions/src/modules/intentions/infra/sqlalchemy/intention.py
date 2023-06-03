from datetime import datetime
from shared.infra.db.sqlalchemy import sqlalchemy as db

class Intention(db.Model):
  intention_id = db.Column(db.Integer, primary_key=True)
  client_id = db.Column(db.Integer, db.ForeignKey('client.client_id'), nullable=False)
  address_id = db.Column(db.Integer, db.ForeignKey('address.address_id'), nullable=False)
  created_at = db.Column(db.DateTime, default=datetime.utcnow)
  updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
