from flask import Blueprint
from endpoints.volumes import (
    volume_details, 
    volume_list
)    

bp = Blueprint('volumes', __name__)

@bp.route('/volumes/', methods=['GET'])
def volumes_app():
    return volume_list()

@bp.route('/volumes/<volume_id>/', methods=['GET'])
def volume_app(volume_id):
    return volume_details(volume_id)
