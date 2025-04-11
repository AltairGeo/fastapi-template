from fastapi_users.authentication import BearerTransport, AuthenticationBackend
from .db import get_database_stategy


bearer_transport = BearerTransport(tokenUrl="auth/jwt/login")

auth_backend = AuthenticationBackend(
    name="db_auth",
    transport=bearer_transport,
    get_strategy=get_database_stategy,
)

