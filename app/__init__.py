from flask import Flask, app
from config import config_options
from flask_bootstrap import Bootstrap

bootstrap = Bootstrap()

def create_app(config_name):

    app = Flask(__name__)

    # creating the app configurations
    app.config.from_object(config_options[config_name])

    # initializing flask extensions
    bootstrap.init_app(app)

    # register
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # setting config
    from .request import configure_request
    configure_request(app)

    return app