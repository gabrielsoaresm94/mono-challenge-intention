from  modules.addresses.infra.sqlalchemy.repositories.address_repository import AddressRepository

class ListAddressesByClientId():
  def execute(client_id):
    data_return = AddressRepository.list_by_client_id(client_id)
    return data_return
