#!/usr/bin/env python
#coding=utf-8
from flask.ext.wtf import Form
from wtforms import TextField, validators, SubmitField, TextAreaField, PasswordField
from models import User


class ContactForm(Form):
    name = TextField("昵称", [validators.Required("Please enter your name.")])
    email = TextField("Email", [validators.Required("Please enter your email address."),
                                validators.Email("Please enter your email address.")])
    subject = TextField("标题", [validators.Required("Please enter a subject.")])
    message = TextAreaField("联系内容", [validators.Required("Please enter a message.")])
    submit = SubmitField("发送")


class SignupForm(Form):
    username = TextField("Username", [validators.Required("Please enter your userxname.")])
    email = TextField("Email", [validators.Required("Please enter your email address."),
                                validators.Email("Please enter your email address.")])
    password = PasswordField('Password', [validators.Required("Please enter a password.")])
    submit = SubmitField("Create account")

    def __init__(self, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)

    def validate(self):
        if not Form.validate(self):
            return False

        user = User.query.filter_by(email=self.email.data.lower()).first()
        if user:
            self.email.errors.append("That email is already taken")
            return False
        else:
            return True


class SigninForm(Form):
    email = TextField("Email", [validators.Required("Please enter your email address."),
                                validators.Email("Please enter your email address.")])
    password = PasswordField('Password', [validators.Required("Please enter a password.")])
    submit = SubmitField("Sign In")

    def __init__(self, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)

    def validate(self):
        if not Form.validate(self):
            return False
        user = User.query.filter_by(email=self.email.data).first()
        if user and user.check_password(self.password.data):
            return True
        else:
            self.email.errors.append("Invalid e-mails")
            return False