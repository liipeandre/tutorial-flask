from database import database


class Usuario(database.Model):
    # TODO: Colocar o nome da tabela do banco de dados.

    table_name = 'usuario'

    # TODO: Colocar as colunas do banco de dados e as constraints delas.

    id = database.Column(
        database.Integer,
        primary_key=True
    )

    nome = database.Column(
        database.String(45),
        nullable=False
    )

    idade = database.Column(
        database.Integer,
        nullable=False
    )

    # TODO: Implementar abaixo as operações de manipulação do banco de dados. Chamá-las através da view.
