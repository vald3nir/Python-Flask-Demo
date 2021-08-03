from flask import Blueprint, request

from src.apis.blueprints.auth.use_cases import login, update_user_password

auth_blueprint = Blueprint('auth_blueprint', __name__)


@auth_blueprint.route('/login', methods=['POST'])
def route_login():
    """
    body:
    {
        "password": "12345678",
        "email": "vald3nir@gmail.com"
    }
    """
    return login(request.get_json())


@auth_blueprint.route('/users/<user_id>/password', methods=['PUT'])
def router_update_user_password(user_id):
    """
    parameters:
    "user_id" : "user_524347ed-8312-4ee7-98dd-5aedc292c485"
    body:
    {
        "password": "12345678",
        "new_password": "11111111",
        "language": "pt-br"
    }
    """
    data_json = request.get_json()
    return update_user_password(data_json, user_id)