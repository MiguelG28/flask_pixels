import json
import os

import requests
from flask import Flask
from flask import render_template
from flask import request
from flask import redirect

from flask_sqlalchemy import SQLAlchemy


project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "bookdatabase.db"))

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = database_file

# MailTrap
app.config['MAIL_SERVER']='smtp.mailtrap.io'
app.config['MAIL_PORT'] = 2525
app.config['MAIL_USERNAME'] = '957df237871ea9'
app.config['MAIL_PASSWORD'] = 'c822e3d3dda305'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False

db = SQLAlchemy(app)

from models import Book
from flask_mail import Mail, Message
mail = Mail(app)

@app.route('/', methods=["GET", "POST"])
def home():
    books = None
    if request.form:
        try:
            book = Book(title=request.form.get("title"))
            db.session.add(book)
            db.session.commit()
            msg = Message("New book added", sender='yourId@gmail.com', recipients=['id1@gmail.com'])
            msg.body = book.title
            mail.send(msg)
        except Exception as e:
            db.session.rollback()
            print("Failed to add book")
            print(e)
    books = Book.query.all()
    return render_template("home.html", books=books)


@app.route("/update", methods=["POST"])
def update():
    try:
        newtitle = request.form.get("newtitle")
        oldtitle = request.form.get("oldtitle")
        book = Book.query.filter_by(title=oldtitle).first()
        book.title = newtitle
        db.session.commit()
    except Exception as e:
        print("Couldn't update book title")
        print(e)
    return redirect("/")


@app.route("/delete", methods=["POST"])
def delete():
    title = request.form.get("title")
    book = Book.query.filter_by(title=title).first()
    db.session.delete(book)
    db.session.commit()
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
    app.run(debug=True)