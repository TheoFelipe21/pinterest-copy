from flask import render_template, url_for, flash, redirect, request
from pinterest import app, database, bcrypt
from flask_login import login_required, login_user, current_user, logout_user
from pinterest.forms import FormCriarConta, FormLogin, FormFoto
from pinterest.models import Usuario, Foto
from PIL import Image
import os
from werkzeug.utils import secure_filename

@app.route("/", methods=["GET", "POST"])
def home():
    form = FormLogin()
    if form.validate_on_submit():
        usuario = Usuario.query.filter_by(email=form.email.data).first()
        if usuario and bcrypt.check_password_hash(usuario.senha, form.senha.data):
            login_user(usuario, remember=True)
            flash('Login realizado com sucesso!', 'alert-success')
            return redirect(url_for('perfil', usuario=usuario.username))
        else:
            flash('Login ou senha incorretos.', 'alert-danger')
    return render_template('home.html', form=form)


@app.route("/criarconta", methods=["GET", "POST"])
def criarconta():
    form = FormCriarConta()
    if form.validate_on_submit():
        senha_crypt = bcrypt.generate_password_hash(form.senha.data)
        usuario = Usuario(username=form.username.data, email=form.email.data, senha=senha_crypt)
        database.session.add(usuario)
        database.session.commit()

        login_user(usuario, remember=True)
        flash('Conta criada com sucesso!', 'success')
        return redirect(url_for('perfil', usuario=usuario.username))
    return render_template('criarconta.html', form=form)



@app.route("/perfil/<usuario>", methods=["GET", "POST"])
@login_required
def perfil(usuario):
    if usuario == current_user.username:
        form_foto = FormFoto()
        if form_foto.validate_on_submit():
            arquivo = form_foto.foto.data
            nome_seguro = secure_filename(arquivo.filename)
            caminho = os.path.join(app.root_path, app.config['UPLOAD_FOLDER'], nome_seguro)

            tamanho = (400,500)
            imagem_reduzida = Image.open(arquivo)
            imagem_reduzida.thumbnail(tamanho)
            imagem_reduzida.save(caminho)

            foto = Foto(imagem=nome_seguro, id_usuario=current_user.id)
            database.session.add(foto)
            database.session.commit()
        return render_template('perfil.html', usuario=current_user, form_foto=form_foto)
    else: 
        usuario = Usuario.query.filter_by(username=usuario).first()
        return render_template('perfil.html', usuario=usuario, form=None)



@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route("/feed")
@login_required
def feed():
    fotos = Foto.query.order_by(Foto.data_criacao.desc()).all()
    return render_template('feed.html', fotos=fotos)

