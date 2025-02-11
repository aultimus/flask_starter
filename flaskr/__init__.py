import os

from flask import Flask


from flaskr import user
from flaskr.extensions import db


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    try:
        db_url = os.environ["DB_URL"]
    except KeyError:
        raise IOError("Could not find DB_URL in env vars")

    app.config.from_mapping(
        SECRET_KEY="dev",
        DATABASE=os.path.join(app.instance_path, "flaskr.sqlite"),
        SQLALCHEMY_DATABASE_URI=db_url,
        # This provides significant overheads and modifications are already tracked
        # via SQLAlchemy events
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile("config.py", silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route("/")
    def root():
        return "Hello, World!"

    register_extensions(app)
    app.register_blueprint(user.user_bp)

    return app


def register_extensions(app: Flask) -> None:
    db.init_app(app)
    with app.app_context():
        db.create_all()
