from flask import render_template, jsonify, request
from docker import DockerClient

client = DockerClient()

def volume_list():
    volumes = client.volumes.list()
    def get_volume_sort_key(volume):
        return volume.name.lower()

    volumes = sorted(volumes, key=get_volume_sort_key)
    return render_template(
        'volumes.html', title='volumes', 
        volumes=volumes)

def volume_details(volume_id):
    format = request.args.get('format', 'app')
    volume = client.volumes.get(volume_id)
    if format == 'app':
        response =  render_template('volume.html', volume=volume)
    elif format == 'api':
        response = jsonify(volume.attrs)
    return response

def volume_list_data():
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
