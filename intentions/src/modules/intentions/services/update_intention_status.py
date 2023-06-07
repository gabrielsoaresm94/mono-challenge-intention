from  modules.intentions.infra.sqlalchemy.repositories.intention_repository import IntentionRepository

class UpdateIntentionStatus():
  def execute(intention_id, intention_status, ):
    intention_created = IntentionRepository.update_status(intention_id, intention_status)
    found_intention = IntentionRepository.find(intention_id)

    data_return = {
      'message': "Intenção de atualizada com sucesso!",
      'status': True,
      'data': found_intention
    }

    return data_return
