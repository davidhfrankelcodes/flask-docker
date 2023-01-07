import random

def test_volumes(client, docker_client):
    volume_id = get_volume_id(docker_client)

    ''' TESTS '''
    get_volume_app(client, volume_id)
    get_volumes_app(client)
    get_volume_api(client, volume_id)
    get_volumes_api(client)


def get_volumes_app(client):
    volumes_app = client.get('/volumes/')
    assert volumes_app.status_code == 200

def get_volumes_api(client):
    volumes_api = client.get('/api/volumes/')
    assert volumes_api.status_code == 200

def get_volume_api(client, volume_id):
    volumes_app =  client.get(f'/api/volumes/{volume_id}/')
    assert volumes_app.status_code == 200

def get_volume_app(client, volume_id):
    volume_app =  client.get(f'/volumes/{volume_id}/')
    assert volume_app.status_code == 200

def get_volume_id(docker_client):
    volumes = docker_client.volumes.list()
    volume_id = random.choice(volumes).id
    return volume_id
