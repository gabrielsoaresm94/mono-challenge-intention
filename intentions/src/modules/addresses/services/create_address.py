from  modules.addresses.infra.sqlalchemy.repositories.address_repository import AddressRepository

class CreateAddress():
  def execute(address_data, client_id):
    address_created = AddressRepository.create(address_data, client_id)
    list_addresses_by_client_id = AddressRepository.list_by_client_id(client_id)

    list_addresses = list_addresses_by_client_id["data"]
    last_address = max(list_addresses, key=lambda address: address['address_id'])

    data_return = {
      'message': list_addresses_by_client_id["message"],
      'status': True,
      'data': last_address
    }

    return data_return
