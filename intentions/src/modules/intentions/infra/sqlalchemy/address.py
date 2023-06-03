from datetime import datetime
from shared.infra.db.sqlalchemy import sqlalchemy as db

class Address(db.Model):
  address_id = db.Column(db.Integer, primary_key=True)
  country = db.Column(db.String(64), nullable=False)
  state = db.Column(db.String(64), nullable=False)
  city = db.Column(db.String(64), nullable=False)
  street = db.Column(db.Text, nullable=False)
  number = db.Column(db.Integer, nullable=False)
  apartment = db.Column(db.Integer, nullable=True)
  complement = db.Column(db.Text, nullable=True)
  client_id = db.Column(db.Integer, db.ForeignKey('client.client_id'), nullable=False)
  created_at = db.Column(db.DateTime, default=datetime.utcnow)
  updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
