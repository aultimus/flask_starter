# conftest.py is a special file for pytest configuration.
# It will always be loaded first.

import os
import psycopg2
import pytest
from sqlalchemy import create_engine, text
from app import create_app, db

TEST_DB_NAME = "flask_app_test"
TEST_DB_URL = f"postgresql://flask_user:flask_password@localhost:5432/{TEST_DB_NAME}"
SYSTEM_DB_URL = "postgresql://flask_user:flask_password@localhost:5432/postgres"


@pytest.fixture(scope="session")
def create_test_database():
    """
    Ensure the test database exists before any tests run.
    """
    conn = psycopg2.connect(SYSTEM_DB_URL)
    conn.autocommit = True
    cur = conn.cursor()

    cur.execute(f"SELECT 1 FROM pg_database WHERE datname = '{TEST_DB_NAME}'")
    exists = cur.fetchone()
    if not exists:
        cur.execute(f'CREATE DATABASE "{TEST_DB_NAME}"')
        print(f"Created database {TEST_DB_NAME}")
    else:
        print(f"Database {TEST_DB_NAME} already exists")

    cur.close()
    conn.close()


@pytest.fixture(scope="session")
def app(create_test_database):
    """
    Create Flask app connected to test DB.
    """
    app = create_app(
        {
            "TESTING": True,
            "SQLALCHEMY_DATABASE_URI": TEST_DB_URL,
        }
    )

    with app.app_context():
        db.drop_all()
        db.create_all()

    return app


@pytest.fixture(scope="function", autouse=True)
def clean_db(app):
    print(">>> clean_db running <<<")
    with app.app_context():
        conn = db.engine.connect()
        trans = conn.begin()
        for table in reversed(db.metadata.sorted_tables):
            conn.execute(
                text(f'TRUNCATE TABLE "{table.name}" RESTART IDENTITY CASCADE')
            )
        trans.commit()
        conn.close()

        # CRITICAL: fully clean session
        db.session.rollback()
        db.session.expunge_all()
        db.session.remove()


@pytest.fixture
def client(app):
    """
    Flask test client.
    """
    return app.test_client()
