from flask import Flask

from routes.markdown import bp as base_bp
from routes.containers_urls import bp as containers_bp
from routes.images_urls import bp as images_bp
from routes.networks_urls import bp as networks_bp
from routes.volumes_urls import bp as volumes_bp

app = Flask(__name__)
app.register_blueprint(base_bp)
app.register_blueprint(containers_bp)
app.register_blueprint(images_bp)
app.register_blueprint(networks_bp)
app.register_blueprint(volumes_bp)
