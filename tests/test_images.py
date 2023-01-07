import random

def test_images(client, docker_client):
    image_id = get_image_id(docker_client)

    ''' TESTS '''
    get_image_app(client, image_id)
    get_images_app(client)
    get_image_api(client, image_id)
    get_images_api(client)


def get_images_app(client):
    images_app = client.get('/images/')
    assert images_app.status_code == 200

def get_images_api(client):
    images_api = client.get('/api/images/')
    assert images_api.status_code == 200

def get_image_api(client, image_id):
    images_app =  client.get(f'/api/images/{image_id}/')
    assert images_app.status_code == 200

def get_image_app(client, image_id):
    image_app =  client.get(f'/images/{image_id}/')
    assert image_app.status_code == 200

def get_image_id(docker_client):
    images = docker_client.images.list()
    image_id = random.choice(images).id
    return image_id
