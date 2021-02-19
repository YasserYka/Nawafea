import os

from flask import Flask, render_template
from . import controllers, models
from app.extensions import setup_db

database_filename = "database.db"
project_dir = os.path.dirname(os.path.abspath(__file__))
database_path = "sqlite:///{}".format(os.path.join(project_dir, database_filename))

def create_app():
    # create and configure the app
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    setup_db(app)
    register_blueprints(app)
    #register_errorhandlers(app)

    return app


def register_blueprints(app):
    """Register Flask blueprints."""
    app.register_blueprint(controllers.auction.blueprint)
    app.register_blueprint(controllers.home.blueprint)
    app.register_blueprint(controllers.product.blueprint)
    return None

'''
def register_errorhandlers(app):
    """Register error handlers."""
    @app.errorhandler(401)
    def internal_error(error):
        return render_template('401.html'), 401

    @app.errorhandler(404)
    def page_not_found(error):
        return render_template('404.html'), 404

    @app.errorhandler(500)
    def internal_error(error):
        return render_template('500.html'), 500

    return None
'''