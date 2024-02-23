import pytest
from app import app
import os
from app.utils.database import db

DATABASE_TYPE = os.getenv("DATABASE_TYPE")
DATABASE_USER = os.getenv("DATABASE_USER")
DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD")
DATABASE_HOST = os.getenv("DATABASE_HOST")
DATABASE_NAME = os.getenv("DATABASE_NAME")
DATABASE_PORT = os.getenv("DATABASE_PORT")

@pytest.fixture
def test_app():
    app.config['TESTING'] = True
    # app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///:memory:"
    with app.app_context():
        yield app