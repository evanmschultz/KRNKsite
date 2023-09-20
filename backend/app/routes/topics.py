from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models.topic import Topic
from app.schemas.topic_schema import TopicCreateSchema, TopicResponseSchema
from config.database import get_db
from typing import List

router = APIRouter()


@router.post("/topic/create/", response_model=TopicResponseSchema)
def create_topic(

    topic_data: TopicCreateSchema, db: Session = Depends(get_db)

) -> dict:

    """
    Create a new topic. -Create

    Args:
        topic_data (TopicCreateSchema): The topic details encapsulated in a Pydantic model.
        db (Session, optional): The database session. Defaults to `get_db()` dependency.

    Returns:
        dict: A dictionary containing the created topic object.
    """

    topic = Topic(**topic_data.dict())
    db.add(topic)
    db.commit()
    db.refresh(topic)
    return topic

@router.get("/topics/", response_model=List[TopicResponseSchema])
def get_all_topics(db: Session = Depends(get_db)) -> List[TopicResponseSchema]:
            
            """
            Get all topics. -Read
    
            Args:
                db (Session, optional): The database session. Defaults to `get_db()` dependency.
    
            Returns:
                dict: A dictionary containing the retrieved topic objects.
            """
    
            topics = db.query(Topic).all()
            return topics

@router.get("/topic/{topic_id}/", response_model=TopicResponseSchema)
def get_topic(topic_id: int, db: Session = Depends(get_db)) -> dict:

        """
        Get a topic by ID. -Read

        Args:
            topic_id (int): The ID of the topic to retrieve.
            db (Session, optional): The database session. Defaults to `get_db()` dependency.

        Raises:
            HTTPException: If the topic does not exist.

        Returns:
            dict: A dictionary containing the retrieved topic object.
        """

        topic = db.query(Topic).filter(Topic.id == topic_id).first()
        if not topic:
            raise HTTPException(status_code=404, detail="Topic not found")
        return topic





@router.patch("/topic/update/{topic_id}/", response_model=TopicResponseSchema)
def update_topic(
        
        topic_id: int, topic_data: TopicCreateSchema, db: Session = Depends(get_db)
    
    ) -> dict:
    
        """
        Update a topic by ID. -Update
    
        Args:
            topic_id (int): The ID of the topic to update.
            topic_data (TopicCreateSchema): The topic details encapsulated in a Pydantic model.
            db (Session, optional): The database session. Defaults to `get_db()` dependency.
    
        Raises:
            HTTPException: If the topic does not exist.
    
        Returns:
            dict: A dictionary containing the updated topic object.
        """
    
        topic = db.query(Topic).filter(Topic.id == topic_id).first()
        if not topic:
            raise HTTPException(status_code=404, detail="Topic not found")
        topic.name = topic_data.topic
        db.commit()
        db.refresh(topic)
        return topic


@router.delete("/topic/delete/{topic_id}/", response_model=TopicResponseSchema)
def delete_topic(topic_id: int, db: Session = Depends(get_db)) -> dict:
        
            """
            Delete a topic by ID. -Delete
    
            Args:
                topic_id (int): The ID of the topic to delete.
                db (Session, optional): The database session. Defaults to `get_db()` dependency.
    
            Raises:
                HTTPException: If the topic does not exist.
    
            Returns:
                dict: A dictionary containing the deleted topic object.
            """
    
            topic = db.query(Topic).filter(Topic.id == topic_id).first()
            if not topic:
                raise HTTPException(status_code=404, detail="Topic not found")
            db.delete(topic)
            db.commit()
            return topic