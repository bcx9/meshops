from ..database import db


class Gateway(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    connection_type = db.Column(db.String(32), nullable=False)
    host = db.Column(db.String(255))
    port = db.Column(db.Integer)
    status = db.Column(db.String(32), default='offline')
    nodes = db.relationship('Node', backref='gateway', lazy=True)
