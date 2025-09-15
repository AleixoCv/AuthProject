from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from models import User

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Simulação de um "banco de dados" de usuários
fake_users_db = {
    "johndoe": {
        "username": "johndoe",
        "email": "johndoe@example.com"
    }
}

def get_current_user(token: str = Depends(oauth2_scheme)) -> User:
    # Aqui você faria a validação real do token
    user_data = fake_users_db.get("johndoe")
    if not user_data:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
        )
    return User(**user_data)
