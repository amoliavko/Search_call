from voip import db
from flask_login import UserMixin


class User(db.Model, UserMixin):
    __tablename__ = 'user'
    __bind_key__ = 'postgres'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255))
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    department = db.Column(db.String(255))
    mobile = db.Column(db.String(255))
    telephone = db.Column(db.String(255))
    email = db.Column(db.String(255))
    roles = db.Column(db.String(255), default='guest')

    def get_id(self):
        return self.id

    def get_roles(self):
            return self.roles

    def __init__(self, username, first_name, last_name, department, mobile, telephone, email):
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.department = department
        self.mobile = mobile
        self.telephone = telephone
        self.email = email

    def fill(self, first_name, last_name, department, mobile, telephone, email):
        self.first_name = first_name
        self.last_name = last_name
        self.department = department
        self.mobile = mobile
        self.telephone = telephone
        self.email = email

