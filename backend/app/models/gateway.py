class Gateway:
    def __init__(self, name, connection_type, host=None, port=None):
        self.name = name
        self.connection_type = connection_type
        self.host = host
        self.port = port
        self.status = 'offline'
