# -*- coding: utf-8 -*-
from app import app
from flask import render_template, redirect, request, url_for, session
from forms import SigninForm, SignupForm
from models import User, db


@app.route('/')
def home():
    user = User.query.filter_by(email=session['email']).first()
    return render_template('home.html', user=user)


@app.route('/about')
def about():
    user = User.query.filter_by(email=session['email']).first()
    return render_template('about.html', user=user)


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm()
    if request.method == 'POST':
        if form.validate():
            newuser = User(form.username.data, form.email.data, form.password.data)
            db.session.add(newuser)
            db.session.commit()

            session['email'] = newuser.email
            return redirect(url_for('profile'))

        else:
            return render_template('signup.html', form=form)

    elif request.method == 'GET':
        return render_template('signup.html', form=form)


@app.route('/profile')
def profile():
    if 'email' not in session:
        return redirect(url_for('signin'))

    user = User.query.filter_by(email=session['email']).first()
    if user is None:
        return redirect(url_for('signin'))
    else:
        return render_template('profile.html', user=user)


@app.route('/signin', methods=['GET', 'POST'])
def signin():
    form = SigninForm()
    if 'email' in session:
        return redirect(url_for('profile'))

    if request.method == 'POST':
        if form.validate():
            session['email'] = form.email.data
            return redirect(url_for('profile'))
        else:
            return render_template('signin.html', form=form)
    elif request.method == 'GET':
        return render_template('signin.html', form=form)


@app.route('/signout')
def signout():
    if 'email' not in session:
        return redirect(url_for('signin'))

    session.pop('email', None)
    return redirect(url_for('home'))