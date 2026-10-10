import pytest
from app import app

@pytest.fixture
def client():
    return app.test_client()

def test_home(client):
    res = client.get("/")
    assert res.status_code == 200
    assert res.get_json()["status"] == "running"

def test_health(client):
    res = client.get("/health")
    assert res.status_code == 200
    assert res.get_json()["status"] == "healthy"

def test_add(client):
    res = client.get("/add/3/4")
    assert res.status_code == 200
    assert res.get_json()["result"] == 7
