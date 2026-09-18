import pytest

from app import create_app
from app.data import reset_requests


@pytest.fixture(autouse=True)
def reset_data():
    reset_requests()


@pytest.fixture()
def client():
    return create_app(testing=True).test_client()
