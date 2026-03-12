from sqlalchemy.orm import Session
from sqlalchemy import func
from backend.models.all_models import Ticket, TicketStatus, Priority, CallLog
from datetime import datetime, timedelta

class AnalyticsService:
    @staticmethod
    def get_dashboard_data(db: Session):
        now = datetime.utcnow()
        last_24h = now - timedelta(hours=24)
        
        total_tickets = db.query(Ticket).count()
        active_tickets = db.query(Ticket).filter(Ticket.status != TicketStatus.RESOLVED, Ticket.status != TicketStatus.CLOSED).count()
        resolved_tickets = db.query(Ticket).filter(Ticket.status == TicketStatus.RESOLVED).count()
        
        # Priority Stats
        critical_count = db.query(Ticket).filter(Ticket.priority == Priority.CRITICAL).count()
        high_count = db.query(Ticket).filter(Ticket.priority == Priority.HIGH).count()
        
        # Category Distribution
        cat_dist = db.query(Ticket.category, func.count(Ticket.id)).group_by(Ticket.category).all()
        cat_map = {cat: count for cat, count in cat_dist}
        
        # SLA Violations
        sla_violations = db.query(Ticket).filter(
            Ticket.status != TicketStatus.RESOLVED,
            Ticket.sla_deadline < now
        ).count()
        
        # Call Volume (Today)
        call_volume = db.query(CallLog).filter(CallLog.timestamp >= last_24h).count()
        
        return {
            "total_calls_24h": call_volume,
            "active_tickets": active_tickets,
            "resolved_tickets": resolved_tickets,
            "critical_alerts": critical_count,
            "sla_violations": sla_violations,
            "category_distribution": cat_map,
            "overall_health": 100 - (sla_violations / (total_tickets + 1) * 100)
        }

    @staticmethod
    def get_department_performance(db: Session):
        # Detailed performance metrics per department
        perf = db.query(
            Ticket.department_id,
            func.avg(
                func.extract('epoch', Ticket.resolved_at - Ticket.created_at) / 3600
            ).label('avg_res_hours')
        ).filter(Ticket.resolved_at.isnot(None)).group_by(Ticket.department_id).all()
        
        return {str(dept_id): hours for dept_id, hours in perf}

analytics_service = AnalyticsService()
