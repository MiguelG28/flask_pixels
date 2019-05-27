import json
import os

import requests
from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask_pymongo import PyMongo

project_dir = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__)

# MailTrap
app.config['MAIL_SERVER'] = 'smtp.mailtrap.io'
app.config['MAIL_PORT'] = 2525
app.config['MAIL_USERNAME'] = '957df237871ea9'
app.config['MAIL_PASSWORD'] = 'c822e3d3dda305'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config["MONGO_URI"] = "mongodb+srv://mongo_flask_db:!Alu12345@mongoflask-c8gqv.mongodb.net/mongo_flask_db?retryWrites=true"

from flask_mail import Mail, Message
mail = Mail(app)
mongo = PyMongo(app)


@app.route('/', methods=["GET", "POST"])
def home():
    if request.form:
        try:
            title = request.form.get("title")
            mongo.db.book.insert({'title': title})
            msg = Message("New book title added", sender='yourId@gmail.com', recipients=['id1@gmail.com'])
            mail.send(msg)
        except Exception as e:
            print("Failed to add book")
            print(e)
    books = mongo.db.book.distinct('title')
    return render_template("home.html", books=books)


@app.route("/update", methods=["POST"])
def update():
    try:
        newtitle = request.form.get("newtitle")
        oldtitle = request.form.get("oldtitle")
        mongo.db.book.update({'title': oldtitle},  {'title': newtitle})
    except Exception as e:
        print("Couldn't update book title")
        print(e)
    return redirect("/")


@app.route("/delete", methods=["POST"])
def delete():
    title = request.form.get("title")
    mongo.db.book.remove({'title': title})
    return redirect("/")


@app.route("/cat-facts", methods=["GET", "POST"])
def get_cat_facts():
    r = requests.get('https://cat-fact.herokuapp.com/facts')
    facts = json.loads(r.content)
    return render_template("cat_facts.html", facts=facts)


@app.route("/cat-facts/users", methods=["GET", "POST"])
def get_cat_facts_users():
    r = requests.get('https://cat-fact.herokuapp.com/facts')
    facts = json.loads(r.content)
    users = ((),)
    for values in facts['all']:
        if values.get('user'):
            first_name = values.get('user').get('name')['first']
            last_name = values.get('user').get('name')['last']
            id = values.get('user').get('_id')
            name = (id, first_name, last_name)
            if name not in users:
                users += (name, )
    return render_template("cat_facts_users.html", users=users)


@app.route("/cat-facts/users/<id>", methods=["GET", "POST"])
def get_cat_facts_by_user(id):
    r = requests.get('https://cat-fact.herokuapp.com/facts')
    facts = json.loads(r.content)
    user_data = []
    for values in facts['all']:
        if values.get('user'):
            if values.get('user').get('_id') == id:
                user_data.append(values)
    return render_template("cat_facts_by_user.html", facts=user_data)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)