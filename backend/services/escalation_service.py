from sqlalchemy.orm import Session
from backend.models.all_models import Ticket, TicketStatus, Priority, TicketHistory
from backend.services.notification_service import notification_service
from datetime import datetime
from loguru import logger

class EscalationService:
    @staticmethod
    def escalate_stale_tickets(db: Session):
        """
        Production-grade escalation logic for tickets hitting SLA soft limits.
        """
        now = datetime.utcnow()
        # Find tickets that are In Progress but near their SLA deadline
        critical_threshold = now + timedelta(hours=2)
        
        candidates = db.query(Ticket).filter(
            Ticket.status == TicketStatus.IN_PROGRESS,
            Ticket.sla_deadline <= critical_threshold,
            Ticket.priority != Priority.CRITICAL
        ).all()
        
        escalated_count = 0
        for ticket in candidates:
            logger.info(f"Escalating ticket {ticket.ticket_id} to CRITICAL due to SLA proximity.")
            
            old_priority = ticket.priority
            ticket.priority = Priority.CRITICAL
            ticket.status = TicketStatus.ESCALATED
            
            # Audit the escalation
            history = TicketHistory(
                ticket_id=ticket.id,
                old_status=TicketStatus.IN_PROGRESS,
                new_status=TicketStatus.ESCALATED,
                change_reason=f"Auto-escalated from {old_priority} due to SLA soft-limit (2h remaining).",
                changed_by="SLA_MONITOR_SERVICE"
            )
            db.add(history)
            
            # Notify the department officer
            if ticket.department:
                msg = f"URGENT: Ticket {ticket.ticket_id} has been escalated to CRITICAL priority."
                notification_service.send_whatsapp(db, ticket.id, msg, ticket.department.contact_phone or "+910000000000")
                
            escalated_count += 1
            
        db.commit()
        return escalated_count

    @staticmethod
    def handle_manual_escalation(db: Session, ticket_id: int, reason: str, officer_id: str):
        """
        Allows an administrator to manually push a ticket to the next urgency level.
        """
        ticket = db.query(Ticket).filter(Ticket.id == ticket_id).first()
        if not ticket:
            return None
            
        ticket.status = TicketStatus.ESCALATED
        history = TicketHistory(
            ticket_id=ticket.id,
            new_status=TicketStatus.ESCALATED,
            change_reason=f"Manual escalation by {officer_id}: {reason}",
            changed_by=officer_id
        )
        db.add(history)
        db.commit()
        return ticket

escalation_service = EscalationService()
from datetime import timedelta # Fix for missing import in snippet
