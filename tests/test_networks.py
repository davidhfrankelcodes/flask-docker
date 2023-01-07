import random

def test_networks(client, docker_client):
    response = get_network_app_response(client, docker_client)
    assert response.status_code == 200

    response = get_networks_api_response(client)
    assert response.status_code == 200

    response = get_networks_app_response(client)
    assert response.status_code == 200

def get_networks_api_response(client):
    return client.get('/api/networks/')

def get_networks_app_response(client):
    return client.get('/networks/')

def get_network_app_response(client, docker_client):
    networks = docker_client.networks.list()
    network_id = random.choice(networks).id
    return client.get(f'/networks/{network_id}/')
    