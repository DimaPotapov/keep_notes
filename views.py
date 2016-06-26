from __init__ import app
from __init__ import db
from models import User
from flask import render_template, flash, redirect, session, url_for, request, g
from flask.ext.login import login_user, logout_user, current_user, login_required

@app.route('/', methods=['GET','POST'])
def login():
	if request.method == 'POST':
		users = User.query.all()
		for user in users:
			if request.form['login'] in user.login and request.form['password'] in user.password:
				user.authenticated = True
				return render_template('field.html', user=request.form['login'])
			else:
				return 'not good bro'
	else:
		return render_template('index.html')

@app.route('/registration', methods=['GET','POST'])
def registration():
	if request.method =='POST':
		user = User(request.form['login'], request.form['password'])
		db.session.add(user)
		db.session.commit()
		return render_template('after_registration.html')
	else:	
		return render_template ('registration.html')