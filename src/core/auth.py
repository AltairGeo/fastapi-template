from fastapi_users.authentication import BearerTransport, AuthenticationBackend
from .db import get_database_stategy, get_user_db
from .db.models import User
from fastapi_users import BaseUserManager, IntegerIDMixin
from src.config import settings
from fastapi import Depends, Request
from typing import Optional



bearer_transport = BearerTransport(tokenUrl="auth/jwt/login")

auth_backend = AuthenticationBackend(
    name="db_auth",
    transport=bearer_transport,
    get_strategy=get_database_stategy,
)


class UserManager(IntegerIDMixin, BaseUserManager[User, int]):
    reset_password_token_secret = settings.app_secret_reset_password
    verification_token_secret = settings.app_secret_verify

    async def on_after_register(self, user: User, request: Optional[Request] = None):
        print(f"User {user.id} has registered.")

    async def on_after_forgot_password(
        self, user: User, token: str, request: Optional[Request] = None
    ):
        print(f"User {user.id} has forgot their password. Reset token: {token}")

    async def on_after_request_verify(
        self, user: User, token: str, request: Optional[Request] = None
    ):
        print(f"Verification requested for user {user.id}. Verification token: {token}")



async def get_user_manager(user_db=Depends(get_user_db)):
    yield UserManager(user_db)