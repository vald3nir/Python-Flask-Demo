from flask import Blueprint, request

from src.apis.blueprints.users.use_cases import *

user_blueprint = Blueprint('user_blueprint', __name__)


@user_blueprint.route('/users', methods=['GET'])
def router_list_all_user():
    return list_all_user()


@user_blueprint.route('/users', methods=['POST'])
def router_create_new_user():
    """
    body:
    {
        "name": "vald3nir",
        "password": "12345678",
        "email": "vald3nir@gmail.com",
        "language": "pt-br"
    }
    """
    return create_new_user(data_json=request.get_json())


@user_blueprint.route('/users/<user_id>', methods=['PUT'])
def router_update_user(user_id):
    """
    parameters:
    "user_id" : "user_524347ed-8312-4ee7-98dd-5aedc292c485"
    body:
    {
        "name": "severino",
        "email": "vald3nir@gmail.com",
        "language": "pt-br"
    }
    """
    return update_user(data_json=request.get_json(), user_id=user_id)
