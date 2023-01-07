from flask import Flask, render_template
from docker import DockerClient

from apis.containers import (container_details, 
    container_list, container_data, container_list_data, )
from apis.images import (image_details, 
    image_list, image_data, image_list_data, )
from apis.networks import (network_details, 
    network_list, network_data, network_list_data,)
from apis.volumes import (volume_details, 
    volume_list, volume_data, volume_list_data)

app = Flask(__name__)
client = DockerClient(base_url='unix://var/run/docker.sock')

@app.route('/')
def index():
    containers = client.containers.list()
    return render_template(
        'index.html', title='Home', 
        containers=containers)

# CONTAINERS
@app.route('/containers/')
def containers_app():
    return container_list()

@app.route('/containers/<container_id>/')
def container_app(container_id):
    return container_details(container_id)

@app.route('/api/containers/', methods=['GET', 'POST'])
def containers_api():
    return container_list_data()

@app.route('/api/containers/<container_id>/')
def container_api(container_id):
    return container_data(container_id)

# IMAGES
@app.route('/images/')
def images_app():
    return image_list()

@app.route('/images/<image_id>/')
def image_app(image_id):
    return image_details(image_id)

@app.route('/api/images/')
def images_api():
    return image_list_data()

@app.route('/api/images/<image_id>/')
def image_api(image_id):
    return image_data(image_id)

# NETWORKS
@app.route('/networks/')
def networks_app():
    return network_list()

@app.route('/networks/<network_id>/')
def network_app(network_id):
    return network_details(network_id)

@app.route('/api/networks/')
def networks_api():
    return network_list_data()

@app.route('/api/networks/<network_id>/')
def network_api(network_id):
    return network_data(network_id)

# VOLUMES
@app.route('/volumes/')
def volumes_app():
    return volume_list()

@app.route('/volumes/<volume_id>/')
def volume_app(volume_id):
    return volume_details(volume_id)

@app.route('/api/volumes/')
def volumes_api():
    return volume_list_data()

@app.route('/api/volumes/<volume_id>/')
def volume_api(volume_id):
    return volume_data(volume_id)
