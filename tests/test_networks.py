import sys 
sys.path.append(".")
import pytest 
from app import app

def test_networks_route(client):
    response = client.get('/networks/')
    assert response.status_code == 200

@pytest.fixture
def client():
    app.config['TESTING'] = True
    client = app.test_client()

    yield client
