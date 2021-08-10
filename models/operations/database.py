from sqlalchemy.exc import SQLAlchemyError

from database import database


# TODO: As principais operações do banco de dados, dentro de um model são as abaixo.

def begin_transaction():
    try:
        database.session.begin()
        return True

    except SQLAlchemyError:
        return False


def commit():
    try:
        database.session.begin()
        return True

    except SQLAlchemyError:
        rollback()
        return False


def rollback():
    database.session.rollback()
