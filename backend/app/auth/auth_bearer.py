from fastapi import Depends, HTTPException, FastAPI
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from datetime import timedelta
from app.jwt_utils import decode_token, create_access_token
from app.models.user import User
from config.jwt_config import ACCESS_TOKEN_EXPIRE_MINUTES
from sqlalchemy.orm import Session

# Create a FastAPI app instance
app = FastAPI()

# OAuth2PasswordBearer is used to get the token from the request headers
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Simulated user authentication function based on email
def authenticate_user(db: Session, email: str, password: str):
    user = db.query(User).filter_by(email=email).first()
    if user is None or not user.verify_password(password):
        return None
    return user

# Simulated function to get user by email (you should replace this with your actual user retrieval code)
def get_user_by_email(db: Session, email: str):
    return db.query(User).filter_by(email=email).first()

# ...

# Route to authenticate and generate a token
@app.post("/token")
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(db, form_data.email, form_data.password)
    if user is None:
        raise HTTPException(status_code=400, detail="Incorrect email or password")
    
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(data={"sub": user.email}, expires_delta=access_token_expires)
    
    return {"access_token": access_token, "token_type": "bearer"}

# ...

# Function to get the current user from the token
def get_current_user(db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)) -> User:
    decoded_token = decode_token(token)
    if decoded_token is None:
        raise HTTPException(status_code=401, detail="Could not validate credentials")
    
    email = decoded_token.get("sub")
    user = get_user_by_email(db, email)
    if user is None:
        raise HTTPException(status_code=401, detail="User not found")
    
    return user

# ...

# Route that requires authentication
@app.get("/protected-route/")
async def protected_route(current_user: User = Depends(get_current_user)):
    return {"message": "This is a protected route"}
