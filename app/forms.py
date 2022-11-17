from wtforms import Form, HiddenField
from wtforms import validators
from wtforms import StringField, PasswordField, TextAreaField
from wtforms.fields.simple import BooleanField, EmailField

from .models import User

def admin_validator(form, field):
    if field.data == 'Admin' or field.data == 'admin' or  field.data == 'ADMIN':
        raise validators.ValidationError('Admin user is not allowed.')

def length_honeypot(form, field):
    if len(field.data) > 0:
        raise validators.ValidationError('Only humans can register.')

class LoginForm(Form):
    username = StringField('Username', [
        validators.length(min=4, max=50, message='Username must be at least 4 characters')
    ])
    password =  PasswordField('Password', [
        validators.DataRequired(message='Password required.')
    ])

class RegisterForm(Form):
    username = StringField('Username', [
        validators.length(min=4, max=50),
        admin_validator
    ])
    email = EmailField('Email', [
        validators.length(min=6, max=100),
        validators.DataRequired(message='Email required'),
        validators.Email(message='Please enter a valid email address.')
    ])
    password = PasswordField('Password', [
        validators.DataRequired('Password required.'),
        validators.EqualTo('confirm_password', message='Passwords do NOT match.')
    ])
    confirm_password = PasswordField('Confirm password')
    accept = BooleanField('',[
        validators.DataRequired()
    ])
    honeypot = HiddenField("", [ length_honeypot] )

    def validate_username(self, username):
        if User.get_by_username(username.data):
            raise validators.ValidationError('Username already exists.')

    def validate_email(self, email):
        if User.get_by_email(email.data):
            raise validators.ValidationError('That email is already in use.')

    def validate(self):
        if not Form.validate(self):
            return False

        if len(self.password.data) < 4:
            self.password.errors.append('Password must be at least 4 characters long.')
            return False
        return True

class TaskForm(Form):
    title = StringField('Title', [
        validators.length(min=4, max=50, message='Title out of range.'),
        validators.DataRequired(message='Title required.')
    ])
    description = TextAreaField('Description', [
        validators.DataRequired(message='Description required.')
    ], render_kw={'rows': 5})

