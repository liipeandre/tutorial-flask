from app import app
from flask import request, render_template, url_for, redirect, flash, session

# Ler um campo da request
campo = request.form.get('campo', '')

# Criar uma mensagem para exibi-la no template.
flash('Nova Messagem')

# Criar uma sessão.
session['logged'] = True

# Enviar um template (usar com o comando return)
render_template('produtos/insert.html')

# Enviar um template com dados (usar com o comando return)
dados = [1, 2, 3, 4]
render_template('produtos/list.html', parametro1=dados)

# Enviar um template com os dados do formulário (usar com o comando return)
render_template('produtos/edit.html', produto=request.form)

# Redirecionar para uma outra view (usar com o comando return)
redirect(url_for('produto.list'))