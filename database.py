from os import getcwd
from app import app

from flask_sqlalchemy import SQLAlchemy


def get_connection():
    file_dir = getcwd()

    # TODO: Editar a URI de acesso ao banco de dados, caso necessário.
    uri = "{database_type}:///{database_name}".format(
        database_type='sqlite',
        database_name=file_dir + '/database/database.db'
    )

    app.config['SQLALCHEMY_DATABASE_URI'] = uri

    database = SQLAlchemy(app)

    return database


def execute_sql_query(query: str, parameters: dict):
    try:
        data = database.session.execute(query, parameters)
        return True, data

    except Exception as exception:
        rollback()
        return False, []


def commit():
    try:
        database.session.commit()
        return True

    except Exception as exception:
        rollback()
        return False


def rollback():
    database.session.rollback()


database = get_connection()
