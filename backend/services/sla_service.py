from sqlalchemy.orm import Session
from datetime import datetime, timedelta
from backend.models.all_models import Ticket, TicketStatus, Priority
from loguru import logger

class SLAService:
    @staticmethod
    def check_sla_compliance(db: Session):
        """
        Monitors all active tickets for SLA breaches.
        """
        now = datetime.utcnow()
        breached_tickets = db.query(Ticket).filter(
            Ticket.status != TicketStatus.RESOLVED,
            Ticket.status != TicketStatus.CLOSED,
            Ticket.sla_deadline < now
        ).all()
        
        for ticket in breached_tickets:
            if ticket.status != TicketStatus.ESCALATED:
                logger.warning(f"SLA BREACH: Ticket {ticket.ticket_id} has exceeded its deadline!")
                ticket.status = TicketStatus.ESCALATED
                # Log escalation history logic could go here
                
        db.commit()
        return len(breached_tickets)

    @staticmethod
    def get_sla_metrics(db: Session):
        """
        Calculates complex SLA performance metrics.
        """
        tickets = db.query(Ticket).all()
        total = len(tickets)
        if total == 0:
            return {"compliance_rate": 100}
            
        on_time = 0
        for t in tickets:
            if t.resolved_at:
                if t.resolved_at <= t.sla_deadline:
                    on_time += 1
            else:
                if datetime.utcnow() <= t.sla_deadline:
                    on_time += 1
                    
        return {
            "compliance_rate": round((on_time / total) * 100, 2),
            "total_tickets": total,
            "on_time": on_time,
            "delayed": total - on_time
        }

sla_service = SLAService()
