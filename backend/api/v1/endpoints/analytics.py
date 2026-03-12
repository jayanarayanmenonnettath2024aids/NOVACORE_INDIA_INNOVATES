from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.database.session import get_db
from backend.services.analytics_service import analytics_service

router = APIRouter()

@router.get("/dashboard")
def get_dashboard_analytics(db: Session = Depends(get_db)):
    return analytics_service.get_dashboard_data(db)

@router.get("/performance")
def get_department_performance(db: Session = Depends(get_db)):
    return analytics_service.get_department_performance(db)
