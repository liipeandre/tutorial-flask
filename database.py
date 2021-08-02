from app import app

from flask_sqlalchemy import SQLAlchemy

# TODO: Preencher os campos abaixo com os dados de acesso ao banco de dados.
database_type = ''
username = ''
password = ''
server = ''
database_name = ''


def get_connection():
    # TODO: Alterar a string de acesso, caso necessário.
    config = "{database_type}://{username}:{password}@{server}/{database_name}".format(
        database_type=database_type,
        username=username,
        password=password,
        server=server,
        database_name=database_name
    )

    app.config['SQLALCHEMY_DATABASE_URI'] = config

    return SQLAlchemy(app)


database = get_connection()
