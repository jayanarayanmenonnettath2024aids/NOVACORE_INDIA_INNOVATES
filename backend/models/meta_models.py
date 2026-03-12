from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, Float
from sqlalchemy.orm import relationship
from backend.database.session import Base
from datetime import datetime

class AuditLog(Base):
    """
    Persistent record of administrative actions.
    """
    __tablename__ = "audit_logs"
    
    id = Column(Integer, primary_key=True, index=True)
    admin_user = Column(String, index=True)
    action = Column(String, index=True)
    target_entity = Column(String) # e.g. "TICKET", "CITIZEN"
    target_id = Column(String)
    timestamp = Column(DateTime, default=datetime.utcnow)
    details = Column(Text)

class SystemMetric(Base):
    """
    Stores historical system performance snapshots.
    """
    __tablename__ = "system_metrics"
    
    id = Column(Integer, primary_key=True)
    metric_name = Column(String, index=True) # "CPU", "MEMORY", "LATENCY"
    value = Column(Float)
    timestamp = Column(DateTime, default=datetime.utcnow)

class AIInferenceLog(Base):
    """
    Logs every inference made by the AI models for quality assurance.
    """
    __tablename__ = "ai_inference_logs"
    
    id = Column(Integer, primary_key=True)
    session_id = Column(String, index=True)
    input_text = Column(Text)
    output_json = Column(Text)
    confidence = Column(Float)
    latency_ms = Column(Float)
    created_at = Column(DateTime, default=datetime.utcnow)
