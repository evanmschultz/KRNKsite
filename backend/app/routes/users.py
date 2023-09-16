import jwt
# from config.jwt_config import SECRET_KEY, ALGORITHM

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user_schema import (
    UserCreateSchema,
    UserInfoUpdateSchema,
    UpdatePasswordSchema,
    UserResponseSchema,
)
from config.database import get_db

# def create_access_token(data: dict, expires_delta: int): 
#     """
#     Create a JWT access token.

#     Args:
#         data (dict): The data to encode in the JWT.
#         expires_delta (int): An integer representing the number of minutes from the current time when the JWT should expire. This parameter is used to set the expiration time for the token.

#     Returns:
#         str: The encoded JWT.
#     """
#     to_encode = data.copy()
#     to_encode.update({"exp": expires_delta})
#     encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
#     return encoded_jwt

# def decode_token(token: str):
#     """
#     Decode a JWT access token.
    
#     Args:
#         token (str): The JWT to decode.
        
#         Returns:
#             dict: The decoded JWT.
#     """
#     try:
#         decoded_token = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
#         return decoded_token
#     except jwt.JWTError:
#         return None
    
router = APIRouter()


@router.post("/register/", response_model=UserCreateSchema)
def register_user(user_data: UserCreateSchema, db: Session = Depends(get_db)) -> dict:
    """
    Register a new user and generate a JWT token.

    Args:
        user_data (UserCreateSchema): The user details encapsulated in a Pydantic model.
        db (Session, optional): The database session. Defaults to `get_db()` dependency.

    Returns:
        dict: A dictionary containing the created user object and a JWT token.

    Raises:
        HTTPException: 400 status if email is already registered.
    """
    # Check if the email is already registered
    if db.query(User).filter_by(email=user_data.email).first():
        raise HTTPException(status_code=400, detail="Email already registered")

    # Hash the user's password
    hashed_password: str = User.hash_password(user_data.password)

    # Create a new user in the database
    db_user = User(
        first_name=user_data.first_name,
        last_name=user_data.last_name,
        email=user_data.email,
        password=hashed_password,
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    # Generate a JWT token for the newly registered user
    expires_delta = 3600  # Set the expiration time (1 hour in seconds)
    jwt_token = jwt.encode({"user_id": db_user.id}, SECRET_KEY, algorithm=ALGORITHM, expires_delta=expires_delta) # Create the JWT token

    print(f"User {db_user.email} has successfully registered.")
    print(f"Token: {jwt_token}")

    # Return the created user object and the JWT token in the response
    response_data = {
        "user": db_user,
        "token": jwt_token,
    }
    return response_data

@router.get("/{user_id}", response_model=UserResponseSchema)
def get_user_by_id(user_id: int, db: Session = Depends(get_db)) -> User:
    """
    Retrieve a user by ID.

    Args:
        user_id (int): The ID of the user to retrieve.
        db (Session, optional): The database session. Defaults to `get_db()` dependency.

    Returns:
        UserResponseSchema: The retrieved user details encapsulated in a Pydantic model.

    Raises:
        HTTPException: 404 status if user is not found.
    """
    user: User = db.query(User).filter_by(id=user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.get("/email/{user_email}", response_model=UserResponseSchema)
def get_user_by_email(user_email: str, db: Session = Depends(get_db)) -> User:
    """
    Retrieve a user by email address.

    Args:
        user_email (str): The email address of the user to retrieve.
        db (Session, optional): The database session. Defaults to `get_db()` dependency.

    Returns:
        UserResponseSchema: The retrieved user details encapsulated in a Pydantic model.

    Raises:
        HTTPException: 404 status if user is not found.
    """
    user: User = db.query(User).filter_by(email=user_email).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.put("/{user_id}/info", response_model=UserResponseSchema)
def update_user_info(
    user_id: int, user_data: UserInfoUpdateSchema, db: Session = Depends(get_db)
) -> User:
    """
    Update a user's personal information by ID.

    Args:
        user_id (int): The ID of the user to update.
        user_data (UserInfoUpdateSchema): The updated user details encapsulated in a Pydantic model.
        db (Session, optional): The database session. Defaults to `get_db()` dependency.

    Returns:
        UserResponseSchema: The updated user details encapsulated in a Pydantic model.

    Raises:
        HTTPException: 404 status if user is not found.
    """
    db_user = db.query(User).filter_by(id=user_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")

    db_user.first_name = user_data.first_name
    db_user.last_name = user_data.last_name
    db_user.email = user_data.email

    db.commit()
    db.refresh(db_user)

    return db_user


# TODO: Fix `422 Unprocessable Entity` error when updating password
# TODO: Confirm password hashing works and the password from the database is compared to the input password correctly
# TODO: Throw error if the `current_password` doesn't match the password in the database
@router.put("/{user_id}/update_password", response_model=UserResponseSchema)
def update_user_password(
    user_id: int, password_data: UpdatePasswordSchema, db: Session = Depends(get_db)
) -> User:
    """
    Update a user's password by ID.

    Args:
        user_id (int): The ID of the user to update.
        password_data (UserUpdatePasswordSchema): The updated user password encapsulated in a Pydantic model.
            {
                "current_password": "string",
                "password": "string",
                "confirm_password": "string"
            }
        db (Session, optional): The database session. Defaults to `get_db()` dependency.

    Returns:
        UserResponseSchema: The updated user details encapsulated in a Pydantic model.

    Raises:
        HTTPException: 404 status if user is not found.
        HTTPException: 400 status if current password is incorrect.
    """
    db_user = db.query(User).filter_by(id=user_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")

    # Verify the current password
    if not User.verify_password(password_data.current_password, db_user.password):
        raise HTTPException(status_code=400, detail="Incorrect current password")

    # Update the password
    db_user.password = User.hash_password(password_data.password)

    db.commit()
    db.refresh(db_user)

    return db_user


@router.delete("/{user_id}/delete", response_model=UserResponseSchema)
def delete_user(user_id: int, db: Session = Depends(get_db)) -> dict[str, str]:
    """
    Delete a user by ID.

    Args:
        user_id (int): The ID of the user to delete.
        db (Session, optional): The database session. Defaults to `get_db()` dependency.

    Returns:
        dict: A dictionary containing a "detail" key with a message indicating the user was deleted.

    Raises:
        HTTPException: 404 status if user is not found.
    """
    db_user: User | None = db.query(User).filter_by(id=user_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")

    db.delete(db_user)
    db.commit()

    return {f"detail": f"User {user_id} was deleted successfully!"}
