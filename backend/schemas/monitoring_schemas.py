from typing import List, Optional
from pydantic import BaseModel, Field
from datetime import datetime
from backend.models.all_models import TicketStatus, Priority

class TelemetrySnapshot(BaseModel):
    timestamp: datetime
    avg_latency: float
    error_rate: float
    current_load: float

class CityHealthReport(BaseModel):
    overall_score: float
    resolution_rate: float
    active_critical_alerts: int
    risk_by_department: List[Dict[str, Any]]

class DeploymentConfig(BaseModel):
    environment: str
    version: str
    nodes_active: int
    last_deployment: datetime
    
class AuditFilter(BaseModel):
    ticket_id: Optional[str]
    actor: Optional[str]
    start_date: Optional[datetime]
    end_date: Optional[datetime]

from typing import Dict # Fix for missing import
