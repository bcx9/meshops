from flask import Blueprint, jsonify
from ..models.gateway import Gateway


gateways_bp = Blueprint('gateways', __name__)


@gateways_bp.get('/gateways')
def list_gateways():
    gateways = Gateway.query.all()

    return jsonify([
        {
            'id': g.id,
            'name': g.name,
            'connection_type': g.connection_type,
            'status': g.status,
        }
        for g in gateways
    ])
