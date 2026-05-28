from typing import Optional
from db.models import User


def create_user(
    username: str,
    password: str,
    email: Optional[str] = None,
    first_name: Optional[str] = None,
    last_name: Optional[str] = None,
) -> User:
    # Збираємо лише ті необов'язкові аргументи, які були передані
    kwargs = {}
    if email is not None:
        kwargs["email"] = email
    if first_name is not None:
        kwargs["first_name"] = first_name
    if last_name is not None:
        kwargs["last_name"] = last_name

    return User.objects.create_user(
        username=username,
        password=password,
        **kwargs
    )


def get_user(user_id: int) -> User:
    return User.objects.get(id=user_id)


def update_user(
    user_id: int,
    username: Optional[str] = None,
    password: Optional[str] = None,
    email: Optional[str] = None,
    first_name: Optional[str] = None,
    last_name: Optional[str] = None,
) -> User:
    user = User.objects.get(id=user_id)

    if username:
        user.username = username
    if password:
        user.set_password(password)
    if email:
        user.email = email
    if first_name:
        user.first_name = first_name
    if last_name:
        user.last_name = last_name

    user.save()
    return user
