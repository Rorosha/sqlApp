"""
sqlApp
------

This is a partially complete flask application used to learn how to 
interact with a database. It's heavily based on flaskr - the 
application created during the flask tutorial. 
"""

import os
from sqlite3 import dbapi2 as sqlite3
from flask import Flask, request, session, g, redirect, url_for, \
     render_template, flash


app = Flask(__name__)

# Load default config and override config from an environment variable
app.config.update(dict(
    DEBUG=True,
    SECRET_KEY='wheee this is a super secret key!',
    USERNAME='admin',
    PASSWORD='password'
))
app.config.from_envvar('FLASKR_SETTINGS', silent=True)

################################
# Your database code goes here #
################################



@app.route('/')
def show_entries():
    # Query the db for all posts
    posts = [{"title": "Example", "text": "Change this to something that \
    actually queries the database! Then you can have multiple posts..."}]
#    posts = "Put your posts here"
    return render_template('index.html', posts=posts)


@app.route('/add', methods=['POST'])
def add_entry():

    # Check if the user is logged in, then submit form data
    # to the database. Then return to homepage.

    flash('New entry was successfully posted')
    return redirect(url_for('show_entries'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    # Normally you store users in the database - not hardcoded
    # into a config file. Extra credit for adding users to the 
    # database.
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            error = 'Invalid username'
        elif request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('You were logged in')
            return redirect(url_for('show_entries'))
    return render_template('login.html', error=error)


@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('show_entries'))


if __name__ == '__main__':
    app.run()
