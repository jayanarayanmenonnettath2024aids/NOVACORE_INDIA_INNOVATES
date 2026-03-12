from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from backend.database.session import get_db
from backend.services.citizen_service import citizen_service
from backend.schemas import all_schemas as schemas

router = APIRouter()

@router.get("/", response_model=List[schemas.Citizen])
def read_citizens(db: Session = Depends(get_db), skip: int = 0, limit: int = 100):
    """
    Retrieves a list of registered citizens.
    """
    return db.query(Citizen).offset(skip).limit(limit).all()

@router.get("/{citizen_id}", response_model=schemas.Citizen)
def read_citizen(citizen_id: int, db: Session = Depends(get_db)):
    """
    Fetches details for a single citizen by ID.
    """
    db_citizen = db.query(Citizen).filter(Citizen.id == citizen_id).first()
    if not db_citizen:
        raise HTTPException(status_code=404, detail="Citizen not found")
    return db_citizen

@router.get("/phone/{phone_number}", response_model=schemas.Citizen)
def read_citizen_by_phone(phone_number: str, db: Session = Depends(get_db)):
    """
    Look up a citizen record via their phone number.
    """
    db_citizen = citizen_service.get_citizen_by_phone(db, phone_number)
    if not db_citizen:
        raise HTTPException(status_code=404, detail="No citizen found with this phone number")
    return db_citizen
