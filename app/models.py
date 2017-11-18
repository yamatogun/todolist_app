from . import db

# class Todo(db.Model):
#     __tablename__ = 'todos'
#     id = db.Column(db.Integer, primary_key=True)
#     todo = db.Column(db.String(200), nullable=False)
#     user_id = db.Column(db.Integer, nullable=False)

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)

    # email must be unique, used for authentication
    email = db.Column(db.String(100), 
                      unique=True,
                      nullable=False
                     )
    password = db.Column(db.String(100), nullable=False)
