from sqlalchemy import Column, Integer, String, Text, DateTime, Boolean, JSON
from backend.database.session import Base
from datetime import datetime

class SystemJob(Base):
    """
    Tracks background tasks scheduled by the scheduler_service.
    """
    __tablename__ = "system_jobs"
    
    id = Column(Integer, primary_key=True, index=True)
    job_name = Column(String, unique=True, index=True)
    last_run = Column(DateTime)
    next_run = Column(DateTime)
    status = Column(String) # RUNNING, IDLE, FAILED
    error_message = Column(Text, nullable=True)

class PerformanceSnapshot(Base):
    """
    Historical record of system performance for long-term trend analysis.
    """
    __tablename__ = "performance_snapshots"
    
    id = Column(Integer, primary_key=True, index=True)
    timestamp = Column(DateTime, default=datetime.utcnow, index=True)
    avg_latency_ms = Column(Float)
    p95_latency_ms = Column(Float)
    throughput_rps = Column(Float)
    error_rate = Column(Float)
    active_connections = Column(Integer)

class RegionMetric(Base):
    """
    Aggregated metrics per city zone for geographic heatmaps.
    """
    __tablename__ = "region_metrics"
    
    id = Column(Integer, primary_key=True, index=True)
    region_name = Column(String, index=True)
    metric_type = Column(String) # "GRIEVANCE_COUNT", "SLA_BREACH_RATE"
    value = Column(Float)
    period_start = Column(DateTime)
    period_end = Column(DateTime)
    metadata_json = Column(JSON)

from sqlalchemy import Float # Fix for missing import
