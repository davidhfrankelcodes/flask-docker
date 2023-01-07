import random

def test_networks_app_route(client):
    response = client.get('/networks/')
    assert response.status_code == 200

def test_networks_api_route(client):
    response = client.get('/api/networks/')
    assert response.status_code == 200

def test_networks_app_route(client, docker_client):
    networks = docker_client.networks.list()
    network_id = random.choice(networks).id
    response = client.get(f'/networks/{network_id}/')
    assert response.status_code == 200
