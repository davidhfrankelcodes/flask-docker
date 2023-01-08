from flask import Blueprint, render_template
from docker import DockerClient
client = DockerClient(base_url='unix://var/run/docker.sock')

bp = Blueprint('base', __name__)

@bp.route('/', methods=['GET'])
def index():
    containers = client.containers.list()
    return render_template(
        'index.html', title='Home', 
        containers=containers)
