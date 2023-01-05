import os
from flask import Flask, jsonify
from docker import DockerClient

app = Flask(__name__)
client = DockerClient(base_url='unix://var/run/docker.sock')

@app.route('/v1/images/')
def images():
    images = client.images.list()
    return jsonify([{'id': image.id, 'tags': image.tags} for image in images])

@app.route('/v1/containers/')
def containers():
    containers = client.containers.list()
    return jsonify([{'id': container.id, 'name': container.name} for container in containers])

@app.route('/v1/networks/')
def networks():
    networks = client.networks.list()
    return jsonify([{'id': network.id, 'name': network.name} for network in networks])

@app.route('/v1/volumes/')
def volumes():
    volumes = client.volumes.list()
    return jsonify([{'id': volume.id, 'name': volume.name} for volume in volumes])
