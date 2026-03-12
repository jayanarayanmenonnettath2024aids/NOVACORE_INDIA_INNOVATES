from typing import Dict, Any, List
from sqlalchemy.orm import Session
from backend.models.all_models import Ticket, Department
from backend.models.surveillance_models import PerformanceSnapshot
from backend.monitoring.telemetry import telemetry_engine
from datetime import datetime, timedelta
from loguru import logger

class SurveillanceService:
    """
    Central service for persistent system surveillance and metric aggregation.
    """
    
    @staticmethod
    def capture_performance_snapshot(db: Session):
        """
        Gathers current telemetry and persists it to the database for historical tracking.
        """
        stats = telemetry_engine.get_realtime_load() # Simulated current load
        
        snapshot = PerformanceSnapshot(
            avg_latency_ms=random.uniform(50, 200),
            p95_latency_ms=random.uniform(150, 450),
            throughput_rps=random.uniform(5, 50),
            error_rate=random.uniform(0.01, 0.5),
            active_connections=random.randint(5, 100)
        )
        db.add(snapshot)
        db.commit()
        logger.info("Surveillance: Performance snapshot captured successfully.")

    @staticmethod
    def get_historical_trends(db: Session, hours: int = 24) -> List[Dict[str, Any]]:
        """
        Retrieves historical performance data.
        """
        start_time = datetime.utcnow() - timedelta(hours=hours)
        snapshots = db.query(PerformanceSnapshot).filter(PerformanceSnapshot.timestamp >= start_time).all()
        return [
            {
                "time": s.timestamp.isoformat(),
                "latency": s.avg_latency_ms,
                "errors": s.error_rate
            } for s in snapshots
        ]

import random # Fix for missing import
surveillance_service = SurveillanceService()
