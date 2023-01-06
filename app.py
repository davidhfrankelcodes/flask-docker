from flask import Flask, jsonify, request, render_template
from docker import DockerClient
from docker.errors import ImageNotFound


app = Flask(__name__)
client = DockerClient(base_url='unix://var/run/docker.sock')

@app.route('/')
def index():
    containers = client.containers.list()
    return render_template(
        'index.html', title='Home', 
        containers=containers)

@app.route('/containers/')
def containers_app():
    containers = client.containers.list()
    print([container.id for container in containers])
    return render_template(
        'containers.html', title='containers', 
        containers=containers)

@app.route('/containers/<container_id>/')
def container_app(container_id):
    container = client.containers.get(container_id)
    return render_template('container.html', container=container)

@app.route('/images/')
def images_app():
    images = client.images.list()
    return render_template(
        'images.html', title='images', 
        images=images)

@app.route('/images/<image_id>/')
def image_app(image_id):
    image = client.images.get(image_id)
    return render_template('image.html', image=image)

@app.route('/networks/')
def networks_app():
    networks = client.networks.list()
    return render_template(
        'networks.html', title='networks', 
        networks=networks)

@app.route('/networks/<network_id>/')
def network_app(network_id):
    network = client.networks.get(network_id)
    return render_template('network.html', network=network)

@app.route('/volumes/')
def volumes_app():
    volumes = client.volumes.list()
    return render_template(
        'volumes.html', title='volumes', 
        volumes=volumes)

@app.route('/volumes/<volume_id>/')
def volume_app(volume_id):
    volume = client.volumes.get(volume_id)
    return render_template('volume.html', volume=volume)


@app.route('/v1/containers/', methods=['GET', 'POST'])
def containers():
    if request.method == 'POST':
        image = request.args.get('image')
        if image is None:
            return "Error: 'image' parameter is required", 400

        # Check if the image exists locally
        try:
            client.images.get(image)
        except ImageNotFound:
            # If the image was not found locally, try to pull it from Docker Hub
            try:
                client.images.pull(image)
            except:
                return "Error: Could not find the specified image", 404

        # Create a container from the image
        container = client.containers.create(image)
        return f"Successfully created container with ID {container.id}"
    elif request.method == 'GET':
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
