from datetime import date

from flask import flash, render_template, redirect, url_for
from flask_login import login_user, logout_user, login_required, current_user

from . import app
from forms import LoginForm
from models import User



@app.route('/')
@login_required
def home():
    todos = current_user.todos
    today = date.today()
    day = today.day
    if 4 <= day <= 20 or 24 <= day <=30:
        suffix = "th"
    else: 
        suffix = ["st", "nd", "rd"][day%10-1]
    literal_date = today.strftime("%A, %B %d{} %Y".format(suffix))
    return render_template("list_of_todos.html", todos=todos, date=literal_date)


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


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))
