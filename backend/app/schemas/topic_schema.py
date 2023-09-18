from datetime import datetime
import re
from pydantic import BaseModel, Field


class TopicBase(BaseModel):
    """
    Pydantic model for serializing user data returned by the API.

    Attributes:
        id (int): The unique identifier for the topic.
        topic (str): The title of the topic.
        created_at (datetime): The date and time when the topic was created.
        updated_at (datetime): The date and time when the topic was last updated.


    Examples:
        >>> topic = TopicBase(id=1, topic="topic"
                            created_at=datetime.now(), updated_at=datetime.now())
    """

    id: int
    topic: str
    created_at: datetime
    updated_at: datetime

class TopicCreateSchema(BaseModel):
    """
    Pydantic model for validating topic creation data.

    Attributes:
        topic (str): The title of the topic. Must be between 1 and 255 characters.
    """

    topic: str = Field(pattern=r"^[a-zA-Z0-9_ ]*$")

class TopicResponseSchema(TopicBase):
    """
    Pydantic model for serializing topic data returned by the API.

    Attributes:
        id (int): The unique identifier for the topic.
        topic (str): The title of the topic.
        created_at (datetime): The date and time when the topic was created.
        updated_at (datetime): The date and time when the topic was last updated.


    Examples:
        >>> topic = TopicResponseSchema(id=1, topic="topic"
                            created_at=datetime.now(), updated_at=datetime.now())
    """

    id: int
    topic: str = Field(..., alias='name')
    created_at: datetime
    updated_at: datetime
