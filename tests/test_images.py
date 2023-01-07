import random

def test_images_app_route(client):
    response = client.get('/images/')
    assert response.status_code == 200

def test_images_api_route(client):
    response = client.get('/api/images/')
    assert response.status_code == 200

def test_images_app_route(client, docker_client):
    images = docker_client.images.list()
    image_id = random.choice(images).id
    response = client.get(f'/images/{image_id}/')
    assert response.status_code == 200
