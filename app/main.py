# from flask import Flask, render_template
# from flask_sqlalchemy import SQLAlchemy
# 
# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqllite:///data.db'
# db = SQLAlchemy(app)
# 
# class Todos(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     todo = db.Column(db.String, nullable=False)
#     user_id = db.Column(db.Integer, nullable=False)
# 
# class Users(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String, nullable=False)
# 
# 
# @app.route("/")
# def home():
#     return render_template("list_of_todos.html")
# 
# if __name__ == "__main__":
#     app.run(debug=True)
