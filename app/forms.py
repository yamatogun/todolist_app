from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import Required, Email, Length, DataRequired


class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[Required(), Email(), Length(max=100)])
    # render <input type="password">
    password = PasswordField('Password', validators=[Required()])
    remember_me = BooleanField('Keep me logged in')
    submit = SubmitField('Send')

class AddTodoForm(FlaskForm):
    todo = StringField("Todo", validators=[DataRequired()])
    addbutton = SubmitField('AddButton')
