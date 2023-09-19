from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models.associations import user_topics_association
from app.models.user import User
from app.models.topic import Topic
from config.database import get_db

router = APIRouter()

@router.post("/add-interest/{user_id}/{topic_id}")
def add_interest(user_id: int, topic_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    topic = db.query(Topic).filter(Topic.id == topic_id).first()
    
    if not user or not topic:
        raise HTTPException(status_code=404, detail="User or topic not found")
    
    user.topics.append(topic)
    db.commit()
    
    return {"message": "Interest added successfully"}

@router.delete("/remove-interest/{user_id}/{topic_id}")
def remove_interest(user_id: int, topic_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    topic = db.query(Topic).filter(Topic.id == topic_id).first()
    
    if not user or not topic:
        raise HTTPException(status_code=404, detail="User or topic not found")
    
    user.topics.remove(topic)
    db.commit()
    
    return {"message": "Interest removed successfully"}

@router.get("/user-interests/{user_id}")
def get_user_interests(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    interests = user.topics
    return [{"id": interest.id, "name": interest.name} for interest in interests]

@router.get("/interest-users/{topic_id}")
def get_interest_users(topic_id: int, db: Session = Depends(get_db)):
    topic = db.query(Topic).filter(Topic.id == topic_id).first()
    
    if not topic:
        raise HTTPException(status_code=404, detail="Topic not found")
    
    users = topic.users
    return [{"id": user.id, "name": f"{user.first_name} {user.last_name}"} for user in users]
