from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text, Enum, JSON, Boolean
from sqlalchemy.orm import relationship
import enum
from datetime import datetime
from .session import Base

class TicketStatus(str, enum.Enum):
    RECEIVED = "Received"
    ASSIGNED = "Assigned"
    IN_PROGRESS = "In Progress"
    ESCALATED = "Escalated"
    RESOLVED = "Resolved"
    CLOSED = "Closed"

class Priority(str, enum.Enum):
    LOW = "Low"
    MEDIUM = "Medium"
    HIGH = "High"
    CRITICAL = "Critical"

class Citizen(Base):
    __tablename__ = "citizens"
    
    id = Column(Integer, primary_key=True, index=True)
    citizen_uuid = Column(String(36), unique=True, index=True)
    phone_number = Column(String(20), unique=True, index=True)
    full_name = Column(String(100), nullable=True)
    preferred_language = Column(String(20), default="English")
    location_lat = Column(String(20), nullable=True)
    location_lng = Column(String(20), nullable=True)
    address = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    is_active = Column(Boolean, default=True)
    
    tickets = relationship("Ticket", back_populates="citizen")
    calls = relationship("CallLog", back_populates="citizen")

class Department(Base):
    __tablename__ = "departments"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True, index=True)
    description = Column(Text, nullable=True)
    responsible_officer = Column(String(100), nullable=True)
    contact_email = Column(String(100), nullable=True)
    contact_phone = Column(String(20), nullable=True)
    
    tickets = relationship("Ticket", back_populates="department")

class Ticket(Base):
    __tablename__ = "tickets"
    
    id = Column(Integer, primary_key=True, index=True)
    ticket_id = Column(String(12), unique=True, index=True)
    citizen_id = Column(Integer, ForeignKey("citizens.id"))
    department_id = Column(Integer, ForeignKey("departments.id"), nullable=True)
    
    complaint_text = Column(Text, nullable=False)
    ai_summary = Column(Text, nullable=True)
    category = Column(String(50), index=True)
    status = Column(Enum(TicketStatus), default=TicketStatus.RECEIVED)
    priority = Column(Enum(Priority), default=Priority.MEDIUM)
    language_code = Column(String(10))
    
    metadata_json = Column(JSON, nullable=True)
    
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    resolved_at = Column(DateTime, nullable=True)
    sla_deadline = Column(DateTime, nullable=True)
    
    citizen = relationship("Citizen", back_populates="tickets")
    department = relationship("Department", back_populates="tickets")
    history = relationship("TicketHistory", back_populates="ticket")
    notifications = relationship("NotificationLog", back_populates="ticket")

class TicketHistory(Base):
    __tablename__ = "ticket_history"
    
    id = Column(Integer, primary_key=True, index=True)
    ticket_id = Column(Integer, ForeignKey("tickets.id"))
    old_status = Column(Enum(TicketStatus), nullable=True)
    new_status = Column(Enum(TicketStatus))
    change_reason = Column(Text, nullable=True)
    changed_by = Column(String(50), default="AI_SYSTEM")
    timestamp = Column(DateTime, default=datetime.utcnow)
    
    ticket = relationship("Ticket", back_populates="history")

class CallLog(Base):
    __tablename__ = "call_logs"
    
    id = Column(Integer, primary_key=True, index=True)
    call_sid = Column(String(50), unique=True, index=True)
    citizen_id = Column(Integer, ForeignKey("citizens.id"))
    direction = Column(String(10)) # "Inbound" or "Outbound"
    duration_seconds = Column(Integer, default=0)
    transcript = Column(Text, nullable=True)
    sentiment_score = Column(JSON, nullable=True)
    timestamp = Column(DateTime, default=datetime.utcnow)
    
    citizen = relationship("Citizen", back_populates="calls")

class NotificationLog(Base):
    __tablename__ = "notification_logs"
    
    id = Column(Integer, primary_key=True, index=True)
    ticket_id = Column(Integer, ForeignKey("tickets.id"))
    channel = Column(String(20)) # "SMS", "WhatsApp", "Voice"
    recipient = Column(String(50))
    template_name = Column(String(50))
    sent_at = Column(DateTime, default=datetime.utcnow)
    status = Column(String(20)) # "Sent", "Delivered", "Failed"
    
    ticket = relationship("Ticket", back_populates="notifications")
