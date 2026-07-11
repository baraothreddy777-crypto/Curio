from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {
        "app": "Curio",
        "status": "Running",
        "message": "Welcome to Curio AI!"
    }

