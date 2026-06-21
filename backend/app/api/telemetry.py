from flask import Blueprint, jsonify
from ..models.telemetry import Telemetry


telemetry_bp = Blueprint('telemetry', __name__)


@telemetry_bp.get('/nodes/<int:node_id>/telemetry')
def node_telemetry(node_id):
    entries = Telemetry.query.filter_by(node_id=node_id).all()

    return jsonify([
        {
            'latitude': t.latitude,
            'longitude': t.longitude,
            'altitude': t.altitude,
            'battery': t.battery,
            'rssi': t.rssi,
            'snr': t.snr,
        }
        for t in entries
    ])
