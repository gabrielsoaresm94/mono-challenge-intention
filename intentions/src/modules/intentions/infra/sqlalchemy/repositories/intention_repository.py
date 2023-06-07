# from flask_sqlalchemy import text
from shared.infra.db.sqlalchemy import sqlalchemy as db
from modules.intentions.infra.sqlalchemy.entities.intention import Intention

class IntentionRepository():
  def create(client_id, address_id):
    try:
      intention = Intention(
        status = "EM_SELECAO",
        client_id = client_id,
        address_id = address_id
      )
      db.session.add(intention)
      db.session.commit()
      data = {
        'message': 'Intenção de compra criada com sucesso!',
        'status': True
      }
      return data
    except Exception as exception:
      db.session.rollback()
      raise exception
  def update_status(intention_id, intention_status):
    try:
      intention = Intention.query.filter_by(intention_id=intention_id).all()
      if intention is None:
        no_data = {
          'message': 'Nenhuma intenção de compra encontrada!',
          'status': False,
        }
        return no_data
      intention_updated = db.update(Intention).where(Intention.intention_id == intention_id).values(status=intention_status)
      db.session.execute(intention_updated)
      db.session.commit()
      data = {
        'message': 'Intenção de compra atualizada com sucesso!',
        'status': True
      }
      return data
    except Exception as exception:
      db.session.rollback()
      raise exception
  def list_by_client_id(client_id):
    try:
      intentions = Intention.query.filter_by(client_id=client_id).all()
      if intentions is None:
        no_data = {
          'message': 'Nenhuma intenção de compra encontrada!',
          'status': False,
        }
        return no_data
      data = {
        'message': 'Intenções de compra listadas com sucesso!',
        'status': True,
        'data': [intention.to_dict() for intention in intentions]
      }
      return data
    except Exception as exception:
      db.session.rollback()
      raise exception
  def list():
    try:
      intentions = Intention.query.all()
      if intentions is None:
        no_data = {
          'message': 'Nenhuma intenção de compra encontrada!',
          'status': False,
        }
        return no_data
      data = {
        'message': 'Intenções de compra listadas com sucesso!',
        'status': True,
        'data': [intention.to_dict() for intention in intentions]
      }
      return data
    except Exception as exception:
      db.session.rollback()
      raise exception
  def find(intention_id):
    try:
      intention = Intention.query.filter_by(intention_id=intention_id).all()
      if intention is None:
        no_data = {
          'message': 'Nenhuma intenção de compra encontrada!',
          'status': False,
        }
        return no_data
      data = {
        'message': 'Intenções de compra encontrada com sucesso!',
        'status': True,
        'data': intention
      }
      return data
    except Exception as exception:
      db.session.rollback()
      raise exception
