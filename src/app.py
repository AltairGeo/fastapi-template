import uvicorn
from fastapi import FastAPI
from api import all_routers

app = FastAPI()

[app.include_router(router) for router in all_routers]

@app.get('/')
async def index() -> str:
    return "<p>Hello world!</p>"



if __name__ == "__main__":
    uvicorn.run(app="app:app", reload=True)