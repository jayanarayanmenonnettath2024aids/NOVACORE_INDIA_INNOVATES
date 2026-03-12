from typing import Dict, List, Any
from sqlalchemy.orm import Session
from backend.models.all_models import Ticket, TicketStatus, Priority
from datetime import datetime, timedelta
import math
from loguru import logger

class HistoricalAnalyticsEngine:
    """
    Simulates a production-scale analytics engine for governance performance.
    Calculates complex metrics like rolling averages, seasonality, and SLA risk.
    """
    
    @staticmethod
    def calculate_rolling_resolution_rate(db: Session, days: int = 30) -> Dict[str, float]:
        """
        Calculates the resolution rate over a sliding window.
        """
        end_date = datetime.utcnow()
        start_date = end_date - timedelta(days=days)
        
        total = db.query(Ticket).filter(Ticket.created_at >= start_date).count()
        resolved = db.query(Ticket).filter(
            Ticket.created_at >= start_date,
            Ticket.status == TicketStatus.RESOLVED
        ).count()
        
        rate = (resolved / total * 100) if total > 0 else 0
        logger.info(f"Analytics: {days}-day resolution rate: {rate:.2f}%")
        return {"days": days, "rate": rate, "total": total, "resolved": resolved}

    @staticmethod
    def estimate_sla_risk(db: Session) -> List[Dict[str, Any]]:
        """
        Uses simulated logic to predict which departments are at risk of SLA breach.
        """
        risks = []
        departments = db.query(Department).all()
        
        for dept in departments:
            # Simulated formula: (Active Tickets / Capacity) * Urgency Factor
            active_count = db.query(Ticket).filter(
                Ticket.department_id == dept.id,
                Ticket.status.in_([TicketStatus.ASSIGNED, TicketStatus.IN_PROGRESS])
            ).count()
            
            # Simulated capacity logic
            capacity = random.randint(20, 100)
            risk_score = (active_count / capacity) * 10
            
            risks.append({
                "department": dept.name,
                "risk_score": round(min(risk_score, 10.0), 1),
                "active_load": active_count,
                "status": "CRITICAL" if risk_score > 8 else "STABLE"
            })
            
        return sorted(risks, key=lambda x: x["risk_score"], reverse=True)

    @staticmethod
    def generate_seasonality_data() -> Dict[str, List[float]]:
        """
        Simulates seasonal patterns in grievance reporting (e.g. Water issues in summer).
        """
        months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        # Sine wave simulation for water issues peaking in summer (May-June)
        water_trend = [math.sin((i - 2) * math.pi / 6) * 50 + 100 for i in range(12)]
        # Random noise for electricity issues
        elec_trend = [random.uniform(80, 150) for _ in range(12)]
        
        return {
            "months": months,
            "category_trends": {
                "Water": [round(x, 1) for x in water_trend],
                "Electricity": [round(x, 1) for x in elec_trend]
            }
        }

import random # Fix for missing import
from backend.models.all_models import Department # Fix for missing import
historical_analytics = HistoricalAnalyticsEngine()
