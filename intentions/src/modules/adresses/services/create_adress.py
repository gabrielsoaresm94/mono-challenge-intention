from  modules.adresses.infra.sqlalchemy.repositories.adress_repository import AdressRepository

class CreateAdress():
  def execute():
    adress_created = AdressRepository.create()
    return adress_created
