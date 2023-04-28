from wtforms import StringField,validators,PasswordField,SubmitField
from flask_wtf import FlaskForm


class UserRegisterForm(FlaskForm):
    firstname=StringField('First Name')
    username=StringField('UserName')
    lastname=StringField('Last Name')
    email=StringField('E-mail',[validators.DataRequired(),validators.Email()])
    password=PasswordField('Password',[validators.DataRequired(),
                                       validators.EqualTo('confirm_password'),])
    confirm_password=PasswordField("Password",[validators.DataRequired()])
    submit= SubmitField('Register')




class LoginForm(FlaskForm):
    username = StringField(
        "username",
        [validators.DataRequired()],
    )
    password = PasswordField(
        "Password",
        [validators.DataRequired()],
    )
    submit = SubmitField("Login")