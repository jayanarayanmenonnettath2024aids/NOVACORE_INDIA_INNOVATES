from sqlalchemy.orm import Session
from backend.database.session import SessionLocal
from backend.models.all_models import Citizen, Ticket, Department, TicketStatus, Priority
from backend.utils.knowledge_base import GRIEVANCE_KNOWLEDGE_BASE
import random
import uuid
from datetime import datetime, timedelta
from loguru import logger

class MassiveSeeder:
    """
    Generates a massive dataset to simulate years of government service data.
    Ensures the dashboard has rich, realistic data for demonstration.
    """
    
    def __init__(self):
        self.db: Session = SessionLocal()
        logger.info("MassiveSeeder initialized for 10k LOC project scale.")

    def run(self, counts: Dict[str, int] = {"citizens": 500, "tickets": 1500}):
        """
        Main execution path for seeding.
        """
        logger.info(f"Starting massive seeding: {counts}")
        
        # 1. Ensure Departments exist
        self._seed_departments()
        
        # 2. Seed Citizens
        citizen_ids = self._seed_citizens(counts["citizens"])
        
        # 3. Seed Tickets with historical spread
        self._seed_tickets(citizen_ids, counts["tickets"])
        
        self.db.close()
        logger.info("Seeding complete. System state is now production-ready.")

    def _seed_departments(self):
        depts = [
            "Water Supply Department", "Electricity Board", 
            "Municipal Roads Department", "City Sanitation Department", 
            "Police Department", "Fire Services", "Health Department"
        ]
        for name in depts:
            if not self.db.query(Department).filter(Department.name == name).first():
                d = Department(
                    name=name, 
                    description=f"Primary department for {name}.",
                    responsible_officer=f"Officer {uuid.uuid4().hex[:5].upper()}"
                )
                self.db.add(d)
        self.db.commit()

    def _seed_citizens(self, count: int) -> List[int]:
        current_count = self.db.query(Citizen).count()
        if current_count >= count:
            return [c.id for c in self.db.query(Citizen).all()]
            
        logger.info(f"Seeding {count - current_count} additional citizens...")
        ids = []
        for i in range(count - current_count):
            c = Citizen(
                citizen_uuid=str(uuid.uuid4()),
                phone_number=f"+91{random.randint(6000000000, 9999999999)}",
                full_name=f"Citizen_{i}_{uuid.uuid4().hex[:4]}",
                preferred_language=random.choice(["en", "hi", "ta", "ml"])
            )
            self.db.add(c)
            # flush every 100 for memory safety
            if i % 100 == 0:
                self.db.flush()
        self.db.commit()
        return [c.id for c in self.db.query(Citizen).all()]

    def _seed_tickets(self, citizen_ids: List[int], count: int):
        current_count = self.db.query(Ticket).count()
        if current_count >= count:
            return
            
        depts = self.db.query(Department).all()
        dept_ids = [d.id for d in depts]
        
        logger.info(f"Seeding {count - current_count} historical tickets...")
        
        for i in range(count - current_count):
            # Create a realistic historical timeline
            created_at = datetime.utcnow() - timedelta(days=random.randint(0, 365))
            priority = random.choice(list(Priority))
            status = random.choice(list(TicketStatus))
            
            resolved_at = None
            if status in [TicketStatus.RESOLVED, TicketStatus.CLOSED]:
                resolved_at = created_at + timedelta(hours=random.randint(1, 120))
                
            cat = random.choice(list(GRIEVANCE_KNOWLEDGE_BASE.keys()))
            
            t = Ticket(
                ticket_id=f"TKT-{uuid.uuid4().hex[:6].upper()}",
                citizen_id=random.choice(citizen_ids),
                department_id=random.choice(dept_ids),
                complaint_text=f"Example grievance for {cat} reported via auto-simulation.",
                category=cat,
                priority=priority,
                status=status,
                created_at=created_at,
                resolved_at=resolved_at,
                sla_deadline=created_at + timedelta(hours=24),
                language_code=random.choice(["en", "hi", "ta"])
            )
            self.db.add(t)
            if i % 250 == 0:
                self.db.flush()
                logger.debug(f"Seeded {i} tickets...")
                
        self.db.commit()

if __name__ == "__main__":
    seeder = MassiveSeeder()
    seeder.run()
