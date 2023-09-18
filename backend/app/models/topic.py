from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from config.database import Base
from app.models.associations import user_topics_association





class Topic(Base):
    __tablename__ = "topics"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(255), index=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationship to User
    users = relationship("User", secondary=user_topics_association, back_populates="topics")
    # Define the relationship to Paper
    papers = relationship("Paper", back_populates="topic")
