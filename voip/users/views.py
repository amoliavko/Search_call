from flask import render_template
from flask import redirect
from voip.auth.models import User
from flask_login import login_required
from voip import app, db, login_manager
from voip.auth.views import requires_roles


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