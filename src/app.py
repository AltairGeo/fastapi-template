import uvicorn
from fastapi import FastAPI
from src.api import all_routers
from fastapi.middleware.cors import CORSMiddleware
from .config import settings

app = FastAPI()

[app.include_router(router) for router in all_routers]


app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/')
async def index() -> str:
    return "<p>Hello world!</p>"



if __name__ == "__main__":
    uvicorn.run(app="app:app", reload=True)