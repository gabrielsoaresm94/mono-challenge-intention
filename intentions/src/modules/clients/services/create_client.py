from  modules.clients.infra.sqlalchemy.repositories.client_repository import ClientRepository

class CreateClient():
  def execute():
    client_created = ClientRepository.create()
    return client_created
