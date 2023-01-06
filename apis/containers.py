from flask import render_template, jsonify, request 
from docker.errors import ImageNotFound
from docker import DockerClient

client = DockerClient()

def container_list():
    containers = client.containers.list()
    containers = sorted(containers, key=lambda c: c.name.lower())
    return render_template(
        'containers.html', title='containers', 
        containers=containers)

def container_details(container_id):
    container = client.containers.get(container_id)
    return render_template('container.html', container=container)


def container_list_data():
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
