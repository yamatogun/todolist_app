from datetime import date

from flask import flash, render_template, redirect, url_for, request
from flask_login import login_user, logout_user, login_required, current_user

from . import app, db
from forms import LoginForm, AddTodoForm
from models import User, Todo


@app.route('/')
@login_required
def home():
    form = AddTodoForm()
    todos = current_user.todos
    today = date.today()
    day = today.day
    if 4 <= day <= 20 or 24 <= day <= 30:
        suffix = "th"
    else:
        suffix = ["st", "nd", "rd"][day % 10 - 1]
    literal_date = today.strftime("%A, %B %d{} %Y".format(suffix))
    return render_template("list_of_todos.html",
                           todos=todos,
                           date=literal_date,
                           form=form)


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


@app.route('/addtodo', methods=['POST'])
@login_required
def addtodo():
    print "IN ADDTODO"
    content = request.form['content']
    print "content: " + content
    user_id = current_user.id
    ntodos = len(current_user.todos)
    rank = ntodos + 1  # new rank is last rank + 1
    # newtodo = Todo(todo=content, user_id=user_id, rank=rank)
    # db.session.add(newtodo)
    # db.session.commit()
    print "NEW TODO TASK CREATED"
    return "new todo task added in the database", 200
