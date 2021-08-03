import uuid

from werkzeug.security import generate_password_hash, check_password_hash


def create_user_id():
    return 'user_' + str(uuid.uuid4())


def create_password_hash(password):
    return generate_password_hash(password, method='sha256')


def compare_password_hash(p1, p2):
    return check_password_hash(p1, p2)
