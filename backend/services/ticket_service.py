from sqlalchemy.orm import Session
from backend.models.all_models import Ticket, TicketStatus, TicketHistory, Priority
from backend.schemas.all_schemas import TicketCreate, TicketUpdate
from datetime import datetime, timedelta
import random
import string

class TicketService:
    @staticmethod
    def generate_ticket_id() -> str:
        chars = string.ascii_uppercase + string.digits
        return ''.join(random.choice(chars) for _ in range(8))

    @staticmethod
    def get_ticket(db: Session, ticket_id_str: str):
        return db.query(Ticket).filter(Ticket.ticket_id == ticket_id_str).first()

    @staticmethod
    def list_tickets(db: Session, skip: int = 0, limit: int = 100):
        return db.query(Ticket).offset(skip).limit(limit).all()

    @staticmethod
    def create_ticket(db: Session, ticket_in: TicketCreate):
        new_id = TicketService.generate_ticket_id()
        
        # Calculate SLA based on priority
        sla_hours = 24
        if ticket_in.priority == Priority.HIGH:
            sla_hours = 4
        elif ticket_in.priority == Priority.LOW:
            sla_hours = 72
            
        db_ticket = Ticket(
            ticket_id=new_id,
            sla_deadline=datetime.utcnow() + timedelta(hours=sla_hours),
            **ticket_in.dict()
        )
        db.add(db_ticket)
        db.commit()
        db.refresh(db_ticket)
        
        # Initial History
        history = TicketHistory(
            ticket_id=db_ticket.id,
            new_status=TicketStatus.RECEIVED,
            change_reason="Ticket Created via AI Call"
        )
        db.add(history)
        db.commit()
        
        return db_ticket

    @staticmethod
    def update_status(db: Session, ticket_id: int, new_status: TicketStatus, reason: str = None):
        db_ticket = db.query(Ticket).filter(Ticket.id == ticket_id).first()
        if not db_ticket:
            return None
            
        old_status = db_ticket.status
        db_ticket.status = new_status
        db_ticket.updated_at = datetime.utcnow()
        
        if new_status == TicketStatus.RESOLVED:
            db_ticket.resolved_at = datetime.utcnow()
            
        # Log History
        history = TicketHistory(
            ticket_id=db_ticket.id,
            old_status=old_status,
            new_status=new_status,
            change_reason=reason
        )
        db.add(history)
        db.commit()
        db.refresh(db_ticket)
        return db_ticket

ticket_service = TicketService()
