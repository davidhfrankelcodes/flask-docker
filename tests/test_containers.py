import random

def test_containers(client, docker_client):
    container_id = get_container_id(docker_client)

    ''' TESTS '''
    get_container_app(client, container_id)
    get_containers_app(client)
    get_container_api(client, container_id)
    get_containers_api(client)


def get_containers_app(client):
    containers_app = client.get('/containers/')
    assert containers_app.status_code == 200

def get_containers_api(client):
    containers_api = client.get('/api/containers/')
    assert containers_api.status_code == 200

def get_container_api(client, container_id):
    containers_app =  client.get(f'/api/containers/{container_id}/')
    assert containers_app.status_code == 200

def get_container_app(client, container_id):
    container_app =  client.get(f'/containers/{container_id}/')
    assert container_app.status_code == 200

def get_container_id(docker_client):
    containers = docker_client.containers.list()
    container_id = random.choice(containers).id
    return container_id
