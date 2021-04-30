from werkzeug.security import safe_str_cmp
from models.user import User


def authenticate(username: str, password: str) -> User:
    user = User.find_by_username(username)
    if user is not None and safe_str_cmp(user.password, password):
        return user


def identity(payload: dict) -> User:
    user_id = payload.get('identity', None)
    user = User.find_by_id(user_id)
    if user_id is not None and user is not None:
        return user

