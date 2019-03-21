from flask import Flask, render_template, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)
from forms import QIDForm
from models import QIDMapping

import os
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY
# @app.route('/')
# def student():
#    return render_template('student.html')
#
# @app.route('/result',methods = ['POST', 'GET'])
# def result():
#    if request.method == 'POST':
#       result = request.form
#       return render_template("results.html",result = result)
#
# if __name__ == '__main__':
#    app.run(debug = True)


@app.route('/qidmapping', methods=['GET', 'POST'])
def qid_map_update():
    form = QIDForm()
    if form.validate_on_submit():
       m = QIDMapping()
       m.qid_number = form.qidnumber.data
       m.br_field_name = form.brfieldname.data
       m.vendor_field = form.vendorfieldname.data
       db.session.add(m)
       # result = QIDMapping.query.all()
       # print(result[1])
       return redirect('/qidmapping')
    return render_template('qidmapping.html',
                            title='QID Mapping',
                            form=form)