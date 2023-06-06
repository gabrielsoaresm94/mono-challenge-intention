from  modules.clients.infra.sqlalchemy.repositories.client_repository import ClientRepository

class CreateClient():
  def execute(client_name):
    found_client_by_name = ClientRepository.find_by_name(client_name)

    if found_client_by_name["status"] == True:
      client_found = {
        'message': 'Já existe um cliente com esse nome!',
        'status': False,
      }
      return client_found

    client_created = ClientRepository.create(client_name)
    found_client_by_name = ClientRepository.find_by_name(client_name)

    data_return = {
      'message': client_created["message"],
      'status': True,
      'data': found_client_by_name["data"]
    }

    return data_return
