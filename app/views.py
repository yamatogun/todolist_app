from flask import flash, render_template, redirect, url_for
from flask_login import login_user

from forms import LoginForm
from models import User

from . import app


@app.route("/")
def home():
    return render_template("list_of_todos.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    print 'IN THE POST'
    form = LoginForm()  # new object even when POST ?
    print "form created"
    print form.errors
    # POST: email and password available
    if form.validate_on_submit():
        print "form validated: send clicked"
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            print "credentials are ok"
            login_user(user)
            return redirect(url_for('home'))
        print "password NOT ok"
        flash('login or password is wrong')
    # GET (+ redirection)
    print 'form not validated: render form'
    print form.errors
    return render_template("login.html", form=form)
