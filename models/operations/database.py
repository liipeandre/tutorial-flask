from database import database


# TODO: As principais operações do banco de dados, dentro de um model são as abaixo.

def begin_transaction():
    database.session.begin()


def commit():
    database.session.commit()


def rollback():
    database.session.rollback()
