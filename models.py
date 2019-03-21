from app import db


class QIDMapping(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    qid_number = db.Column(db.Integer)
    br_field_name = db.Column(db.String(75))
    vendor_field = db.Column(db.String(75))