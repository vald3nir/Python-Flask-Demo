from src.apis.factory.user_factory import *
from src.apis.responses.user_responses import *
from src.db.daos import UserDao


# --------------------------------------------------------------------

def list_all_user():
    users = []
    for data_json in UserDao().find_all({}):
        users.append(create_user_dto(data_json).to_json())
    return response_list_all_users(users)


# --------------------------------------------------------------------

def create_new_user(data_json):
    language = data_json.get("language", None)

    try:

        db = UserDao()

        if db.find_one({"email": data_json["email"]}):
            return response_user_created(language)

        user_dto = create_new_user_dto(data_json)
        db.insert_one(user_dto.to_json())

        return response_new_user_created(language)

    except Exception as e:
        print(e)
        return response_user_api_fail(language)


# --------------------------------------------------------------------

def update_user(data_json, user_id):
    language = data_json.get("language", None)

    db = UserDao()

    if not db.find_one({"user_id": user_id}):
        return response_user_not_found(language)

    data_mutable = create_user_dto(data_json).get_data_mutable()
    db.update(query={"user_id": user_id}, new_value={"$set": data_mutable})
    return response_user_updated(language)

# --------------------------------------------------------------------
