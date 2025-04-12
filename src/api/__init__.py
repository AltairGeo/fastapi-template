from .users import router as users
from .auth_pages import router as auth_pages

all_routers = [
    users,
    auth_pages,
]