from flask import render_template, jsonify
from docker import DockerClient
from util import util


client = DockerClient()

def network_list():
    format = util.get_format_param()
    networks = client.networks.list()
    def get_network_sort_key(network):
        return network.name.lower()
    networks = sorted(networks, key=get_network_sort_key)
    if format == 'app':
        response =  render_template(
            'networks.html', title='networks', 
            networks=networks)
    elif format == 'api':
        response = jsonify([{
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
    return response

def network_details(network_id):
    format = util.get_format_param()
    network = client.networks.get(network_id)
    if format == 'app':
        response =  render_template('network.html', network=network)
    elif format == 'api':
        response = jsonify(network.attrs)
    return response
