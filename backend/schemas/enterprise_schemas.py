from typing import List, Optional, Any, Dict
from pydantic import BaseModel, Field, EmailStr, validator
from datetime import datetime
from uuid import UUID
from backend.models.all_models import TicketStatus, Priority

# --- Citizen Schemas ---

class CitizenBase(BaseModel):
    phone_number: str = Field(..., pattern=r"^\+?1?\d{9,15}$")
    full_name: str = Field(..., min_length=2, max_length=100)
    preferred_language: str = Field("en", pattern="^(en|hi|ta|ml|te|kn)$")

class CitizenCreate(CitizenBase):
    pass

class CitizenUpdate(BaseModel):
    full_name: Optional[str]
    preferred_language: Optional[str]
    metadata: Optional[Dict[str, Any]]

class Citizen(CitizenBase):
    id: int
    citizen_uuid: UUID
    created_at: datetime

    class Config:
        orm_mode = True

# --- Ticket Schemas ---

class TicketBase(BaseModel):
    complaint_text: str = Field(..., min_length=10, max_length=2000)
    category: str
    priority: Priority = Priority.MEDIUM
    language_code: str = "en"

class TicketCreate(TicketBase):
    citizen_id: int
    department_id: Optional[int]
    metadata_json: Optional[Dict[str, Any]]

class TicketUpdate(BaseModel):
    status: Optional[TicketStatus]
    priority: Optional[Priority]
    department_id: Optional[int]
    resolved_at: Optional[datetime]
    internal_notes: Optional[str]

class Ticket(TicketBase):
    id: int
    ticket_id: str
    status: TicketStatus
    citizen_id: int
    department_id: Optional[int]
    created_at: datetime
    resolved_at: Optional[datetime]
    sla_deadline: datetime
    
    citizen: Optional[Citizen]
    
    class Config:
        orm_mode = True

# --- Department Schemas ---

class DepartmentBase(BaseModel):
    name: str
    description: Optional[str]
    responsible_officer: Optional[str]

class DepartmentCreate(DepartmentBase):
    pass

class Department(DepartmentBase):
    id: int
    active_tickets_count: Optional[int] = 0
    
    class Config:
        orm_mode = True

# --- Analytics Schemas ---

class DashboardStats(BaseModel):
    total_tickets: int
    active_tickets: int
    resolved_tickets: int
    sla_breaches: int
    category_distribution: Dict[str, int]
    priority_distribution: Dict[str, int]
    daily_trend: List[Dict[str, Any]]

class DepartmentPerformance(BaseModel):
    department_name: str
    resolution_rate: float
    avg_resolution_time_hrs: float
    sla_compliance_percent: float

# --- Surveillance & Monitoring (Expanded) ---

class PerformanceMetric(BaseModel):
    metric: str
    value: float
    unit: str
    timestamp: datetime

class SystemHealth(BaseModel):
    status: str
    components: Dict[str, str]
    load: float
    uptime_seconds: int

# --- AI & Telephony (Expanded) ---

class CallTranscription(BaseModel):
    call_sid: str
    transcript: str
    confidence: float
    sentiment: Optional[float]
    language: str

class AIClassificationResult(BaseModel):
    category: str
    sub_category: Optional[str]
    priority: Priority
    confidence: float
    entities: List[Dict[str, str]]
    summary: str
