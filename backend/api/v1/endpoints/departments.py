from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from backend.database.session import get_db
from backend.models.all_models import Department
from backend.schemas import all_schemas as schemas

router = APIRouter()

@router.get("/", response_model=List[schemas.Department])
def read_departments(db: Session = Depends(get_db)):
    """
    Lists all government departments integrated with PALLAVI.
    """
    return db.query(Department).all()

@router.get("/{department_id}", response_model=schemas.Department)
def read_department(department_id: int, db: Session = Depends(get_db)):
    """
    Fetches details and performance for a specific department.
    """
    db_dept = db.query(Department).filter(Department.id == department_id).first()
    if not db_dept:
        raise HTTPException(status_code=404, detail="Department not found")
    return db_dept

@router.get("/{department_id}/tickets")
def get_department_tickets(department_id: int, db: Session = Depends(get_db)):
    """
    Retrieves all tickets assigned to a specific department.
    """
    tickets = db.query(Ticket).filter(Ticket.department_id == department_id).all()
    return tickets
