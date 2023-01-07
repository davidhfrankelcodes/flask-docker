import random

def test_containers_app_route(client):
    response = client.get('/containers/')
    assert response.status_code == 200

def test_containers_api_route(client):
    response = client.get('/api/containers/')
    assert response.status_code == 200

def test_container_app_route(client, docker_client):
    containers = docker_client.containers.list()
    container_id = random.choice(containers).id
    response = client.get(f'/containers/{container_id}/')
    assert response.status_code == 200
