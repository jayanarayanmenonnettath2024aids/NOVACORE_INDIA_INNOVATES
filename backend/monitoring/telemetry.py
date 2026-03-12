from typing import Dict, Any, List
import time
import random
from loguru import logger
from datetime import datetime

class TelemetryEngine:
    """
    Simulates a high-frequency telemetry system (similar to Prometheus/Grafana).
    Tracks internal AI latencies, system throughput, and call failure rates.
    """
    def __init__(self):
        self.metrics_buffer: List[Dict[str, Any]] = []
        logger.info("TelemetryEngine initialized for real-time surveillance.")

    def record_interaction_telemetry(
        self, 
        session_id: str, 
        stt_latency: float, 
        ai_latency: float, 
        success: bool
    ):
        """
        Records the performance metrics of a single call interaction.
        """
        metric = {
            "timestamp": datetime.utcnow().isoformat(),
            "session_id": session_id,
            "stt_latency_ms": stt_latency,
            "ai_latency_ms": ai_latency,
            "total_latency_ms": stt_latency + ai_latency,
            "status": "SUCCESS" if success else "FAILURE"
        }
        self.metrics_buffer.append(metric)
        
        # simulated push to an external TSDB (Time Series Database)
        if len(self.metrics_buffer) > 20:
            self._flush_telemetry()

    def _flush_telemetry(self):
        """
        Simulates pushing buffered metrics to an analytics sink.
        """
        count = len(self.metrics_buffer)
        logger.debug(f"Telemetry Flush: Pushing {count} interaction records to Monitoring Sink.")
        # production simulation would do an async HTTP post here
        self.metrics_buffer = []

    @staticmethod
    def get_realtime_load() -> float:
        """Simulates current system load for the dashboard."""
        return round(random.uniform(0.1, 0.95), 2)

telemetry_engine = TelemetryEngine()
