#blog.py - the controller

#imports
from flask import Flask, render_template, request, session, \
	flash, redirect, url_for, g

import sqlite3

#configuration

DATABASE = 'blog.db'
USERNAME = 'RyanGoh83'
PASSWORD = 'IloveSecretSauce'
SECRET_KEY = '\x17\xa4\xc94. 0\x03\r\xc7\x96\xda\x7fk\x08\xef0\xa6\xe4\xf6\xb5^\x10\x8b'


app = Flask(__name__)

# pulls in app configuration by looking for UPPERCASE variables.

app.config.from_object(__name__)

#function used for connecting to the db
def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

@app.route('/', methods=['GET', 'POST'])
def login():
	error = None
	status_code = 200
	if request.method == 'POST':
		if request.form['username'] != app.config['USERNAME'] or\
			request.form['password'] != app.config['PASSWORD']:
			error = 'Invalid credentials. Please try again.'
			status_code = 401
		else:
			session['logged_in'] = True
			return redirect(url_for('main'))
	return render_template('login.html', error=error), status_code

@app.route('/main')

@app.route('/logout')
def logout():
	session.pop('logged_in', None)
	flash("You were logged out")
	return redirect(url_for('login'))
	
def main():
    return render_template('main.html')


if __name__ == '__main__':
    app.run(debug=True)

