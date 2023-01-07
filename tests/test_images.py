import random

def test_images(client, docker_client):
    response = get_image_app_response(client, docker_client)
    assert response.status_code == 200

    response = get_images_api_response(client)
    assert response.status_code == 200

    response = get_images_app_response(client)
    assert response.status_code == 200

def get_images_api_response(client):
    return client.get('/api/images/')

def get_images_app_response(client):
    return client.get('/images/')

def get_image_app_response(client, docker_client):
    images = docker_client.images.list()
    image_id = random.choice(images).id
    return client.get(f'/images/{image_id}/')
    