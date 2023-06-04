from  modules.intentions.infra.sqlalchemy.repositories.intention_repository import IntentionRepository

class CreateIntention():
  def execute():
    intention_created = IntentionRepository.create()
    return intention_created
