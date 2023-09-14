# Models for the many-to-many relationships between tables

from sqlalchemy import Column, Integer, ForeignKey, Table
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# For the, "table", many-to-many relationship between Users and Topics
user_topics_association = Table(
    "user_topics",
    Base.metadata,
    Column("user_id", Integer, ForeignKey("users.id")),
    Column("topic_id", Integer, ForeignKey("topics.id")),
)
