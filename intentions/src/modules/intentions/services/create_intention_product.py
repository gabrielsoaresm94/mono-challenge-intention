from modules.intentions.infra.sqlalchemy.repositories.intention_product_repository import IntentionProductRepository

class CreateIntentionProduct():
  def execute(intention_id, intention_product_data):
    intention_product_created = IntentionProductRepository.create(intention_id, intention_product_data)
    list_intention_product_by_intention_id = IntentionProductRepository.list_by_intention_id(intention_id)

    list_intention_product = list_intention_product_by_intention_id["data"]
    last_intention_product = max(list_intention_product, key=lambda intention_product: intention_product['intention_product_id'])

    data_return = {
      'message': "Produto de intenção de compra salvo com sucesso!",
      'status': True,
      'data': last_intention_product
    }

    return data_return
