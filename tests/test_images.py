import sys 
sys.path.append(".")
import pytest 
from app import app

def test_images_app_route(client):
    response = client.get('/images/')
    assert response.status_code == 200

def test_images_api_route(client):
    response = client.get('/api/images/')
    assert response.status_code == 200

@pytest.fixture
def client():
    app.config['TESTING'] = True
    client = app.test_client()

    yield client
