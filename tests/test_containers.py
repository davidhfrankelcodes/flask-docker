import random

def test_containers(client, docker_client):
    response = get_container_app_response(client, docker_client)
    assert response.status_code == 200

    response = get_containers_api_response(client)
    assert response.status_code == 200

    response = get_containers_app_response(client)
    assert response.status_code == 200

def get_containers_api_response(client):
    return client.get('/api/containers/')

def get_containers_app_response(client):
    return client.get('/containers/')

def get_container_app_response(client, docker_client):
    containers = docker_client.containers.list()
    container_id = random.choice(containers).id
    return client.get(f'/containers/{container_id}/')
    