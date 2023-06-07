from  modules.intentions.infra.sqlalchemy.repositories.intention_repository import IntentionRepository

class CreateIntention():
  def execute(client_id, address_id, products_ids):
    # intention_created = IntentionRepository.create(client_id, address_id)
    list_intention_by_client_id = IntentionRepository.list_by_client_id(client_id)

    list_intentions = list_intention_by_client_id["data"]
    last_intention = max(list_intentions, key=lambda intention: intention['intention_id'])

    data_return = {
      'message': "Intenção de compra criada com sucesso!",
      'status': True,
      'data': last_intention
    }

    data_to_send_to_products_service = {
      'intention_id': data_return["data"]["intention_id"],
      'products': products_ids
    }

    url = "http://products-service:3001/v1/intentions/" + str(last_intention["intention_id"]) +"/"
    # request_provider("post", url, None, jsonify(data_to_send_to_products_service))

    return data_return
