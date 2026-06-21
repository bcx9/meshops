from flask import Flask
from .config import Config
from .database import db


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    @app.get('/api/health')
    def health():
        return {'status': 'ok'}

    return app
