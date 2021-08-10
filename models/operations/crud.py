from database import database
from sqlalchemy.exc import SQLAlchemyError

# TODO: As principais operações de dados, dentro de um model são as abaixo.

def insert(registry):
    try:
        database.session.add(registry)
        return True

    except SQLAlchemyError:
        return False


def delete(registry):
    try:
        database.session.delete(registry)
        return True

    except SQLAlchemyError:
        return False


def list(model: database.Model):
    try:
        return model.query.all()

    except SQLAlchemyError as error:
        return None

def view(model: database.Model, id):
    try:
        return model.query.get(id)

    except SQLAlchemyError:
        return None


def edit(model: database.Model, fields):
    try:
        registry = view(model, fields['id'])

        for key, value in zip(fields.keys, fields.values):
            setattr(registry, str(key), value)

        insert(registry)

        return True

    except SQLAlchemyError:
        return False
