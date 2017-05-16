from ldap3 import Server, Connection
from voip import db
from voip.users.models import User
import config


def ldap_conn(username, password):
    s = Server(config.Config.LDAP_HOST)
    user = 'cn={},ou=test,dc=test,dc=test'.format(username)
    conn = Connection(s, user=user, password=password)
    return conn


def check_ldap_login(username, password):
    conn = ldap_conn(username, password)
    return conn.bind()


def sync_ldap_users():

    conn = ldap_conn(config.Config.LDAP_NAME, config.Config.LDAP_PASSWORD)
    conn.bind()
    conn.search(
        'ou=test,dc=test,dc=test',
        '(cn=*)',
        attributes=[
            'cn',
            'givenName',
            'sn',
            'departmentNumber',
            'mobile',
            'telephoneNumber',
            'mail',
        ]
    )

    for users in conn.response:
        username = "".join(users['attributes']['cn'])
        first_name = "".join(users['attributes']['givenName'])
        last_name = "".join(users['attributes']['sn'])
        department = "".join(users['attributes']['departmentNumber'])
        mobile = "".join(users['attributes']['mobile'])
        telephone = "".join(users['attributes']['telephoneNumber'])
        email = "".join(users['attributes']['mail'])
        user_db = User.query.filter_by(username=username).first()

        if not user_db:
            user_db = User(
                username=username,
                first_name=first_name,
                last_name=last_name,
                department=department,
                mobile=mobile,
                telephone=telephone,
                email=email
            )

            db.session.add(user_db)
        else:
            user_db.fill(first_name, last_name, department, mobile, telephone, email)

    db.session.commit()


