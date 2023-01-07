import sys 
sys.path.append(".")
import pytest 
from app import app

def test_volumes_app_route(client):
    response = client.get('/volumes/')
    assert response.status_code == 200

def test_volumes_api_route(client):
    response = client.get('/api/volumes/')
    assert response.status_code == 200

@pytest.fixture
def client():
    app.config['TESTING'] = True
    client = app.test_client()

    yield client
