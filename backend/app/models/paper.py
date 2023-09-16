from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from app.models.associations import Base


class Paper(Base):
    __tablename__ = "papers"
#This is the paper model. It contains the paper's ID, path to the PDF file, and the date and time when the paper was created and last updated.
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    pdf_path = Column(String(255), index=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
