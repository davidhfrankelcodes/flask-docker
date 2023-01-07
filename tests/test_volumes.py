import random

def test_volumes(client, docker_client):
    response = get_volume_app_response(client, docker_client)
    assert response.status_code == 200

    response = get_volumes_api_response(client)
    assert response.status_code == 200

    response = get_volumes_app_response(client)
    assert response.status_code == 200

def get_volumes_api_response(client):
    return client.get('/api/volumes/')

def get_volumes_app_response(client):
    return client.get('/volumes/')

def get_volume_app_response(client, docker_client):
    volumes = docker_client.volumes.list()
    volume_id = random.choice(volumes).id
    return client.get(f'/volumes/{volume_id}/')
    