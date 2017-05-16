from flask import render_template
from flask import redirect
from voip.auth.form import LoginForm
from voip.lib.ldap import check_ldap_login
from voip.users.models import User
from flask_login import login_required
from flask_login import logout_user
from flask_login import login_user
from flask_login import current_user
from voip import app, db, login_manager
from functools import wraps


def requires_roles(*roles):
    def wrapper(f):
        @wraps(f)
        def wrapped(*args, **kwargs):
            if get_current_user_role() not in roles:
                return error_response()
            return f(*args, **kwargs)
        return wrapped
    return wrapper


def get_current_user_role():
    role = User.query.filter_by(username=current_user.username).first()
    if role is None:
        role.roles = 'Guest'

    return role.roles


def error_response():
    return render_template('error.html')


@app.route("/auth/login", methods=["GET", "POST"])
def login_view():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        if check_ldap_login(username, password):
            user = User.query.filter_by(username=username).first()
            if not user:
                user = User(username=username)
                db.session.add(user)
                db.session.commit()
            login_user(user, remember=True)
            return redirect('/')

    return render_template('login.html', form=form)


@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))


@app.route("/auth/logout")
@login_required
def logout():
    logout_user()
    return redirect('/')


@app.route("/users/")
@login_required
@requires_roles('admin')
def users():
    users = User.query.all()
    return render_template('users.html', users=users)


@app.route('/users/remove/<id>')
@login_required
@requires_roles('admin')
def remove_user(id):
    User.query.filter_by(id=id).delete()
    db.session.commit()
    return redirect('/users/')


@app.route('/users/makeadmin/<id>')
@login_required
@requires_roles('admin')
def make_admin(id):
    User.query.filter_by(id=id).update(dict(roles='admin'))
    db.session.commit()
    return redirect('/users/')