from typing import Dict, Any, List
from sqlalchemy.orm import Session
from backend.models.all_models import Ticket, Department
from backend.services.historical_analytics import historical_analytics
from backend.services.geospatial_service import geospatial_service
from backend.monitoring.telemetry import telemetry_engine
from loguru import logger

class AdvancedAnalyticsGateway:
    """
    Combines spatial, historical, and real-time data for high-level administration insights.
    """
    
    @staticmethod
    def get_city_health_score(db: Session) -> float:
        """
        Calculates a proprietary 'City Health' metric (0-100).
        Factors: SLA Resolution Rate, Urgent Incident Volume, Sentiment (simulated).
        """
        # 1. Historical Resolution
        res_data = historical_analytics.calculate_rolling_resolution_rate(db, 7)
        res_rate = res_data["rate"]
        
        # 2. Risk Factors
        risks = historical_analytics.estimate_sla_risk(db)
        avg_risk = sum(r["risk_score"] for r in risks) / len(risks) if risks else 0
        
        # 3. System Load
        load = telemetry_engine.get_realtime_load()
        
        # Weighted Score
        score = (res_rate * 0.5) + ( (10 - avg_risk) * 4 ) + ( (1 - load) * 10 )
        return round(min(score, 100.0), 1)

    @staticmethod
    def get_regional_hotspots(db: Session) -> List[Dict[str, Any]]:
        """
        Returns spatial clusters for the GIS dashboard layer.
        """
        # Simulated point generation from tickets
        tickets = db.query(Ticket).limit(100).all()
        points = [geospatial_service.generate_random_city_point() for _ in tickets]
        return geospatial_service.identify_clusters(points)

advanced_analytics = AdvancedAnalyticsGateway()
