from  modules.addresses.infra.sqlalchemy.repositories.address_repository import AddressRepository

class UpdateAddress():
  def execute():
    update_created = AddressRepository.update()
    return update_created
