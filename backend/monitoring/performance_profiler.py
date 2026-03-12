import time
import functools
from typing import Dict, Any, List
from loguru import logger
from datetime import datetime

class PerformanceProfiler:
    """
    Simulates a production-scale application profiler.
    Tracks execution time of critical AI and database functions to identify bottlenecks.
    """
    def __init__(self):
        self.profile_data: List[Dict[str, Any]] = []
        logger.info("PerformanceProfiler active: Instrumenting system execution.")

    def trace(self, name: str):
        """
        Decorator for profiling function execution time.
        """
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                start = time.perf_counter()
                result = func(*args, **kwargs)
                end = time.perf_counter()
                latency = (end - start) * 1000 # ms
                
                self._record(name, latency)
                return result
            return wrapper
        return decorator

    def _record(self, name: str, latency_ms: float):
        entry = {
            "timestamp": datetime.utcnow().isoformat(),
            "function": name,
            "latency_ms": round(latency_ms, 2)
        }
        self.profile_data.append(entry)
        if latency_ms > 500: # Threshold for slow calls
            logger.warning(f"PERF_WARNING | {name} took {latency_ms:.2f}ms")
            
        # Keep buffer manageable
        if len(self.profile_data) > 1000:
            self.profile_data = self.profile_data[-1000:]

    def get_latency_report(self) -> Dict[str, float]:
        if not self.profile_data:
            return {}
        # Simple simulation of avg calculation
        return { "avg_ms": sum(d["latency_ms"] for d in self.profile_data) / len(self.profile_data) }

profiler = PerformanceProfiler()
