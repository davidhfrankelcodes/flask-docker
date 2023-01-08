from flask import Flask, render_template
from docker import DockerClient

from routes.containers_urls import bp as containers_bp
from routes.images_urls import bp as images_bp
from routes.networks_urls import bp as networks_bp
from routes.volumes_urls import bp as volumes_bp

client = DockerClient(base_url='unix://var/run/docker.sock')

app = Flask(__name__)
app.register_blueprint(containers_bp)
app.register_blueprint(images_bp)
app.register_blueprint(networks_bp)
app.register_blueprint(volumes_bp)

@app.route('/')
def index():
    containers = client.containers.list()
    return render_template(
        'index.html', title='Home', 
        containers=containers)
