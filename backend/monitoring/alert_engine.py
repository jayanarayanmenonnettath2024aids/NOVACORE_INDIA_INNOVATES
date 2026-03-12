from typing import Dict, Any, List
from sqlalchemy.orm import Session
from backend.models.all_models import Ticket, TicketStatus, Priority
from backend.services.notification_service import notification_service
from loguru import logger
from datetime import datetime

class AlertEngine:
    """
    Simulates a real-time alerting engine that monitors system state.
    Triggers critical notifications for administrators based on specific thresholds.
    """
    def __init__(self):
        self.alert_history: List[Dict[str, Any]] = []
        logger.info("AlertEngine online: Monitoring city governance thresholds.")

    def evaluate_critical_conditions(self, db: Session):
        """
        Scans for conditions that require immediate administrative attention.
        """
        logger.info("AlertEngine: Evaluating critical conditions...")
        
        # 1. Check for surging critical tickets
        critical_count = db.query(Ticket).filter(
            Ticket.priority == Priority.CRITICAL,
            Ticket.status != TicketStatus.RESOLVED
        ).count()
        
        if critical_count > 10:
            self._trigger_alert(
                "CRITICAL_TICKET_SURGE",
                f"Alert! There are {critical_count} unresolved critical tickets in the system!",
                "EMERGENCY"
            )

        # 2. Check for SLA mass breaches
        now = datetime.utcnow()
        breaches = db.query(Ticket).filter(
            Ticket.status != TicketStatus.RESOLVED,
            Ticket.sla_deadline < now
        ).count()
        
        if breaches > 50:
             self._trigger_alert(
                "SLA_MASS_BREACH",
                f"Warning: {breaches} tickets have breached SLA! Immediate department follow-up required.",
                "HIGH"
            )

    def _trigger_alert(self, code: str, message: str, severity: str):
        """
        Record and log the alert. In production, this would hit PagerDuty/Slack.
        """
        alert = {
            "timestamp": datetime.utcnow().isoformat(),
            "code": code,
            "message": message,
            "severity": severity
        }
        self.alert_history.append(alert)
        logger.critical(f"ALERT_SYSTEM | {severity} | {code}: {message}")
        
        # Simulated SMS to head administrator
        # notification_service.send_sms(...)

    def get_active_alerts(self) -> List[Dict[str, Any]]:
        return self.alert_history[-20:]

alert_engine = AlertEngine()
