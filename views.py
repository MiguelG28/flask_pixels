from flask import render_template, jsonify, Blueprint
from werkzeug.utils import redirect

from forms import QIDForm
from models import User
from cenas import db, flask_app


# admin = User('admin', 'admin@example.com')
#
# db.create_all() # In case user table doesn't exists already. Else remove it.
#
# db.session.add(admin)
#
# db.session.commit() # This is needed to write the changes to database
#
# User.query.all()
#
# User.query.filter_by(username='admin').first()

# @app.route('/', methods=['GET', 'POST'])
# def qid_map_update():
#     form = QIDForm()
#     if form.validate_on_submit():
#        m = User()
#        m.username =app form.qidnumber.data
#        m.email = form.brfieldname.data
#        db.session.add(m)
#        db.session.commit()
#        return redirect('/')
#     return render_template('qidmapping.html',
#                             title='QID Mapping',
#                             form=form)


appx = Blueprint("app", __name__)


@appx.route('/', methods=['GET', 'POST'])
def qid_map_update():
    form = QIDForm()
    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        m = User(username=username, email=email)
        db.session.add(m)
        db.session.commit()
        return redirect('/')
    return render_template('user_form.html', title='QID Mapping', form=form)


@appx.route('/test', methods=['GET', 'POST'])
def qid_map_update_2():
    form = QIDForm()
    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        m = User(username=username, email=email)
        db.session.add(m)
        db.session.commit()
        return jsonify(m.to_json())
    return render_template('user_form.html', title='QID Mapping', form=form)
