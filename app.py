from flask import Flask, render_template, redirect
from flask_sqlalchemy import SQLAlchemy
import pymysql
#
# app = Flask(__name__)
#
# # SQLALCHEMY SETUP
# # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
# # db = SQLAlchemy(app)
#
#
# class Database:
#     def __init__(self):
#         host = "127.0.0.1"
#         user = "root"
#         password = "qwerty"
#         db = "employees"
#         self.con = pymysql.connect(host=host, user=user, password=password, db=db, cursorclass=pymysql.cursors.
#                                    DictCursor)
#         self.cur = self.con.cursor()
#
#     def list_employees(self):
#         self.cur.execute("SELECT first_name, last_name, gender FROM employees LIMIT 50")
#         result = self.cur.fetchall()
#         return result
#
#
# @app.route('/')
# def employees():
#     def db_query():
#         db = Database()
#         emps = db.list_employees()
#         return emps
#
#     res = db_query()
#     return render_template('employees.html', result=res, content_type='application/json')
#
# # from forms import QIDForm
# # from models import QIDMapping
#
# import os
# SECRET_KEY = os.urandom(32)
# app.config['SECRET_KEY'] = SECRET_KEY
# # @app.route('/')
# # def student():
# #    return render_template('student.html')
# #
# # @app.route('/result',methods = ['POST', 'GET'])
# # def result():
# #    if request.method == 'POST':
# #       result = request.form
# #       return render_template("results.html",result = result)
# #
# # if __name__ == '__main__':
# #    app.run(debug = True)
#
#
# # @app.route('/qidmapping', methods=['GET', 'POST'])
# # def qid_map_update():
# #     form = QIDForm()
# #     if form.validate_on_submit():
# #        m = QIDMapping()
# #        m.qid_number = form.qidnumber.data
# #        m.br_field_name = form.brfieldname.data
# #        m.vendor_field = form.vendorfieldname.data
# #        db.session.add(m)
# #        # result = QIDMapping.query.all()
# #        # print(result[1])
# #        return redirect('/qidmapping')
# #     return render_template('qidmapping.html',
# #                             title='QID Mapping',
# #                             form=form)
#
# from flask import Flask, render_template
# import pymysql
#
# app = Flask(__name__)
#
#
# class Database:
#     def __init__(self):
#         host = "127.0.0.1"
#         user = "root"
#         password = "qwerty"
#         db = "employees"
#         self.con = pymysql.connect(host=host, user=user, password=password, db=db, cursorclass=pymysql.cursors.
#                                    DictCursor)
#         self.cur = self.con.cursor()
#
#     def list_employees(self):
#         self.cur.execute("SELECT first_name, last_name, gender FROM employees LIMIT 50")
#         result = self.cur.fetchall()
#         return result
#
#
# @app.route('/')
# def employees():
#     def db_query():
#         db = Database()
#         emps = db.list_employees()
#         return emps
#
#     res = db_query()
#     return render_template('employees.html', result=res, content_type='application/json')

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
DATABASE_URI='mysql+mysqlconnector://{user}:{password}@{server}/{database}'.format(user='root', password='qwerty', server='localhost', database='employees')
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:qwerty@localhost/employees'
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
db = SQLAlchemy(app)

# class Employees(db.Model):
#     emp_no = db.Column(db.Integer, primary_key=True)
#     birth_date = db.Column(db.Date)
#     first_name = db.Column(db.String(75))
#     last_name = db.Column(db.String(75))
#     gender = db.Column(db.String(75))
#     hire_date = db.Column(db.Date)
#
# test = Employees(emp_no='121212', birth_date='12/12/12', first_name='gatilhada', last_name='meita', gender='M', hire_date='12/12/12')
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.username

admin = User('admin', 'admin@example.com')

db.create_all() # In case user table doesn't exists already. Else remove it.

db.session.add(admin)

db.session.commit() # This is needed to write the changes to database

User.query.all()

User.query.filter_by(username='admin').first()
