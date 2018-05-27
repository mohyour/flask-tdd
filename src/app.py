import sqlite3
import sys
sys.path.append('config')
import config
from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash, jsonify


# create and initialize app
app = Flask(__name__)

# configuration
app.config.from_object('config.APPLICATIONCONFIG')

# connect to database
def connect_db():
    """Connects to database"""
    connect = sqlite3.connect(app.config['DATABASE'])
    connect.row_factory = sqlite3.Row
    return connect

# create database
def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource('../schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()

# open database connection
def get_db():
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db

# close database connection
@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()


if __name__ == '__main__':
    init_db()
    app.run()
