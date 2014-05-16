# -*- coding: utf-8 -*-
from flask.ext.sqlalchemy import SQLAlchemy
#加密保存密码
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from webhelpers.date import time_ago_in_words
db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'user'
    uid = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100))
    email = db.Column(db.String(120), unique=True)
    pwdhash = db.Column(db.String(54))
    created = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, username, email, password):
        self.username = username.title()
        self.email = email.lower()
        self.set_password(password)

    def set_password(self, password):
        self.pwdhash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.pwdhash, password)


class Topics():
    __tablename__ = 'topics'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text)
    created = db.Column(db.DateTime, default=datetime.utcnow)
    updated = db.Column(
        db.DateTime,
        default=datetime.utcnow,
        index=True,
    )

    def __init__(self, title, content):
        self.title = title
        self.content = content

    def __str__(self):
        return self.title

    def __repr__(self):
        return '<Topic: %s>' % self.id

    @property
    def created_in_words(self):
        return time_ago_in_words(self.created)




