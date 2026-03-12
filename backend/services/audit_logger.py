from sqlalchemy.orm import Session
from backend.models.all_models import Ticket, TicketHistory
from datetime import datetime
from loguru import logger

class DetailedAuditService:
    """
    Provides an immutable-like audit trail of every interaction within the PALLAVI system.
    Ensures accountability and transparency for government digital services.
    """
    
    @staticmethod
    def log_ticket_mutation(
        db: Session, 
        ticket_id: int, 
        old_val: str, 
        new_val: str, 
        field: str, 
        actor: str = "SYSTEM"
    ):
        """
        Logs a specific field mutation for a ticket.
        """
        reason = f"Mutation of '{field}' from '{old_val}' to '{new_val}'"
        log = TicketHistory(
            ticket_id=ticket_id,
            new_status=None,
            change_reason=reason,
            changed_by=actor,
            timestamp=datetime.utcnow()
        )
        db.add(log)
        db.commit()
        logger.info(f"AUDIT_LOG | Ticket {ticket_id} | {reason} | Actor: {actor}")

    @staticmethod
    def generate_audit_summary(db: Session, ticket_id: int) -> List[Dict[str, Any]]:
        """
        Retrieves and formats the full audit trail for a ticket.
        """
        history = db.query(TicketHistory).filter(TicketHistory.ticket_id == ticket_id).order_by(TicketHistory.timestamp.asc()).all()
        return [
            {
                "time": h.timestamp.isoformat(),
                "actor": h.changed_by,
                "change": h.change_reason,
                "status": h.new_status.value if h.new_status else "No Change"
            } for h in history
        ]

audit_logger = DetailedAuditService()
