from shared.infra.db.sqlalchemy import sqlalchemy as db
from modules.clients.infra.sqlalchemy.entities.client import Client

class ClientRepository():
  def create(client_name):
    try:
      client = Client(name = client_name)
      db.session.add(client)
      db.session.commit()
      data = {
        'message': 'Cliente criado com sucesso!',
        'status': True
      }
      return data
    except Exception as exception:
      db.session.rollback()
      raise exception
  def find_by_name(client_name):
    try:
      client = Client.query.filter_by(name=client_name).first()

      if client is None:
        no_data = {
          'message': 'Ainda não foi criado cliente com esse nome!',
          'status': False,
        }
        return no_data

      data = {
        'message': 'Cliente retornado com sucesso!',
        'status': True,
        'data': client.to_dict()
      }
      return data
    except Exception as exception:
      db.session.rollback()
      raise exception
