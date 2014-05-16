#!/usr/bin/env python
#coding=utf-8
from app import app


@app.route('/')
def hello_world():
    return 'Hello World!'

