class Node:
    def __init__(self, node_id, name=None):
        self.node_id = node_id
        self.name = name
        self.last_seen = None
        self.battery = None
