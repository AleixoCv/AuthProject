from fastapi import FastAPI, Depends
from auth import get_current_user
from models import User

app = FastAPI()

@app.post("/auth/me")
def auth_me(user: User = Depends(get_current_user)):
    return {
        "user": user,
        "ping": "Pong"
    }
