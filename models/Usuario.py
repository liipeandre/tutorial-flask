from database import database, execute_sql_query


class Usuario(database.Model):
    id_usuario = database.Column(
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

    def inserir(self):
        query = """
            insert into usuario (nome, idade)
            values (:nome, :idade);
        """
        return execute_sql_query(query, self.__dict__)

    def deletar(self):
        query = """
            delete from usuario
            where id_usuario = :id_usuario;
        """
        return execute_sql_query(query, self.__dict__)


    def listar(self):
        query = """
            select id_usuario, nome, idade from usuario;
        """
        return execute_sql_query(query, self.__dict__)


    def visualizar(self):
        query = """
            select id_usuario, nome, idade from usuario
            where id_usuario = :id_usuario;
        """
        return execute_sql_query(query, self.__dict__)


    def editar(self):
        query = """
            update usuario set 
            nome = :nome, 
            idade = :idade
            where id_usuario = :id_usuario;
        """
        return execute_sql_query(query, self.__dict__)