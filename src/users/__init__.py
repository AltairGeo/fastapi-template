from .manager import auth_backend, get_user_manager
from fastapi_users import FastAPIUsers
from .models import User



fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend]
)