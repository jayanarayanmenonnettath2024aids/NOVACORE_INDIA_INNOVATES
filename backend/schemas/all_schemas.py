from typing import List, Optional
from pydantic import BaseModel, Field
from datetime import datetime
from .all_models import TicketStatus, Priority

# CITIZEN SCHEMAS
class CitizenBase(BaseModel):
    phone_number: str
    full_name: Optional[str] = None
    preferred_language: str = "English"
    location_lat: Optional[str] = None
    location_lng: Optional[str] = None
    address: Optional[str] = None

class CitizenCreate(CitizenBase):
    pass

class CitizenUpdate(CitizenBase):
    phone_number: Optional[str] = None

class Citizen(CitizenBase):
    id: int
    citizen_uuid: str
    created_at: datetime
    is_active: bool

    class Config:
        from_attributes = True

# TICKET SCHEMAS
class TicketBase(BaseModel):
    complaint_text: str
    category: str
    priority: Priority = Priority.MEDIUM
    language_code: str = "en"
    metadata_json: Optional[dict] = None

class TicketCreate(TicketBase):
    citizen_id: int

class TicketUpdate(BaseModel):
    status: Optional[TicketStatus] = None
    priority: Optional[Priority] = None
    department_id: Optional[int] = None
    ai_summary: Optional[str] = None
    resolved_at: Optional[datetime] = None

class Ticket(TicketBase):
    id: int
    ticket_id: str
    citizen_id: int
    department_id: Optional[int] = None
    status: TicketStatus
    created_at: datetime
    updated_at: datetime
    sla_deadline: Optional[datetime] = None

    class Config:
        from_attributes = True

# DEPARTMENT SCHEMAS
class DepartmentBase(BaseModel):
    name: str
    description: Optional[str] = None
    responsible_officer: Optional[str] = None
    contact_email: Optional[str] = None
    contact_phone: Optional[str] = None

class Department(DepartmentBase):
    id: int

    class Config:
        from_attributes = True

# STATS SCHEMAS
class DashboardStats(BaseModel):
    total_calls: int
    active_tickets: int
    resolved_tickets: int
    high_priority_count: int
    avg_resolution_hours: float
    category_distribution: dict
    department_workload: dict
