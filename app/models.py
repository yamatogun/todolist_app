from . import db
from flask_login import UserMixin
from . import login_manager
from werkzeug import generate_password_hash, check_password_hash


@login_manager.user_loader
def load_user(user_id):
    # returns the User object that match the given primary key
    return User.query.get(user_id)

# class Todo(db.Model):
#     __tablename__ = 'todos'
#     id = db.Column(db.Integer, primary_key=True)
#     todo = db.Column(db.String(200), nullable=False)
#     user_id = db.Column(db.Integer, nullable=False)


class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)

    # email must be unique, used for authentication
    email = db.Column(db.String(100),
                      unique=True,
                      nullable=False)
    password_hash = db.Column(db.String(100), nullable=False)

    def set_password(self, pwd):
        self.password_hash = generate_password_hash(pwd)

    def verify_password(self, pwd):
        """
        Check whether or not user password <pwd> given is correct
        """
        return check_password_hash(self.password_hash, pwd)
