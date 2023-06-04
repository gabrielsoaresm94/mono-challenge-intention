from  modules.adresses.infra.sqlalchemy.repositories.adress_repository import AdressRepository

class UpdateAdress():
  def execute():
    update_created = AdressRepository.update()
    return update_created
