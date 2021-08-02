from database import database


class NomeModel(database.Model):
    # TODO: Colocar o nome da tabela do banco de dados.

    table_name = ''

    # TODO: Colocar as colunas do banco de dados e as constraints delas.

    exemplo_campo = database.Column(
        database.Integer,   # Isso são as constraints
        primary_key=True
    )

    # TODO: Implementar as operações de manipulação do banco de dados. Chamá-las através da view.
