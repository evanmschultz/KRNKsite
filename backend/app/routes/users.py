from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user_schema import (
    UserCreateSchema,
    UserLoginSchema,
    UserInfoUpdateSchema,
    UpdatePasswordSchema,
    UserResponseSchema,
    UserLogoutSchema
)
from app.models.topic import Topic
from app.schemas.topic_schema import TopicResponseSchema

from config.database import get_db
from app.jwt_utils import create_access_token, decode_token

import logging
logger = logging.getLogger(__name__)

router = APIRouter()


import logging

logger = logging.getLogger(__name__)

@router.post("/register/", response_model=UserCreateSchema)
def register_user(user_data: UserCreateSchema, db: Session = Depends(get_db)) -> User:
    """
    Register a new user.

    Args:
        user_data (UserCreateSchema): The user details encapsulated in a Pydantic model.
        db (Session, optional): The database session. Defaults to `get_db()` dependency.

    Returns:
        User: The created user object.

    Raises:
        HTTPException: 400 status if email is already registered.
    """
    try:
        if db.query(User).filter_by(email=user_data.email).first():
            logger.error("Email already registered: %s", user_data.email)
            raise HTTPException(status_code=400, detail="Email already registered")

        hashed_password: str = User.hash_password(user_data.password)
        db_user = User(
            first_name=user_data.first_name,
            last_name=user_data.last_name,
            email=user_data.email,
            password=hashed_password,
        )
        db.add(db_user)
        db.commit()
        db.refresh(db_user)

        # # Create a JWT token
        # access_token_expires = 60  # minutes
        # access_token = create_access_token(
        #     data={"sub": db_user.email}, expires_delta=access_token_expires
        # )

        # return {"user": db_user, "access_token": access_token, "token_type": "bearer"}

        return db_user
    

    except Exception as e:
        logger.error("Error registering user: %s", str(e))
        raise




@router.post("/login", response_model=UserResponseSchema)
def login_user(user_data: UserLoginSchema, db: Session = Depends(get_db)) -> User:
    db_user = db.query(User).filter_by(email=user_data.email).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="Incorrect email or password.")

    if not User.verify_password(user_data.password, db_user.password):
        raise HTTPException(status_code=400, detail="Incorrect email or password.")

    # # Create a JWT token
    # access_token_expires = 60  # minutes
    # access_token = create_access_token(
    #     data={"sub": db_user.email}, expires_delta=access_token_expires
    # )

    user_response = {
        "id": db_user.id,
        "first_name": db_user.first_name,
        "last_name": db_user.last_name,
        "email": db_user.email,
        "is_premium_user": db_user.is_premium_user,
        "created_at": db_user.created_at,
        "updated_at": db_user.updated_at,
        # "access_token": access_token,
        # "token_type": "bearer",
    }

    return user_response

@router.get("/user/{user_id}", response_model=UserResponseSchema)
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
        raise HTTPException(status_code=401, detail="Incorrect current password")

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

@router.post("/logout", response_model=UserLogoutSchema)
def logout_user(db: Session = Depends(get_db)):
    """
    Logout the currently authenticated user.

    Args:
        db (Session, optional): The database session. Defaults to `get_db()` dependency.

    Returns:
        dict: A dictionary containing a "detail" key with a message indicating the user was logged out.

    Raises:
        HTTPException: 404 status if user is not found or other errors.
    """
    # Assuming you have a method to get the current authenticated user's ID
    user_id = get_current_user_id()

    db_user: User | None = db.query(User).filter_by(id=user_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")

    # Handle your logout logic here. E.g., invalidate a token, clear a session, etc.

    db.commit()

    return {"detail": f"User {user_id} was logged out successfully!"}