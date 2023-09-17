from pydantic import BaseModel
from datetime import datetime

class PaperBase(BaseModel):
    pdf_path: str

class PaperRead(PaperBase):
    id: int
    created_at: datetime
    updated_at: datetime

class PaperCreate(PaperBase):
    pass

class PaperUpdate(PaperBase):
    pass

class PaperDelete(PaperRead):
    pass