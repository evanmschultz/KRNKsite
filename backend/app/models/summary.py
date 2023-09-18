from sqlalchemy import Column, Integer, DateTime, ForeignKey, Text
from datetime import datetime
from config.database import Base


class Summary(Base):
    __tablename__ = "summaries"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    paper_id = Column(Integer, ForeignKey("papers.id"), index=True)
    short_summary = Column(Text)
    long_summary = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)