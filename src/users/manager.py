from fastapi_users.authentication import AuthenticationBackend
from .depends import get_database_stategy, get_user_db
from .models import User
from fastapi_users import BaseUserManager, IntegerIDMixin
from src.config import settings
from fastapi import Depends, Request, BackgroundTasks
from typing import Optional
from .transport import bearer_transport
from src.utils.email import get_fast_mail
from typing import Optional
from fastapi_mail import FastMail, MessageSchema, MessageType



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
        self, user: User, token: str, request: Optional[Request] = None, background_tasks: BackgroundTasks = None
    ):  
        fast_mail = get_fast_mail()
        message = MessageSchema(
                subject="FastAPI Template",
                recipients=[user.email], 
                template_body={"reset_url": str(request.base_url) + f'pages/reset-password?token={token}'}, 
                subtype=MessageType.html
            )

        await fast_mail.send_message(message=message, template_name="email/forgot_mail.html")


    async def on_after_request_verify(
        self, user: User, token: str, request: Optional[Request] = None
    ):
        fast_mail = get_fast_mail()
        message = MessageSchema(
            subject="FastAPI Template",
            recipients=[user.email],
            template_body={"verify_url": str(request.base_url) + f"pages/verify?token={token}"},
            subtype=MessageType.html
        )
        await fast_mail.send_message(message=message, template_name="email/verify_mail.html")





async def get_user_manager(user_db=Depends(get_user_db)):
    yield UserManager(user_db)
