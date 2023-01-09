from flask import Blueprint
from apis.volumes import (
    volume_details, 
    volume_list, 
    volume_list_data)

bp = Blueprint('volumes', __name__)

@bp.route('/volumes/', methods=['GET'])
def volumes_app():
    return volume_list()

@bp.route('/volumes/<volume_id>/', methods=['GET'])
def volume_app(volume_id):
    return volume_details(volume_id)

@bp.route('/api/volumes/', methods=['GET'])
def volumes_api():
    return volume_list_data()

