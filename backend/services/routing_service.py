from sqlalchemy.orm import Session
from backend.models.all_models import Department, Ticket
from typing import Optional

class RoutingService:
    @staticmethod
    def get_department_by_category(db: Session, category: str) -> Optional[Department]:
        """
        Maps a complaint category to a government department.
        """
        mapping = {
            "Water": "Water Supply Department",
            "Electricity": "Electricity Board",
            "Roads": "Municipal Roads Department",
            "Sanitation": "City Sanitation Department",
            "Public Safety": "Police Department"
        }
        
        dept_name = mapping.get(category, "General Administration")
        return db.query(Department).filter(Department.name == dept_name).first()

    @staticmethod
    def auto_route_ticket(db: Session, ticket_id: int):
        """
        Orchestrates the automatic routing of a newly created ticket.
        """
        ticket = db.query(Ticket).filter(Ticket.id == ticket_id).first()
        if not ticket:
            return False
            
        dept = RoutingService.get_department_by_category(db, ticket.category)
        if dept:
            ticket.department_id = dept.id
            db.add(ticket)
            db.commit()
            return True
        return False

routing_service = RoutingService()
