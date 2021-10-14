import jinja2.exceptions
from flask import Blueprint, render_template

home_blueprint = Blueprint('home_blueprint', __name__)


@home_blueprint.route('/')
def home():
    return render_template('index.html')


@home_blueprint.route('/<pagename>')
def admin(pagename):
    return render_template(pagename + '.html')


@home_blueprint.errorhandler(jinja2.exceptions.TemplateNotFound)
def template_not_found(e):
    return not_found(e)


@home_blueprint.errorhandler(404)
def not_found(e):
    return render_template('404.html')
