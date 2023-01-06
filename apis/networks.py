from flask import render_template, jsonify
from docker import DockerClient

client = DockerClient()

def network_list():
    networks = client.networks.list()
    def get_network_sort_key(network):
        return network.name.lower()

    networks = sorted(networks, key=get_network_sort_key)
    return render_template(
        'networks.html', title='networks', 
        networks=networks)

def network_details(network_id):
    network = client.networks.get(network_id)
    return render_template('network.html', network=network)

def network_list_data():
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
