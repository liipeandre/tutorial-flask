from app import app
from flask import render_template, request, flash, redirect, url_for

from models.Usuario import Usuario

from models.operations import crud, database


@app.route('/usuario/inserir', methods=['GET', 'POST'], endpoint='usuario.inserir')
def inserir():
    if request.method == 'GET':
        return render_template('usuario/cadastrar.html')

    else:
        nome = request.form.get('nome', '')
        idade = request.form.get('idade', '')

        if not nome or len(nome) > 40:
            flash("Campo 'nome' é obrigatório e deve ter no máximo 40 caracteres.")

        elif not idade or not idade.isdigit() or int(idade) < 0:
            flash("Campo 'idade' é obrigatório e deve ser numérico.")

        else:
            database.begin_transaction()

            usuario = Usuario()

            if crud.insert(usuario) and database.commit():
                flash('Usuário criado com sucesso.')

            else:
                flash('Erro ao inserir usuário.')

        return redirect(url_for('usuario.list'))


@app.route('/usuario/deletar', methods=['GET'], endpoint='usuario.deletar')
def deletar():
    id_usuario = request.form.get('id_usuario', '')

    if not id_usuario or not id_usuario.isdigit() or int(id_usuario) < 0:
            flash("Campo 'id_usuario' é obrigatório e deve ser numérico.")

    else:
        database.begin_transaction()

        usuario = Usuario()
        usuario.id_usuario = id_usuario

        if crud.delete(usuario) and database.commit():
            flash('Usuário excluído com sucesso.')

        else:
            flash('Erro ao excluir usuário.')

    return redirect(url_for('usuario.list'))


@app.route('/', methods=['GET'], endpoint='usuario.listar')
def listar():
    usuario = Usuario()
    usuarios = crud.list(usuario)

    if usuarios is None:
        flash('Erro ao listar usuários.')
        usuarios = []

    return render_template('index.html', usuarios=usuarios)


@app.route('/usuario/visualizar', methods=['GET'], endpoint='usuario.visualizar')
def visualizar():
    id_usuario = request.form.get('id_usuario', '')

    if not id_usuario or not id_usuario.isdigit() or int(id_usuario) < 0:
        flash("Campo 'id_usuario' é obrigatório e deve ser numérico.")

    else:
        usuario = Usuario()
        usuario = crud.view(usuario, id_usuario)

        if usuario is None:
            usuario = []
            flash('Erro ao selecionar usuário.')

        return render_template('usuario/editar.html', usuario=usuario)

    return redirect(url_for('usuario.list'))


@app.route('/usuario/editar', methods=['GET', 'POST'], endpoint='usuario.editar')
def editar():
    if request.method == 'GET':
        visualizar()

    else:
        id_usuario = request.form.get('id_usuario', '')
        nome = request.form.get('nome', '')
        idade = request.form.get('idade', '')

        if not id_usuario or not id_usuario.isdigit() or int(id_usuario) < 0:
            flash("Campo 'id_usuario' é obrigatório e deve ser numérico.")

        elif not nome or len(nome) > 40:
            flash("Campo 'nome' é obrigatório e deve ter no máximo 40 caracteres.")

        elif not idade or not idade.isdigit() or int(idade) < 0:
            flash("Campo 'idade' é obrigatório e deve ser numérico.")

        else:
            database.begin_transaction()

            usuario = Usuario()

            if crud.edit(usuario, request.form) and database.commit():
                flash('Usuário alterado com sucesso.')
                return redirect(url_for('usuario.list'))

            else:
                flash('Erro ao alterar usuário.')
                return render_template('usuario/editar.html', usuario=request.form)
