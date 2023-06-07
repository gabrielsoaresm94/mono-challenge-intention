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

  def to_dict(self):
    return {
      'intention_product_id': self.intention_product_id,
      'product_id': self.product_id,
      'title': self.title,
      'price': self.price,
      'category': self.category,
      'description': self.description,
      'image': self.image,
      'quantity': self.quantity,
      'intention_id': self.intention_id,
      'created_at': self.created_at,
      'updated_at': self.updated_at
    }
