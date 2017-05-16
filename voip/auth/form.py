from flask_wtf import FlaskForm
from wtforms import PasswordField
from wtforms import StringField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    username = StringField('Логин', validators=[DataRequired(message='Введите логин')])
    password = PasswordField('Пароль', validators=[DataRequired(message='Введите пароль')])
