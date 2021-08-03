from datetime import datetime, timedelta

import jwt

from src.apis.responses.auth_responses import response_password_wrong, response_password_updated
from src.apis.responses.user_responses import response_user_not_found
from src.apis.utils.auth import create_password_hash, compare_password_hash
from src.db.daos import UserDao


# --------------------------------------------------------------------

def login(data_json):
    language = data_json.get("language", None)
    db = UserDao()

    try:

        user_db = db.find_one({"email": data_json["email"]})

        user_password_param = create_password_hash(data_json["password"])

        if compare_password_hash(user_db["password"], user_password_param):
            data_exp = datetime.utcnow() + timedelta(minutes=60 * 60 * 60)
            token = jwt.encode({'user_id': user_db["user_id"], 'exp': data_exp}, 'Th1s1ss3cr3t')
            return {'user_id': user_db["user_id"], 'token': token.decode('UTF-8')}, 200

    except Exception as e:
        print(e)

    return response_user_not_found(language)


# --------------------------------------------------------------------


def update_user_password(data_json, user_id):
    language = data_json.get("language", None)
    db = UserDao()

    try:

        user_db = db.find_one({"user_id": user_id})

        if not compare_password_hash(user_db["password"], data_json["password"]):
            return response_password_wrong(language)

        db.update(
            query={"user_id": user_id}, new_value={
                "$set": {
                    "password": create_password_hash(data_json['new_password'])
                }
            })
        return response_password_updated(language)

    except Exception as e:
        print(e)

    return response_user_not_found(language)
