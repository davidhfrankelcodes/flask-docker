import random

def test_volumes_app_route(client):
    response = client.get('/volumes/')
    assert response.status_code == 200

def test_volumes_api_route(client):
    response = client.get('/api/volumes/')
    assert response.status_code == 200

def test_volumes_app_route(client, docker_client):
    volumes = docker_client.volumes.list()
    volume_id = random.choice(volumes).id
    response = client.get(f'/volumes/{volume_id}/')
    assert response.status_code == 200
