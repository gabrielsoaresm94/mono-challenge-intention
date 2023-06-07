from  modules.intentions.infra.sqlalchemy.repositories.intention_repository import IntentionRepository

class ListIntentions():
  def execute():
    intentions_listed = IntentionRepository.list()
    return intentions_listed
