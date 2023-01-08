from flask import Blueprint
from apis.networks import (network_details, 
    network_list, network_data, network_list_data)

bp = Blueprint('networks', __name__)

@bp.route('/networks/', methods=['GET'])
def networks_app():
    return network_list()

@bp.route('/networks/<network_id>/', methods=['GET'])
def network_app(network_id):
    return network_details(network_id)

@bp.route('/api/networks/', methods=['GET'])
def networks_api():
    return network_list_data()

@bp.route('/api/networks/<network_id>/', methods=['GET'])
def network_api(network_id):
    return network_data(network_id)
