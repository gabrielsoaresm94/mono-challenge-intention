from modules.intentions.infra.sqlalchemy.repositories.intention_product_repository import IntentionProductRepository

class ListIntentionProducts():
  def execute(intention_id):
    intentions_listed = IntentionProductRepository.list_by_intention_id(intention_id)
    return intentions_listed
