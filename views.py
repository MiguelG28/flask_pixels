from flask import render_template
from werkzeug.utils import redirect

from forms import QIDForm
from models import User
from app import db

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
#        m.username = form.qidnumber.data
#        m.email = form.brfieldname.data
#        db.session.add(m)
#        db.session.commit()
#        return redirect('/')
#     return render_template('qidmapping.html',
#                             title='QID Mapping',
#                             form=form)