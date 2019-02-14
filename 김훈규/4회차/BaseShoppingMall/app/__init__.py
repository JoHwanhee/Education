from flask import Flask
from app.api.home import home as home_blueprint
from app.api.items import items as items_blueprint


def create_app():
    app = Flask(__name__, template_folder='template', instance_relative_config=True)
    app.register_blueprint(home_blueprint)
    app.register_blueprint(items_blueprint, url_prefix='/items')

    return app
