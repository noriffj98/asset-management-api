from flask import Flask
from .routes import setup_routes
from .errors import register_error_handlers

def create_app():
    app = Flask(__name__)
    
    # Register routes and error handlers
    setup_routes(app)
    register_error_handlers(app)

    return app
