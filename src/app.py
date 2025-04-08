import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def index() -> str:
    return "<p>Hello world!</p>"



if __name__ == "__main__":
    uvicorn.run(app="app:app", reload=True)