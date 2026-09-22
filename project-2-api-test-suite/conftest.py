import pytest
from api_client import APIClient

@pytest.fixture()
def client():
    return APIClient("https://reqres.in/api")

