import pytest
from app import app as flask_app

# These tests largely duplicate the system tests, but they are run in-process
# and do not require the Docker container to be running.
# These are mostly here for demonstration purposes


@pytest.fixture
def client():
    with flask_app.test_client() as client:
        yield client
