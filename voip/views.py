from flask import render_template, redirect, request
from voip import app
from voip import db
from flask_login import login_required


@app.route('/')
@login_required
def index():
    return render_template("main.html")