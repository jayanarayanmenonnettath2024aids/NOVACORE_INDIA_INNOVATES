import psutil
import platform
import time
from typing import Dict, Any
from loguru import logger
from backend.database.session import SessionLocal

class MonitoringService:
    """
    Monitors system health, database connectivity, and hardware resource usage.
    Ensures the PALLAVI platform meets high-availability government standards.
    """
    
    @staticmethod
    def get_system_stats() -> Dict[str, Any]:
        """
        Retrieves real-time OS and hardware metrics.
        """
        cpu_usage = psutil.cpu_percent(interval=None)
        memory = psutil.virtual_memory()
        disk = psutil.disk_usage('/')
        
        # Database connectivity check
        db_alive = False
        try:
            db = SessionLocal()
            db.execute("SELECT 1")
            db_alive = True
            db.close()
        except Exception as e:
            logger.error(f"Database health check failed: {e}")
            
        return {
            "timestamp": datetime.utcnow().isoformat(),
            "os": platform.system(),
            "cpu_percent": cpu_usage,
            "memory_percent": memory.percent,
            "disk_free_gb": disk.free // (1024**3),
            "database_status": "UP" if db_alive else "DOWN",
            "uptime_seconds": time.monotonic(),
            "active_ai_threads": 4 # Simulated
        }

    @staticmethod
    def log_incident(module: str, severity: str, message: str):
        """Logs an operational incident to the monitoring audit trail."""
        logger.critical(f"HEALTH_ALERT | Module: {module} | Severity: {severity} | Msg: {message}")

from datetime import datetime # Fix for missing import
monitoring_service = MonitoringService()
