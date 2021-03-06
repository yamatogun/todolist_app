from datetime import date

from flask import flash, jsonify, redirect, render_template, request, url_for
from flask_login import current_user, login_user,  login_required, logout_user
from sqlalchemy.exc import IntegrityError

from . import app, db
from forms import AddTodoForm, LoginForm
from models import Todo, User


@app.route('/')
@login_required
def home():
    form = AddTodoForm()
    todos = current_user.todos  # current_user is an instance of User
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
    user_id = current_user.id
    ntodos = len(current_user.todos)
    rank = ntodos + 1  # new rank is last rank + 1
    print "rank: ", rank
    newtodo = Todo(todo=content, user_id=user_id, rank=rank)
    db.session.add(newtodo)
    try:
        db.session.commit()
        todo_id = newtodo.id  # id given only after committing
        print "todo_id: {}".format(todo_id)
        message = "New todo task successfully inserted"
        response = jsonify(message=message, tid=todo_id)
        response.status_code = 200
        return response
        # return "New todo task added in database", 200
    except IntegrityError:
        db.session.rollback()
        return "Couldn't perform todo insertion", 500


@app.route('/removetodo', methods=['POST'])
@login_required
def removetodo():
    print "IN REMOVETODO"
    todo_id = request.form['todo-id']
    # remove corresponding todo from the database
    todo_to_remove = Todo.query.get(todo_id)
    current_rank = todo_to_remove.rank
    print todo_to_remove
    db.session.delete(todo_to_remove)
    # update rank of remaining todos in the same transaction
    # decrement rank for todos that have higher ranks
    todos_higher_rank = Todo.query.filter(Todo.rank > current_rank).all()
    if todos_higher_rank:
        for todo in todos_higher_rank:
            todo.rank -= 1
    db.session.commit()
    return "Deletion completed", 200


@login_required
@app.route('/updatestatus', methods=['POST'])
def update_status():
    status_value = request.form['todo-status']
    tid = request.form['tid']
    status = True if status_value == "true" else False
    uid = current_user.id
    todo = Todo.query.get(tid)  # int ?
    if todo.user_id == uid:  # to prevent any update from another user
        todo.status = status
        db.session.commit()
    return "ok status updated", 200
