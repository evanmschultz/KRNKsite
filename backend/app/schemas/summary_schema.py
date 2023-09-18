from datetime import datetime
import re
from pydantic import BaseModel, validator, EmailStr, ValidationError, Field


class SummaryBase(BaseModel):
    short_content: str
    long_content: str


class SummaryCreateSchema(SummaryBase):
    pass

class SummaryResponseSchema(SummaryBase):
    id: int
    paper_id: int
    created_at: datetime
    updated_at: datetime