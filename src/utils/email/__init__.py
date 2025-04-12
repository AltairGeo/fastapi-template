from .config import conf
from fastapi_mail import FastMail

def get_fast_mail() -> FastMail:
    return FastMail(conf)

