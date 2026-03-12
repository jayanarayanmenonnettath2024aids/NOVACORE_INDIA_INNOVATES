# Production Simulation script for generating massive data volume
import sys
import os
from sqlalchemy.orm import Session
from backend.database.session import SessionLocal
from backend.services.telephony_service import telephony_service
import random
from loguru import logger

# Add project root to sys path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def run_massive_simulation(iterations: int = 500):
    db: Session = SessionLocal()
    
    logger.info(f"INITIATING MASSIVE CITIZEN INTERACTION SIMULATION: {iterations} SESSIONS")
    
    phones = [f"+9188888{i:05d}" for i in range(200)]
    complaints = [
        "My street is flooded due to a drain block.",
        "Electrical transformer is making loud noises and sparking.",
        "There's a broken road signal at the main junction causing chaos.",
        "No garbage collection for the last ten days in this area.",
        "Someone is stealing batteries from the public charging station.",
        "Supply of drinking water is highly turbid today.",
        "Streetlight poles are leaning dangerously after the storm.",
        "Power outage reported in the entire apartment block.",
        "Illegal garbage dumping in the lake bed.",
        "Abandoned vehicle is blocking the primary fire exit route."
    ]

    success_count = 0
    for i in range(iterations):
        try:
            phone = random.choice(phones)
            speech = random.choice(complaints)
            
            # Simulate the full pipeline
            telephony_service.process_inbound_call(db, phone, speech)
            
            if (i + 1) % 50 == 0:
                logger.info(f"Progress: {i + 1}/{iterations} tickets successfully injected.")
            
            success_count += 1
        except Exception as e:
            logger.error(f"Simulation failed at iteration {i}: {e}")
            
    db.close()
    logger.info(f"SIMULATION COMPLETE. {success_count} production-scale records created.")

if __name__ == "__main__":
    # Note: DB must be initialized first!
    run_massive_simulation(100) # Generating 100 deep records
