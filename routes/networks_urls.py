from flask import Blueprint
from endpoints.networks import (
    network_details, 
    network_list, 
)

bp = Blueprint('networks', __name__)

@bp.route('/networks/', methods=['GET'])
def networks_app():
    return network_list()

@bp.route('/networks/<network_id>/', methods=['GET'])
def network_app(network_id):
    return network_details(network_id)

