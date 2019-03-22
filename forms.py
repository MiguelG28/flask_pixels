from flask_wtf import Form
from wtforms import StringField


class QIDForm(Form):
    username = StringField('username')
    email = StringField('email')
