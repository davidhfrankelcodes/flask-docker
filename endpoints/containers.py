from flask import render_template, jsonify, request
from docker.errors import ImageNotFound
from docker import DockerClient
from util import util

client = DockerClient()

def container_list():
    format = util.get_format_param()
    containers = client.containers.list()
    containers = sorted(containers, key=lambda c: c.name.lower())
    if format == 'app':
        response= render_template(
        'containers.html', title='containers', 
        containers=containers)
    elif format == 'api':
        response = jsonify([{
            'id': container.id,
            'name': container.name,
            'image': container.attrs['Config']['Image'],
            'command': container.attrs['Config']['Cmd'],
            'created_at': container.attrs['Created'],
            'status': container.attrs['State']['Status'],
            'ports': container.attrs['NetworkSettings']['Ports'],
            'labels': container.attrs['Config']['Labels']
        } for container in containers])
    return response

def container_details(container_id):
    format = util.get_format_param()
    container = client.containers.get(container_id)
    if format == 'app':
        response =  render_template('container.html', container=container)
    elif format == 'api':
        response = jsonify(container.attrs)
    return response
