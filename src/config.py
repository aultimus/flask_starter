import os


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "dev")
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DB_URL", "postgresql://flask_user:flask_password@localhost:5432/flask_db"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
