from flask import Blueprint
from apis.containers import (container_details, 
    container_list, container_data, container_list_data)

bp = Blueprint('containers', __name__)

@bp.route('/containers/', methods=['GET'])
def containers_app():
    return container_list()

@bp.route('/containers/<container_id>/', methods=['GET'])
def container_app(container_id):
    return container_details(container_id)

@bp.route('/api/containers/', methods=['GET'])
def containers_api():
    return container_list_data()

@bp.route('/api/containers/<container_id>/', methods=['GET'])
def container_api(container_id):
    return container_data(container_id)
