from flask import Blueprint, jsonify
from ..models.node import Node


nodes_bp = Blueprint('nodes', __name__)


@nodes_bp.get('/nodes')
def list_nodes():
    nodes = Node.query.all()

    return jsonify([
        {
            'id': n.id,
            'node_id': n.node_id,
            'name': n.name,
            'battery': n.battery,
            'gateway_id': n.gateway_id,
        }
        for n in nodes
    ])
