import logging
import os

from flask import Flask

from flask_starter import user
from flask_starter.extensions import db

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    if test_config is None:
        # load default config from file or env
        app.config.from_object("config.Config")
    else:
        # use explicitly provided config
        app.config.from_mapping(
            test_config,
            SQLALCHEMY_TRACK_MODIFICATIONS=False,
        )
    print("DB URI:", app.config["SQLALCHEMY_DATABASE_URI"])

    # db_url = os.environ.get(
    #    "DB_URL", "postgresql://flask_user:flask_password@localhost:5432/flask_db"
    # )

    @app.route("/")
    def root():
        return "Hello, World!"

    register_extensions(app)
    app.register_blueprint(user.user_bp)

    return app


def register_extensions(app: Flask) -> None:
    db.init_app(app)
    with app.app_context():
        # Create tables if they don't exist
        # Don't do this in production, use migrations instead
        db.create_all()
