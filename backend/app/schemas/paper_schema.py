from datetime import datetime
import re
from pydantic import BaseModel 



class PaperBase(BaseModel):
    """
    Pydantic model for serializing user data returned by the API.

    Attributes:
        id (int): The unique identifier for the paper.
        paper_title (str): The title of the paper.
        paper_source (str): The source of the paper.
        pdf_path (str): The path to the paper's PDF file.
        created_at (datetime): The date and time when the paper was created.
        updated_at (datetime): The date and time when the paper was last updated.

        
    Examples:
        >>> paper = PaperBase(id=1, pdf_path="path/to/pdf"
        ...                    created_at=datetime.now(), updated_at=datetime.now())
    """

    id: int
    pdf_path: str
    # paper_title: str
    # paper_source: str  Could these be useful?
    created_at: datetime
    updated_at: datetime

    # @validator('paper_title') - [ ] Do we need these?
    # def validate_paper_title_length(cls, value):
    #     if len(value) < 5:
    #         raise ValueError("Paper title must be at least 5 characters long")
    #     return value
    
    # @validator('paper_source')
    # def validate_paper_source_length(cls, value):
    #     if len(value) < 5:
    #         raise ValueError("Paper source must be at least 5 characters long")
    #     return value
    
    