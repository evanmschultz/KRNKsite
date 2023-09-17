#associations routes
#--------------------------------------------------------

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models.association import Association

from app.schemas.association_schema import AssociationCreateSchema, AssociationResponseSchema
from config.database import get_db

router = APIRouter()



#--------------------------------------------------------
# GET ROUTES
#--------------------------------------------------------

@router.get("/association/get/{association_id}/", response_model=AssociationResponseSchema)
def get_association(association_id: int, db: Session = Depends(get_db)) -> dict:
        
            """
            Get an association by ID. -Read
        
            Args:
                association_id (int): The ID of the association to retrieve.
                db (Session, optional): The database session. Defaults to `get_db()` dependency.
        
            Raises:
                HTTPException: If the association does not exist.
        
            Returns:
                dict: A dictionary containing the retrieved association object.
            """
        
            association = db.query(Association).filter(Association.id == association_id).first()
            if not association:
                raise HTTPException(status_code=404, detail="Association not found")
            return association


@router.get("/association/get/all/", response_model=AssociationResponseSchema)
def get_all_associations(db: Session = Depends(get_db)) -> dict:
                
        """
        Get all associations. -Read
    
        Args:
            db (Session, optional): The database session. Defaults to `get_db()` dependency.
    
        Returns:
            dict: A dictionary containing the retrieved association objects.
        """
    
        associations = db.query(Association).all()
        return associations 

#--------------------------------------------------------
# POST ROUTES
#--------------------------------------------------------

@router.post("/association/create/", response_model=AssociationResponseSchema)
def create_association(
    
        association_data: AssociationCreateSchema, db: Session = Depends(get_db)
    
    ) -> dict:
    
        """
        Create a new association. -Create
    
        Args:
            association_data (AssociationCreateSchema): The association details encapsulated in a Pydantic model.
            db (Session, optional): The database session. Defaults to `get_db()` dependency.
    
        Returns:
            dict: A dictionary containing the created association object.
        """
    
        association = Association(**association_data.dict())
        db.add(association)
        db.commit()
        db.refresh(association)
        return association

#--------------------------------------------------------
# PUT ROUTES
#--------------------------------------------------------

@router.put("/association/update/{association_id}/", response_model=AssociationResponseSchema)
def update_association(
    association_id: int, association_data: AssociationCreateSchema, db: Session = Depends(get_db)
) -> dict:
    
        """
        Update an association by ID. -Update
    
        Args:
            association_id (int): The ID of the association to update.
            association_data (AssociationCreateSchema): The association details encapsulated in a Pydantic model.
            db (Session, optional): The database session. Defaults to `get_db()` dependency.
    
        Raises:
            HTTPException: If the association does not exist.
    
        Returns:
            dict: A dictionary containing the updated association object.
        """
    
        association = db.query(Association).filter(Association.id == association_id).first()
        if not association:
            raise HTTPException(status_code=404, detail="Association not found")
        for key, value in association_data.dict().items():
            setattr(association, key, value)

        db.commit()
        return association
#--------------------------------------------------------
# DELETE ROUTES
#--------------------------------------------------------

@router.delete("/association/delete/{association_id}/", response_model=AssociationResponseSchema)
def delete_association(association_id: int, db: Session = Depends(get_db)) -> dict:
        
            """
            Delete an association by ID. -Delete
        
            Args:
                association_id (int): The ID of the association to delete.
                db (Session, optional): The database session. Defaults to `get_db()` dependency.
        
            Raises:
                HTTPException: If the association does not exist.
        
            Returns:
                dict: A dictionary containing the deleted association object.
            """
        
            association = db.query(Association).filter(Association.id == association_id).first()
            if not association:
                raise HTTPException(status_code=404, detail="Association not found")
            db.delete(association)
            db.commit()
            return association
