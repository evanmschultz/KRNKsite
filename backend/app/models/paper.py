from sqlalchemy import Column, Integer, String, DateTime, Date, ForeignKey, Text
from sqlalchemy.orm import relationship
from datetime import datetime
from config.database import Base


class Paper(Base):
    __tablename__ = "papers"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    pdf_url = Column(String(255), index=True)
    title = Column(String(255), index=True)
    authors = Column(Text)
    topic_id = Column(Integer, ForeignKey("topics.id"), nullable=False)
    summary = Column(Text)
    publication_date = Column(Date)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Define the relationship to Topic
    topic = relationship("Topic", back_populates="papers")
