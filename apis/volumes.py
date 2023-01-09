from flask import render_template, jsonify
from docker import DockerClient
from . import util

client = DockerClient()

def volume_list():
    format = util.get_format_param()
    volumes = client.volumes.list()
    def get_volume_sort_key(volume):
        return volume.name.lower()
    volumes = sorted(volumes, key=get_volume_sort_key)
    if format == 'app':
        response =  render_template(
            'volumes.html', title='volumes', 
            volumes=volumes)
    elif format == 'api':
        response = jsonify([{
        'id': volume.id,
        'name': volume.name,
        'driver': volume.attrs['Driver'],
        'mountpoint': volume.attrs['Mountpoint'],
        'created_at': volume.attrs['CreatedAt'],
        'labels': volume.attrs['Labels'],
        'options': volume.attrs['Options']
    } for volume in volumes])
    return response

def volume_details(volume_id):
    format = util.get_format_param()
    volume = client.volumes.get(volume_id)
    if format == 'app':
        response =  render_template('volume.html', volume=volume)
    elif format == 'api':
        response = jsonify(volume.attrs)
    return response
