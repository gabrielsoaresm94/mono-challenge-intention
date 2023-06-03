from datetime import datetime
from shared.infra.db.sqlalchemy import sqlalchemy as db

class IntentionProduct(db.Model):
  intention_product_id = db.Column(db.Integer, primary_key=True)
  product_id = db.Column(db.Integer, nullable=False)
  title = db.Column(db.String(256), nullable=False)
  price = db.Column(db.Double, nullable=False)
  category = db.Column(db.String(64), nullable=False)
  description = db.Column(db.Text, nullable=False)
  image = db.Column(db.String(128), nullable=False)
  quantity = db.Column(db.Integer, nullable=True)
  intention_id = db.Column(db.Integer, db.ForeignKey('intention.intention_id'), nullable=False)
  created_at = db.Column(db.DateTime, default=datetime.utcnow)
  updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
