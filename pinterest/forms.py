from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed
from wtforms import EmailField, StringField, PasswordField, SubmitField, FileField
from wtforms.validators import DataRequired, Email, Length, EqualTo, ValidationError
from pinterest.models import Usuario

class FormLogin(FlaskForm):
    email = EmailField('Email', validators=[DataRequired(message='Este campo é obrigatório.'), Email()])
    senha = PasswordField('Senha', validators=[DataRequired(), DataRequired(message='Este campo é obrigatório.')])
    submit = SubmitField('Login')

    def validate_email(self, email):
        usuario = Usuario.query.filter_by(email=email.data).first()
        if not usuario:
            raise ValidationError('Usuário inexistente. Por favor, verifique o email informado.')


class FormCriarConta(FlaskForm):
    email = EmailField('Email', validators=[DataRequired(), Email()])
    username = StringField('Nome de Usuário', validators=[DataRequired(), Length(min=5, max=25)])
    senha = PasswordField('Senha', validators=[DataRequired(), Length(min=8, max=20)])
    confirmar_senha = PasswordField('Confirmação de senha', 
        validators=[DataRequired(), 
        EqualTo('senha', message='As senhas não coincidem.')])
    submit = SubmitField('Criar Conta')

    def validate_email(self, email):
        usuario = Usuario.query.filter_by(email=email.data).first()
        if usuario:
            raise ValidationError('Este email já está em uso. Por favor, escolha outro.')

    def validate_username(self, username):
        usuario = Usuario.query.filter_by(username=username.data).first()
        if usuario:
            raise ValidationError('Este nome de usuário já está em uso. Por favor, escolha outro.')

class FormFoto(FlaskForm):
    foto = FileField('Foto', validators=[FileAllowed(['jpg', 'png'], 'Apenas imagens são permitidas.')])
    submit = SubmitField('Publicar')
