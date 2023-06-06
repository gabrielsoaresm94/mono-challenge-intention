from shared.infra.db.sqlalchemy import sqlalchemy as db
from modules.addresses.infra.sqlalchemy.entities.address import Address

class AddressRepository():
  def create(address_data, client_id):
    try:
      apartment = None
      complement = None
      if 'apartment' in address_data:
        apartment = address_data["apartment"]
      if 'complement' in address_data:
        complement = address_data["complement"]
      address = Address(
        country = address_data["country"],
        state = address_data["state"],
        city = address_data["city"],
        street = address_data["street"],
        number = address_data["number"],
        apartment = apartment,
        complement = complement,
        client_id = client_id
      )
      db.session.add(address)
      db.session.commit()
      data = {
        'message': 'Endereço criado com sucesso!',
        'status': True
      }
      return data
    except Exception as exception:
      db.session.rollback()
      raise exception
  def list_by_client_id(client_id):
    try:
      addresses = Address.query.filter_by(client_id=client_id).all()
      if addresses is None:
        no_data = {
          'message': 'Cliente ainda não tem nenhum endereço cadastrado!',
          'status': False,
        }
        return no_data
      data = {
        'message': 'Endereço(s) retornado(s) com sucesso!',
        'status': True,
        'data': [address.to_dict() for address in addresses]
      }
      return data
    except Exception as exception:
      db.session.rollback()
      raise exception
  def update():
    data = {
      'message': 'Endereço atualizado com sucesso!',
    }
    return data
