from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List
from backend.database.session import get_db
from backend.services.ticket_service import ticket_service
from backend.schemas import all_schemas as schemas

router = APIRouter()

@router.get("/", response_model=List[schemas.Ticket])
def read_tickets(db: Session = Depends(get_db), skip: int = 0, limit: int = 100):
    return ticket_service.list_tickets(db, skip=skip, limit=limit)

@router.get("/{ticket_id}", response_model=schemas.Ticket)
def read_ticket(ticket_id: str, db: Session = Depends(get_db)):
    db_ticket = ticket_service.get_ticket(db, ticket_id_str=ticket_id)
    if not db_ticket:
        raise HTTPException(status_code=404, detail="Ticket not found")
    return db_ticket

@router.patch("/{ticket_id}", response_model=schemas.Ticket)
def update_ticket(
    ticket_id: int, 
    ticket_in: schemas.TicketUpdate, 
    db: Session = Depends(get_db)
):
    db_ticket = ticket_service.update_status(
        db, 
        ticket_id=ticket_id, 
        new_status=ticket_in.status, 
        reason="Admin Update"
    )
    if not db_ticket:
        raise HTTPException(status_code=404, detail="Ticket not found")
    return db_ticket
