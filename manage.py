from voip import manager
from voip import db
from voip.users.models import User
from flask_migrate import MigrateCommand
from voip.lib.ldap import sync_ldap_users

manager.add_command('db', MigrateCommand)

@manager.command
def hello():
    print('Hello, world!')


@manager.command
def createdb():
    db.create_all(bind=['postgres'])

@manager.command
def sync_users():
    sync_ldap_users()

@manager.command
def make_admin(username):
    u = User.query.filter_by(username=username).first()
    if u is None:
        raise ValueError('Нет пользователя с таким юзернеймом')
    User.query.filter_by(username=username).update(dict(roles='admin'))
    db.session.commit()
    print("{} теперь admin".format(username))

if __name__ == '__main__':
    manager.run()