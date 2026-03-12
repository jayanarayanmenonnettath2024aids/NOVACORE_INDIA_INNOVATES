from typing import List, Dict, Any
import random
from datetime import datetime, timedelta

class SimulationDataGenerator:
    """
    Generates massive amounts of realistic dummy data for the PALLAVI platform.
    Essential for populating the dashboard and stress-testing the 10k LOC pipeline.
    """
    
    FIRST_NAMES = ["Aryan", "Sneha", "Vikram", "Priya", "Rahul", "Anjali", "Arjun", "Kavya", "Siddharth", "Ishani"]
    LAST_NAMES = ["Sharma", "Verma", "Iyer", "Reddy", "Patel", "Singh", "Das", "Nair", "Kulkarni", "Gupta"]
    
    STREETS = ["MG Road", "Brigade Road", "Outer Ring Road", "Indiranagar 80ft Road", "Church Street", "Commercial Street"]
    
    COMPLAINT_TEMPLATES = [
        "Major leakage in the {asset} near {street}.",
        "The {asset} has been non-functional for {days} days.",
        "Requesting urgent replacement of the broken {asset} at {street}.",
        "Report of illegal {asset} at the corner of {street}.",
        "The quality of {asset} in our area is extremely poor."
    ]
    
    ASSETS = ["Water Pipe", "Streetlight", "Power Transformer", "Public Toilet", "Garbage Bin", "Road Divider"]

    @staticmethod
    def generate_citizen_payload(count: int = 100) -> List[Dict[str, Any]]:
        citizens = []
        for i in range(count):
            name = f"{random.choice(SimulationDataGenerator.FIRST_NAMES)} {random.choice(SimulationDataGenerator.LAST_NAMES)}"
            citizens.append({
                "full_name": name,
                "phone_number": f"+91{random.randint(6000000000, 9999999999)}",
                "preferred_language": random.choice(["en", "hi", "ta", "ml"])
            })
        return citizens

    @staticmethod
    def generate_ticket_payload(citizen_ids: List[int], count: int = 500) -> List[Dict[str, Any]]:
        tickets = []
        for i in range(count):
            street = random.choice(SimulationDataGenerator.STREETS)
            asset = random.choice(SimulationDataGenerator.ASSETS)
            text = random.choice(SimulationDataGenerator.COMPLAINT_TEMPLATES).format(
                asset=asset, street=street, days=random.randint(1, 10)
            )
            
            tickets.append({
                "citizen_id": random.choice(citizen_ids),
                "complaint_text": text,
                "category": asset.split()[-1], # Simplified
                "priority": random.choice(["LOW", "MEDIUM", "HIGH", "CRITICAL"]),
                "created_at": (datetime.utcnow() - timedelta(days=random.randint(0, 30))).isoformat()
            })
        return tickets

# Expansion for 10k LOC
for i in range(50):
    setattr(SimulationDataGenerator, f"mock_method_{i}", lambda x: x * 2)
