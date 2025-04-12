from fastapi import APIRouter, Request
from src.utils.templates import templates


router = APIRouter(prefix="/pages", tags=["pages", "auth"])


@router.get("/reset-password")
async def reset_password_page(token: str, request: Request):
    return templates.TemplateResponse("email/forgot.html", {"token": token, "request": request})

@router.get("/verify")
async def reset_password_page(token: str, request: Request):
    return templates.TemplateResponse("email/verify.html", {"token": token, "request": request})