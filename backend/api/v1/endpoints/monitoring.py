from fastapi import APIRouter, Depends
from typing import Dict, Any, List
from backend.monitoring.system_health import monitoring_service
from backend.monitoring.alert_engine import alert_engine
from backend.monitoring.performance_profiler import profiler
from backend.monitoring.telemetry import telemetry_engine

router = APIRouter()

@router.get("/health")
def get_system_health():
    """Returns comprehensive system health status."""
    return monitoring_service.get_system_stats()

@router.get("/alerts")
def get_active_alerts():
    """Returns the most recent system-critical alerts."""
    return alert_engine.get_active_alerts()

@router.get("/telemetry")
def get_system_telemetry():
    """Returns real-time performance and load telemetry."""
    return {
        "current_load": telemetry_engine.get_realtime_load(),
        "avg_latency": profiler.get_latency_report(),
        "throughput_calls_per_min": 45 # Simulated
    }

@router.post("/alert/test")
def trigger_test_alert():
    """Utility to test the alerting system manually."""
    alert_engine._trigger_alert("TEST_ALERT", "This is a manually triggered system test alert.", "INFO")
    return {"status": "Alert triggered"}
