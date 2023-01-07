import sys 
sys.path.append(".")
import pytest 
from app import app

def test_containers_route(client):
    response = client.get('/containers/')
    assert response.status_code == 200

def test_images_route(client):
    response = client.get('/images/')
    assert response.status_code == 200

def test_networks_route(client):
    response = client.get('/networks/')
    assert response.status_code == 200

def test_volumes_route(client):
    response = client.get('/volumes/')
    assert response.status_code == 200

@pytest.fixture
def client():
    app.config['TESTING'] = True
    client = app.test_client()

    yield client
