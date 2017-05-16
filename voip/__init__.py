from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CsrfProtect
from flask_login import LoginManager
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

app = Flask(__name__)
app.config.from_object('config')
app.debug = True
app.config['SQLALCHEMY_DATABASE_URI'] = config.Config.Postgres
databases = {
    'postgres': config.Config.Postgres,
    'cdr': config.Config.cdr


}

app.config['SQLALCHEMY_BINDS'] = databases
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)
CsrfProtect(app)
login_manager = LoginManager(app)
login_manager.login_view = app.config['LOGIN_URL']
login_manager.login_message = 'Пожалуйста, войдите, чтобы получить доступ к этой странице.'
login_manager.login_message_category = 'danger'
manager = Manager(app)
migrate = Migrate(app, db)

from voip import views # NOQA
from voip.auth import views # NOQA
from voip.users import models # NOQA
from voip.calls import views, models # NOQA
from voip.routing import models, views # NOQA


