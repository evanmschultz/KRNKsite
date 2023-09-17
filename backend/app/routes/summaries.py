from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models.summary import Summary
from app.schemas.summary_schema import SummaryCreateSchema, SummaryResponseSchema
from config.database import get_db


router = APIRouter()

#--------------------------------------------------------
# GET ROUTES
#--------------------------------------------------------

@router.get("/summary/get/{summary_id}/", response_model=SummaryResponseSchema)
def get_summary(summary_id: int, db: Session = Depends(get_db)) -> dict:
            
            """
            Get a summary by ID. -Read
        
            Args:
                summary_id (int): The ID of the summary to retrieve.
                db (Session, optional): The database session. Defaults to `get_db()` dependency.
        
            Raises:
                HTTPException: If the summary does not exist.
        
            Returns:
                dict: A dictionary containing the retrieved summary object.
            """
        
            summary = db.query(Summary).filter(Summary.id == summary_id).first()
            if not summary:
                raise HTTPException(status_code=404, detail="Summary not found")
            return summary


@router.get("/summary/get/all/", response_model=SummaryResponseSchema)
def get_all_summaries(db: Session = Depends(get_db)) -> dict:
                    
            """
            Get all summaries. -Read
        
            Args:
                db (Session, optional): The database session. Defaults to `get_db()` dependency.
        
            Returns:
                dict: A dictionary containing the retrieved summary objects.
            """
        
            summaries = db.query(Summary).all()
            return summaries

#--------------------------------------------------------
# POST ROUTES
#--------------------------------------------------------

@router.post("/summary/create/", response_model=SummaryCreateSchema)
def create_summary(
    summary_data: SummaryCreateSchema, db: Session = Depends(get_db)
) -> dict:
    """
    Create a new summary. -Create

    Args:
        summary_data (SummaryCreateSchema): The summary details encapsulated in a Pydantic model.
        db (Session, optional): The database session. Defaults to `get_db()` dependency.

    Returns:
        dict: A dictionary containing the created summary object.
    """

    summary = Summary(**summary_data.dict())
    db.add(summary)
    db.commit()
    db.refresh(summary)
    return summary

#--------------------------------------------------------
# PUT ROUTES
#--------------------------------------------------------

@router.put("/summary/update/{summary_id}/", response_model=SummaryCreateSchema)
def update_summary(
    summary_id: int, summary_data: SummaryCreateSchema, db: Session = Depends(get_db)
) -> dict:
    """
    Update a summary by ID. -Update

    Args:
        summary_id (int): The ID of the summary to update.
        summary_data (SummaryCreateSchema): The summary details encapsulated in a Pydantic model.
        db (Session, optional): The database session. Defaults to `get_db()` dependency.

    Raises:
        HTTPException: If the summary does not exist.

    Returns:
        dict: A dictionary containing the updated summary object.
    """

    summary = db.query(Summary).filter(Summary.id == summary_id).first()
    if not summary:
        raise HTTPException(status_code=404, detail="Summary not found")
    summary_data = summary_data.dict(exclude_unset=True)
    for key, value in summary_data.items():
        setattr(summary, key, value)
    db.add(summary)
    db.commit()
    db.refresh(summary)
    return summary

#--------------------------------------------------------
# DELETE ROUTES
#--------------------------------------------------------

@router.delete("/summary/delete/{summary_id}/", response_model=SummaryCreateSchema)
def delete_summary(summary_id: int, db: Session = Depends(get_db)
) -> dict:
    """
    Delete a summary by ID. -Delete
    
    Args:
        summary_id (int): The ID of the summary to delete.
        db (Session, optional): The database session. Defaults to `get_db()` dependency.
        
        Raises:
            HTTPException: If the summary does not exist.
            
            Returns:
                
                dict: A dictionary containing the deleted summary object.
                """
    
    summary = db.query(Summary).filter(Summary.id == summary_id).first()
    if not summary:
        raise HTTPException(status_code=404, detail="Summary not found")
    db.delete(summary)
    db.commit()
    return summary
