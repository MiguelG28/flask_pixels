import os

from flask import Flask, redirect, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy


from forms import QIDForm

app = Flask(__name__)
db = SQLAlchemy(app)

from models import User

from views import appx


DATABASE_URI='mysql+mysqlconnector://{user}:{password}@{server}/{database}'.format(
    user='root',
    password='qwerty',
    server='localhost',
    database='employees'
)
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI

SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

app.register_blueprint(appx)

