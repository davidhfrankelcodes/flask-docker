from flask import render_template, jsonify 
from docker import DockerClient

client = DockerClient()

def image_list():
    images = client.images.list()

    def get_image_sort_key(image):
        if image.attrs['RepoTags']:
            return image.attrs['RepoTags'][0].lower()
        else:
            return ''

    images = sorted(images, key=get_image_sort_key)
    return render_template(
        'images.html', title='images', 
        images=images)

def image_details(image_id):
    image = client.images.get(image_id)
    return render_template('image.html', image=image)

def image_list_data():
    images = client.images.list()
    return jsonify([{
        'id': image.id,
        'tags': image.tags,
        'created_at': image.attrs['Created'],
        'size': image.attrs['Size'],
        'virtual_size': image.attrs['VirtualSize']
    } for image in images])
