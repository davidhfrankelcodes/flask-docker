from flask import Blueprint
from endpoints.images import (
    image_details, 
    image_list
)

bp = Blueprint('images', __name__)

@bp.route('/images/', methods=['GET'])
def images_app():
    return image_list()

@bp.route('/images/<image_id>/', methods=['GET'])
def image_app(image_id):
    return image_details(image_id)
