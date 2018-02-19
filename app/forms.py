from flask_wtf import FlaskForm
from wtforms import BooleanField, PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, Email, Length, Required


class AddTodoForm(FlaskForm):
    todo = StringField("Todo", validators=[DataRequired()])
    addbutton = SubmitField('AddButton')


class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[Required(), Email(), Length(max=100)])
    password = PasswordField('Password', validators=[Required()])
    remember_me = BooleanField('Keep me logged in')
    submit = SubmitField('Send')
