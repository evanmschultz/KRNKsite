from datetime import datetime
from sqlalchemy import Boolean, Column, Integer, String, DateTime, Table, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from passlib.hash import bcrypt
from app.models.associations import Base, user_topics_association


class User(Base):
    """
    The User class is a model for storing user information and includes methods
    for hashing passwords, checking passwords, and other CRUD operations.
    """

    __tablename__: str = "users"

    id: int = Column(Integer, primary_key=True, index=True, autoincrement=True)  # type: ignore
    first_name: str = Column(String(255))  # type: ignore
    last_name: str = Column(String(255))  # type: ignore
    email: str = Column(String(255), unique=True)  # type: ignore
    password: str = Column(String(255))  # type: ignore
    is_premium_user: bool = Column(Boolean, default=False)  # type: ignore

    created_at: datetime = Column(DateTime, default=datetime.utcnow)  # type: ignore
    updated_at: datetime = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)  # type: ignore

    # Relationship to Topic
    topics = relationship("Topic", secondary=user_topics_association)

    @staticmethod
    def hash_password(password: str) -> str:
        """
        Hashes the given password using bcrypt and returns the hashed password.

        Args:
            password (str): The plain-text password to hash.

        Returns:
            str: The hashed password.
        """
        return bcrypt.hash(password)

    @staticmethod
    def verify_password(password: str, hashed_password: str) -> bool:
        """
        Verifies a password against its hashed version.

        Args:
            password (str): The plain-text password to verify.
            hashed_password (str): The hashed password to compare against.

        Returns:
            bool: True if the password matches, False otherwise.
        """
        return bcrypt.verify(password, hashed_password)
