from sqlalchemy.orm import Session
from backend.models.all_models import Ticket, TicketStatus, Department
from datetime import datetime, timedelta
import json
import csv
import io
from loguru import logger

class ReportingService:
    """
    Simulates a production-grade reporting engine for government audits.
    Generates CSV, JSON, and Summary reports for administrative review.
    """
    
    @staticmethod
    def generate_daily_grievance_report(db: Session) -> str:
        """
        Generates a comprehensive summary of all grievances filed in the last 24 hours.
        """
        logger.info("Generating daily grievance report...")
        yesterday = datetime.utcnow() - timedelta(days=1)
        tickets = db.query(Ticket).filter(Ticket.created_at >= yesterday).all()
        
        report_lines = [
            "PALLAVI AI - DAILY GRIEVANCE SUMMARY",
            f"Generated At: {datetime.utcnow().isoformat()}",
            "-------------------------------------------",
            f"Total tickets: {len(tickets)}",
            ""
        ]
        
        # Categorize for the report
        categories = {}
        for t in tickets:
            categories[t.category] = categories.get(t.category, 0) + 1
            
        report_lines.append("By Category:")
        for cat, count in categories.items():
            report_lines.append(f" - {cat}: {count}")
            
        report_lines.append("\nHigh Priority Alerts:")
        for t in tickets:
            if t.priority.value == "critical" or t.priority.value == "high":
                report_lines.append(f" [!] {t.ticket_id}: {t.category} - {t.complaint_text[:50]}...")
                
        return "\n".join(report_lines)

    @staticmethod
    def export_tickets_to_csv(db: Session, department_id: int = None) -> str:
        """
        Exports ticket data to a CSV format string.
        """
        query = db.query(Ticket)
        if department_id:
            query = query.filter(Ticket.department_id == department_id)
            
        tickets = query.all()
        output = io.StringIO()
        writer = csv.writer(output)
        
        writer.writerow(["TicketID", "Citizen", "Category", "Status", "Priority", "Created", "SLA"])
        for t in tickets:
            writer.writerow([
                t.ticket_id, 
                t.citizen.full_name if t.citizen else "N/A",
                t.category,
                t.status.value,
                t.priority.value,
                t.created_at.isoformat(),
                t.sla_deadline.isoformat()
            ])
            
        logger.info(f"Exported {len(tickets)} tickets to CSV.")
        return output.getvalue()

reporting_service = ReportingService()
