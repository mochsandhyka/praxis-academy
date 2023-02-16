from flask import Flask, Blueprint, render_template, abort
from jinja2 import TemplateNotFound

app = Flask(__name__)

simple_page = Blueprint('simple_page', __name__ ,
                        template_folder='templates')

@simple_page.route('/', defaults={'page': 'index'})
@simple_page.route('/<page>')
def show(page):
    try:
        return render_template(f"pages/{page}.html")
    except TemplateNotFound:
        abort(404)