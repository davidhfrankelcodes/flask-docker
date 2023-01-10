from flask import Blueprint, render_template
from jinja2.utils import markupsafe
from docker import DockerClient
import markdown

bp = Blueprint('base', __name__)

@bp.route('/', methods=['GET'])
def index():
    with open("README.md", "r") as f:
        md = f.read()
    html = markdown.markdown(md)
    return render_template(
        'markdown.html', title='Home', 
        content=markupsafe.Markup(html))
