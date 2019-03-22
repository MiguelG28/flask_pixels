import os

from flask import Flask, redirect, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy


from forms import QIDForm

flask_app = Flask(__name__)
db = SQLAlchemy(flask_app)

from models import User
from views import appx


DATABASE_URI='mysql+mysqlconnector://{user}:{password}@{server}/{database}'.format(
    user='root',
    password='qwerty',
    server='localhost',
    database='employees'
)
flask_app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI

SECRET_KEY = os.urandom(32)
flask_app.config['SECRET_KEY'] = SECRET_KEY

flask_app.register_blueprint(appx)

#https://www.python-boilerplate.com/py3+flask+pytest/