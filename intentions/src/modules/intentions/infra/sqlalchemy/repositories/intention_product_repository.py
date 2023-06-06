from shared.infra.db.sqlalchemy import sqlalchemy as db
from modules.intentions.infra.sqlalchemy.entities.intention import Intention
from modules.intentions.infra.sqlalchemy.entities.intention_product import IntentionProduct

class IntentionRepository():
  def create(product_data, intention_id):
    try:
      intention_product = IntentionProduct(
        product_id = product_data["product_id"],
        title = product_data["title"],
        price = product_data["price"],
        category = product_data["category"],
        description = product_data["description"],
        image = product_data["image"],
        quantity = None,
        intention_id = intention_id
      )
      db.session.add(intention_product)
      db.session.commit()
      data = {
        'message': 'Produto de intenção de compra salvo com sucesso!',
        'status': True
      }
      return data
    except Exception as exception:
      db.session.rollback()
      raise exception
  def list():
    try:
      intention_products = IntentionProduct.query.all()
      if intention_products is None:
        no_data = {
          'message': 'Nenhum produto da intenção de compra encontrado!',
          'status': False,
        }
        return no_data
      data = {
        'message': 'Produtos de intenção de compra listados com sucesso!',
        'status': True,
        'data': [intention_product.to_dict() for intention_product in intention_products]
      }
      return data
    except Exception as exception:
      db.session.rollback()
      raise exception
