from fastapi import APIRouter, Depends, BackgroundTasks
from sqlalchemy.orm import Session
from backend.database.session import get_db
from backend.services.reporting_service import reporting_service
from backend.database.seeder.massive_seeder import MassiveSeeder
from backend.monitoring.alert_engine import alert_engine
from loguru import logger

router = APIRouter()

@router.post("/reports/daily-summary")
def trigger_daily_report(db: Session = Depends(get_db)):
    """Triggers the generation of a daily grievance summary."""
    report = reporting_service.generate_daily_grievance_report(db)
    return {"message": "Report generated", "content": report}

@router.post("/system/seed")
def trigger_system_seed(background_tasks: BackgroundTasks, citizen_count: int = 100, ticket_count: int = 500):
    """Triggers a massive database seeding operation in the background."""
    def run_seeder():
        seeder = MassiveSeeder()
        seeder.run({"citizens": citizen_count, "tickets": ticket_count})
        
    background_tasks.add_task(run_seeder)
    return {"status": "Seeding initiated in background."}

@router.get("/system/events")
def get_system_events():
    """Returns the high-level system event log for administrators."""
    return alert_engine.get_active_alerts()

@router.post("/system/shutdown")
def shutdown_node():
    """Simulates a secure node shutdown for maintenance."""
    logger.warning("System shutdown signal received. Preparing for safe termination.")
    # In real app, this would trigger uvicorn shutdown
    return {"message": "Shutdown sequence initiated."}
