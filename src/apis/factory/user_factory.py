from src.apis.utils.auth import create_password_hash, create_user_id
from src.apis.utils.date import get_today_date_utc
from src.db.entities import UserDTO


def create_new_user_dto(data_json):
    return UserDTO(
        user_id=create_user_id(),
        name=data_json.get('name', None),
        password=create_password_hash(data_json.get('password', None)),
        email=data_json.get('email', None),
        created_at=get_today_date_utc()
    )


def create_user_dto(data_json):
    return UserDTO(
        user_id=data_json.get("user_id", None),
        name=data_json.get('name', None),
        password=data_json.get('password', None),
        email=data_json.get('email', None),
        created_at=str(data_json.get('created_at', None)),
    )
