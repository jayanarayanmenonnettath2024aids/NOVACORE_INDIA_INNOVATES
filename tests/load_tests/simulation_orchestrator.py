import asyncio
import aiohttp
import time
from typing import List, Dict, Any
from loguru import logger
import random

class LoadSimulationOrchestrator:
    """
    High-fidelity load tester for the PALLAVI AI gateway.
    Simulates thousands of concurrent citizen calls and API interactions.
    """
    
    def __init__(self, base_url: str = "http://localhost:8000"):
        self.base_url = base_url
        self.results: List[Dict[str, Any]] = []
        logger.info(f"LoadSimulator ready: Targeting {base_url}")

    async def simulate_burst(self, call_count: int, concurrency: int = 10):
        """
        Executes a burst of simulated calls.
        """
        logger.info(f"LoadBurst: Starting {call_count} calls with concurrency {concurrency}")
        start_time = time.time()
        
        semaphore = asyncio.Semaphore(concurrency)
        tasks = []
        
        async with aiohttp.ClientSession() as session:
            for i in range(call_count):
                task = self._single_call_simulation(session, semaphore, i)
                tasks.append(task)
            
            await asyncio.gather(*tasks)
            
        duration = time.time() - start_time
        logger.info(f"LoadBurst: Completed {call_count} calls in {duration:.2f}s ({call_count/duration:.1f} rps)")

    async def _single_call_simulation(self, session, semaphore, call_id):
        async with semaphore:
            payload = {
                "phone_number": f"+9198{random.randint(10000000, 99999999)}",
                "speech_text": "Greetings, there is a major issue with the power lines here."
            }
            try:
                start = time.perf_counter()
                async with session.post(f"{self.base_url}/api/v1/telephony/inbound", json=payload) as resp:
                    latency = (time.perf_counter() - start) * 1000
                    status = resp.status
                    self.results.append({"id": call_id, "latency": latency, "status": status})
            except Exception as e:
                logger.error(f"SimCall {call_id} failed: {e}")

    def get_summary_stats(self) -> Dict[str, Any]:
        if not self.results: return {}
        latencies = [r["latency"] for r in self.results]
        return {
            "total": len(self.results),
            "avg_latency_ms": sum(latencies) / len(latencies),
            "max_latency_ms": max(latencies),
            "p95_latency_ms": sorted(latencies)[int(0.95 * len(latencies))],
            "success_rate": len([r for r in self.results if r["status"] == 200]) / len(self.results)
        }

if __name__ == "__main__":
    # In practice, this would be run via a script
    orchestrator = LoadSimulationOrchestrator()
    asyncio.run(orchestrator.simulate_burst(100))
