import os
from flask import Flask, jsonify
from docker import DockerClient

app = Flask(__name__)
client = DockerClient(base_url='unix://var/run/docker.sock')

@app.route('/v1/images/')
def images():
    images = client.images.list()
    return jsonify([{
        'id': image.id,
        'tags': image.tags,
        'created_at': image.attrs['Created'],
        'size': image.attrs['Size'],
        'virtual_size': image.attrs['VirtualSize']
    } for image in images])

@app.route('/v1/containers/')
def containers():
    containers = client.containers.list()
    return jsonify([{
        'id': container.id,
        'name': container.name,
        'image': container.attrs['Config']['Image'],
        'command': container.attrs['Config']['Cmd'],
        'created_at': container.attrs['Created'],
        'status': container.attrs['State']['Status'],
        'ports': container.attrs['NetworkSettings']['Ports'],
        'labels': container.attrs['Config']['Labels']
    } for container in containers])

@app.route('/v1/networks/')
def networks():
    networks = client.networks.list()
    return jsonify([{
        'id': network.id,
        'name': network.name,
        'driver': network.attrs['Driver'],
        'scope': network.attrs['Scope'],
        'created_at': network.attrs['Created'],
        'ipam': network.attrs['IPAM'],
        'internal': network.attrs['Internal'],
        'attachable': network.attrs['Attachable'],
        'ingress': network.attrs['Ingress'],
        'enable_ipv6': network.attrs['EnableIPv6'],
        'options': network.attrs['Options']
    } for network in networks])

@app.route('/v1/volumes/')
def volumes():
    volumes = client.volumes.list()
    return jsonify([{
        'id': volume.id,
        'name': volume.name,
        'driver': volume.attrs['Driver'],
        'mountpoint': volume.attrs['Mountpoint'],
        'created_at': volume.attrs['CreatedAt'],
        'labels': volume.attrs['Labels'],
        'options': volume.attrs['Options']
    } for volume in volumes])
