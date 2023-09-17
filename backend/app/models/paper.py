from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from config.database import Base


class Paper(Base):
    __tablename__ = "papers"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    pdf_path = Column(String(255), index=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
