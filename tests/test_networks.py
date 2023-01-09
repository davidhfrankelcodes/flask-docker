import random

def test_networks(client, docker_client):
    network_id = get_network_id(docker_client)

    ''' TESTS '''
    get_network_app(client, network_id)
    get_networks_app(client)
    get_network_api(client, network_id)
    get_networks_api(client)


def get_networks_app(client):
    networks_app = client.get('/networks/')
    assert networks_app.status_code == 200

def get_networks_api(client):
    networks_api = client.get('/networks/?format=api')
    assert networks_api.status_code == 200

def get_network_api(client, network_id):
    networks_app =  client.get(f'/networks/{network_id}/?format=api')
    assert networks_app.status_code == 200

def get_network_app(client, network_id):
    network_app =  client.get(f'/networks/{network_id}/')
    assert network_app.status_code == 200

def get_network_id(docker_client):
    networks = docker_client.networks.list()
    network_id = random.choice(networks).id
    return network_id
