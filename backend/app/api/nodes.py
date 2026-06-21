from flask import Blueprint, jsonify


nodes_bp = Blueprint('nodes', __name__)


@nodes_bp.get('/nodes')
def list_nodes():
    return jsonify([])
