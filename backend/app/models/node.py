from ..database import db


class Node(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    node_id = db.Column(db.String(64), unique=True, nullable=False)
    name = db.Column(db.String(128))
    last_seen = db.Column(db.DateTime)
    battery = db.Column(db.Float)
    gateway_id = db.Column(db.Integer, db.ForeignKey('gateway.id'))
    telemetry = db.relationship('Telemetry', backref='node', lazy=True)
