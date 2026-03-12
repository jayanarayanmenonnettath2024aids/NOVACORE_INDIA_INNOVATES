from sqlalchemy.orm import Session
from backend.models.all_models import Ticket, TicketHistory, Department
from backend.services.departments.water_service import water_dept_service
from backend.services.departments.electricity_service import electricity_dept_service
from backend.services.departments.roads_service import roads_dept_service
from backend.services.departments.sanitation_service import sanitation_dept_service
from backend.services.departments.safety_service import public_safety_service
from backend.services.departments.health_service import health_dept_service
from loguru import logger

class DepartmentalOrchestrator:
    """
    Central hub for routing tickets to specialized departmental handlers.
    Ensures that domain-specific logic is executed post-assignment.
    """
    
    @staticmethod
    def process_assignment(db: Session, ticket_id: int):
        """
        Coordinates the specialized departmental response for an assigned ticket.
        """
        ticket = db.query(Ticket).filter(Ticket.id == ticket_id).first()
        if not ticket or not ticket.department:
            return

        dept_name = ticket.department.name
        logger.info(f"Orchestrator: Routing {ticket.ticket_id} to {dept_name} logic.")

        # Mapping names to services
        if "Water" in dept_name:
            water_dept_service.process_water_grievance(db, ticket)
        elif "Electricity" in dept_name or "Power" in dept_name:
            electricity_dept_service.handle_grid_incident(db, ticket)
        elif "Roads" in dept_name:
            roads_dept_service.dispatch_repair_crew(db, ticket)
        elif "Sanitation" in dept_name:
            sanitation_dept_service.schedule_cleanup(db, ticket)
        elif "Police" in dept_name:
            public_safety_service.initiate_emergency_response(db, ticket)
        elif "Health" in dept_name:
            health_dept_service.trace_outbreak(db, ticket)
        else:
            logger.debug(f"Orchestrator: No specialized logic for {dept_name}. Skipping.")

dept_orchestrator = DepartmentalOrchestrator()
