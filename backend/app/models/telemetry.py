from ..database import db


class Telemetry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    altitude = db.Column(db.Float)
    speed = db.Column(db.Float)
    rssi = db.Column(db.Integer)
    snr = db.Column(db.Float)
    battery = db.Column(db.Float)
    timestamp = db.Column(db.DateTime)
    node_id = db.Column(db.Integer, db.ForeignKey('node.id'))
