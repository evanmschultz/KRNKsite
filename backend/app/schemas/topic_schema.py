from datetime import datetime
import re
from pydantic import BaseModel 


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
