from sqlalchemy.orm import Session
from backend.database.session import SessionLocal
from backend.models.all_models import Department, Citizen, Ticket, TicketStatus, Priority
from datetime import datetime, timedelta
import random

def seed_database():
    db = SessionLocal()
    
    # 1. Departments
    departments = [
        {"name": "Water Supply Department", "officer": "Mr. Arjun S."},
        {"name": "Electricity Board", "officer": "Ms. Priya K."},
        {"name": "Municipal Roads Department", "officer": "Mr. Rajesh V."},
        {"name": "City Sanitation Department", "officer": "Ms. Deepa R."},
        {"name": "Police Department", "officer": "Inspector Khan"}
    ]
    
    for d_data in departments:
        if not db.query(Department).filter(Department.name == d_data["name"]).first():
            dept = Department(
                name=d_data["name"],
                responsible_officer=d_data["officer"],
                description=f"Handles all {d_data['name'].lower()} related issues."
            )
            db.add(dept)
    
    db.commit()
    
    # 2. Citizens (Simulate 50 initial citizens)
    if db.query(Citizen).count() == 0:
        for i in range(50):
            citizen = Citizen(
                citizen_uuid=f"SIM-{i:03d}",
                phone_number=f"+9199999{i:05d}",
                full_name=f"Citizen {i}",
                preferred_language=random.choice(["English", "Hindi", "Tamil", "Telugu"])
            )
            db.add(citizen)
        db.commit()

    # 3. Tickets (Simulate various states)
    if db.query(Ticket).count() == 0:
        citizen_ids = [c.id for c in db.query(Citizen).all()]
        dept_ids = [d.id for d in db.query(Department).all()]
        
        for i in range(200):
            status = random.choice(list(TicketStatus))
            priority = random.choice(list(Priority))
            
            # Historical timestamps
            created = datetime.utcnow() - timedelta(days=random.randint(1, 30))
            resolved = None
            if status in [TicketStatus.RESOLVED, TicketStatus.CLOSED]:
                resolved = created + timedelta(hours=random.randint(4, 96))
                
            ticket = Ticket(
                ticket_id=f"TKT{i:05d}",
                citizen_id=random.choice(citizen_ids),
                department_id=random.choice(dept_ids),
                complaint_text=f"Sample issue #{i} for testing PALLAVI AI system scalability.",
                category=random.choice(["Water", "Electricity", "Roads", "Sanitation", "Public Safety"]),
                status=status,
                priority=priority,
                created_at=created,
                resolved_at=resolved,
                sla_deadline=created + timedelta(hours=24)
            )
            db.add(ticket)
        db.commit()
        print("Database seeded with 200+ tickets.")

if __name__ == "__main__":
    seed_database()
