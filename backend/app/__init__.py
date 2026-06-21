from flask import Flask
from .config import Config
from .database import db
from .api.health import health_bp
from .api.gateways import gateways_bp
from .api.nodes import nodes_bp


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    app.register_blueprint(health_bp, url_prefix='/api')
    app.register_blueprint(gateways_bp, url_prefix='/api')
    app.register_blueprint(nodes_bp, url_prefix='/api')

    return app
