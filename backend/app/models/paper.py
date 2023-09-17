from sqlalchemy import Column, Integer, String, DateTime, Date, ForeignKey, Text
from sqlalchemy.orm import relationship
from datetime import datetime
from app.models.associations import Base


class Paper(Base):
    __tablename__ = "papers"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    pdf_url = Column(String(255), index=True)
    title = Column(String(255), index=True)
    authors = Column(Text)
    topic_id = Column(Integer, ForeignKey("topics.id"), nullable=False)
    publication_date = Column(Date)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Define the relationship to Topic
    topic = relationship("Topic", back_populates="papers")


"""
USE krnksite;

DELIMITER //
-- Update 'topics' table
CREATE PROCEDURE UpdateTopics()
BEGIN
    IF NOT EXISTS (SELECT * FROM information_schema.columns WHERE table_name = 'topics' AND column_name = 'name') THEN
        ALTER TABLE topics ADD COLUMN name VARCHAR(255);
    END IF;
    IF NOT EXISTS (SELECT * FROM information_schema.columns WHERE table_name = 'topics' AND column_name = 'created_at') THEN
        ALTER TABLE topics ADD COLUMN created_at DATETIME DEFAULT CURRENT_TIMESTAMP;
    END IF;
    IF NOT EXISTS (SELECT * FROM information_schema.columns WHERE table_name = 'topics' AND column_name = 'updated_at') THEN
        ALTER TABLE topics ADD COLUMN updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP;
    END IF;
END;
//

-- Update 'summaries' table
CREATE PROCEDURE UpdateSummaries()
BEGIN
    IF NOT EXISTS (SELECT * FROM information_schema.columns WHERE table_name = 'summaries' AND column_name = 'paper_id') THEN
        ALTER TABLE summaries ADD COLUMN paper_id INT;
    END IF;
    IF NOT EXISTS (SELECT * FROM information_schema.columns WHERE table_name = 'summaries' AND column_name = 'short_summary') THEN
        ALTER TABLE summaries ADD COLUMN short_summary TEXT;
    END IF;
    IF NOT EXISTS (SELECT * FROM information_schema.columns WHERE table_name = 'summaries' AND column_name = 'long_summary') THEN
        ALTER TABLE summaries ADD COLUMN long_summary TEXT;
    END IF;
    IF NOT EXISTS (SELECT * FROM information_schema.columns WHERE table_name = 'summaries' AND column_name = 'created_at') THEN
        ALTER TABLE summaries ADD COLUMN created_at DATETIME DEFAULT CURRENT_TIMESTAMP;
    END IF;
    IF NOT EXISTS (SELECT * FROM information_schema.columns WHERE table_name = 'summaries' AND column_name = 'updated_at') THEN
        ALTER TABLE summaries ADD COLUMN updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP;
    END IF;
END;
//

-- Update 'papers' table
CREATE PROCEDURE UpdatePapers()
BEGIN
    IF NOT EXISTS (SELECT * FROM information_schema.columns WHERE table_name = 'papers' AND column_name = 'pdf_url') THEN
        ALTER TABLE papers ADD COLUMN pdf_url VARCHAR(255);
    END IF;
    IF NOT EXISTS (SELECT * FROM information_schema.columns WHERE table_name = 'papers' AND column_name = 'title') THEN
        ALTER TABLE papers ADD COLUMN title VARCHAR(255);
    END IF;
    IF NOT EXISTS (SELECT * FROM information_schema.columns WHERE table_name = 'papers' AND column_name = 'authors') THEN
        ALTER TABLE papers ADD COLUMN authors TEXT;
    END IF;
    IF NOT EXISTS (SELECT * FROM information_schema.columns WHERE table_name = 'papers' AND column_name = 'topic_id') THEN
        ALTER TABLE papers ADD COLUMN topic_id INT NOT NULL;
    END IF;
    IF NOT EXISTS (SELECT * FROM information_schema.columns WHERE table_name = 'papers' AND column_name = 'publication_date') THEN
        ALTER TABLE papers ADD COLUMN publication_date DATE;
    END IF;
    IF NOT EXISTS (SELECT * FROM information_schema.columns WHERE table_name = 'papers' AND column_name = 'created_at') THEN
        ALTER TABLE papers ADD COLUMN created_at DATETIME DEFAULT CURRENT_TIMESTAMP;
    END IF;
    IF NOT EXISTS (SELECT * FROM information_schema.columns WHERE table_name = 'papers' AND column_name = 'updated_at') THEN
        ALTER TABLE papers ADD COLUMN updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP;
    END IF;
END;
//

DELIMITER ;

-- Call the procedures to actually update the tables
CALL UpdateTopics();
CALL UpdateSummaries();
CALL UpdatePapers();

"""
