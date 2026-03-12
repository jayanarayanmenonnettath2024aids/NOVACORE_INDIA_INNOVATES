from sqlalchemy.orm import Session
from backend.models.all_models import Ticket, TicketHistory
from typing import List, Optional
from datetime import datetime

class AuditService:
    @staticmethod
    def log_action(db: Session, ticket_id: int, action: str, performed_by: str = "SYSTEM"):
        """
        Logs a specific administrative or system action.
        """
        history = TicketHistory(
            ticket_id=ticket_id,
            new_status=None, # Not necessarily a status change
            change_reason=action,
            changed_by=performed_by,
            timestamp=datetime.utcnow()
        )
        db.add(history)
        db.commit()

    @staticmethod
    def get_ticket_history(db: Session, ticket_id_str: str) -> List[TicketHistory]:
        """
        Retrieves the full audit trail for a ticket.
        """
        ticket = db.query(Ticket).filter(Ticket.ticket_id == ticket_id_str).first()
        if not ticket:
            return []
        return db.query(TicketHistory).filter(TicketHistory.ticket_id == ticket.id).order_by(TicketHistory.timestamp.desc()).all()

audit_service = AuditService()
