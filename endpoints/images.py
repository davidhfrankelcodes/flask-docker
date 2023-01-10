from flask import render_template, jsonify
from docker import DockerClient
from util import flask_util

client = DockerClient()

def image_list():
    format = flask_util.get_format_param()
    images = client.images.list()
    def get_image_sort_key(image):
        if image.attrs['RepoTags']:
            return image.attrs['RepoTags'][0].lower()
        else:
            return ''
    images = sorted(images, key=get_image_sort_key)
    if format == 'app':
        response = render_template(
        'images.html', title='images', 
        images=images)
    elif format == 'api':
        response = jsonify([{
        'id': image.id,
        'tags': image.tags,
        'created_at': image.attrs['Created'],
        'size': image.attrs['Size'],
        'virtual_size': image.attrs['VirtualSize']
    } for image in images])
    return response

def image_details(image_id):
    format = flask_util.get_format_param()
    image = client.images.get(image_id)
    if format == 'app':
        response =  render_template('image.html', image=image)
    elif format == 'api':
        response = jsonify(image.attrs)
    return response

