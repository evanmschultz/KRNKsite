from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models.paper import Paper
from typing import List

from app.schemas.paper_schema import PaperCreate, PaperRead, PaperUpdate, PaperDelete
from config.database import get_db

router = APIRouter()


@router.post("/paper/create/", response_model=PaperCreate)
def create_paper(

    paper_data: PaperCreate, db: Session = Depends(get_db)

) -> dict:

    """
    Create a new paper. -Create

    Args:
        paper_data (PaperCreateSchema): The paper details encapsulated in a Pydantic model.
        db (Session, optional): The database session. Defaults to `get_db()` dependency.

    Returns:
        dict: A dictionary containing the created paper object.
    """

    paper = Paper(**paper_data.dict())
    db.add(paper)
    db.commit()
    db.refresh(paper)
    return paper


@router.get("/paper/get/{paper_id}/", response_model=PaperRead)
def get_paper(paper_id: int, db: Session = Depends(get_db)) -> dict:
    
        """
        Get a paper by ID. -Read
    
        Args:
            paper_id (int): The ID of the paper to retrieve.
            db (Session, optional): The database session. Defaults to `get_db()` dependency.
    
        Raises:
            HTTPException: If the paper does not exist.
    
        Returns:
            dict: A dictionary containing the retrieved paper object.
        """
    
        paper = db.query(Paper).filter(Paper.id == paper_id).first()
        if not paper:
            raise HTTPException(status_code=404, detail="Paper not found")
        return paper

@router.get("/papers/", response_model=List[PaperRead])
def get_all_papers(db: Session = Depends(get_db)) -> List[dict]:
    """
    Get all papers. -Read
    
    Args:
        db (Session, optional): The database session. Defaults to `get_db()` dependency.
        
        Returns:
            dict: A dictionary containing the retrieved paper objects."""
    papers = db.query(Paper).all()
    return papers


@router.put("/paper/update/{paper_id}/", response_model=PaperUpdate)
def update_paper(
    paper_id: int, paper_data: PaperUpdate, db: Session = Depends(get_db)
) -> dict:
    
        """
        Update a paper by ID. -Update
    
        Args:
            paper_id (int): The ID of the paper to update.
            paper_data (PaperCreateSchema): The updated paper details encapsulated in a Pydantic model.
            db (Session, optional): The database session. Defaults to `get_db()` dependency.
    
        Returns:
            dict: A dictionary containing the updated paper object.
        """
    
        paper = db.query(Paper).filter(Paper.id == paper_id).first()
        if not paper:
            raise HTTPException(status_code=404, detail="Paper not found")
    
        for key, value in paper_data.dict().items():
            setattr(paper, key, value)
    
        db.commit()
        db.refresh(paper)
        return paper


@router.delete("/paper/delete/{paper_id}/", response_model=PaperDelete)
def delete_paper(paper_id: int, db: Session = Depends(get_db)) -> dict:
        
            """
            Delete a paper by ID. -Delete
        
            Args:
                paper_id (int): The ID of the paper to delete.
                db (Session, optional): The database session. Defaults to `get_db()` dependency.
        
            Returns:
                dict: A dictionary containing a "detail" key with a message indicating the paper was deleted.
        
            Raises:
                HTTPException: 404 status if paper is not found.
            """
        
            paper = db.query(Paper).filter(Paper.id == paper_id).first()
            if not paper:
                raise HTTPException(status_code=404, detail="Paper not found")
        
            db.delete(paper)
            db.commit()
            return {"detail": "Paper deleted"}

