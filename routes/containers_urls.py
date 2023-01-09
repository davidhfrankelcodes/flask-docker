from flask import Blueprint
from apis.containers import (
    container_details, 
    container_list
)

bp = Blueprint('containers', __name__)

@bp.route('/containers/', methods=['GET'])
def containers_app():
    return container_list()

@bp.route('/containers/<container_id>/', methods=['GET'])
def container_app(container_id):
    return container_details(container_id)

