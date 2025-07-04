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

    # Database URL: get from env or default to local SQLite for fallback
    db_url = os.environ.get(
        "DB_URL", "postgresql://flask_user:flask_password@postgres:5432/flask_db"
    )

    app.config.from_mapping(
        SECRET_KEY="dev",
        SQLALCHEMY_DATABASE_URI=db_url,
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
    )

    if test_config:
        # If passed a test config dict, override everything
        app.config.from_mapping(test_config)
    else:
        # load instance config (optional), e.g., instance/config.py
        app.config.from_pyfile("config.py", silent=True)

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


# Only create the app if this file is run directly OR imported by Gunicorn
app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
