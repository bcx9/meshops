from flask import Blueprint, jsonify


gateways_bp = Blueprint('gateways', __name__)


@gateways_bp.get('/gateways')
def list_gateways():
    return jsonify([])
