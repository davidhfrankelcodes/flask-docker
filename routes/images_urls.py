from flask import Blueprint
from apis.images import (image_details, 
    image_list, image_data, image_list_data)

bp = Blueprint('images', __name__)

@bp.route('/images/', methods=['GET'])
def images_app():
    return image_list()

@bp.route('/images/<image_id>/', methods=['GET'])
def image_app(image_id):
    return image_details(image_id)

@bp.route('/api/images/', methods=['GET'])
def images_api():
    return image_list_data()

@bp.route('/api/images/<image_id>/', methods=['GET'])
def image_api(image_id):
    return image_data(image_id)
