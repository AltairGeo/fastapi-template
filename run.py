from src.app import app

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("src.app:app", reload=True)