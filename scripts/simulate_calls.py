import requests
import random
import time
from typing import List

API_BASE = "http://localhost:8000/api/v1"

CITIZENS_PHONES = [
    f"+9198765{i:05d}" for i in range(100)
]

COMPLAINTS = [
    "There is a massive water pipe burst in the main square. Water is everywhere!",
    "I haven't had electricity for 3 days. Please help.",
    "Road pothole near the school is causing accidents. It's very dangerous.",
    "Garbage has not been collected for a week. The smell is unbearable.",
    "I saw someone suspicious near the bank. Public safety is at risk.",
    "Streetlights are flickering and some are broken on my street.",
    "The drainage system is blocked and overflowing into my yard.",
    "High voltage fluctuation is damaging my appliances.",
    "There is a huge traffic jam due to a broken signal at the intersection.",
    "Someone is dumping industrial waste in the local park."
]

def simulate_calls(count: int = 50):
    print(f"Starting simulation of {count} citizen interactions...")
    
    for i in range(count):
        phone = random.choice(CITIZENS_PHONES)
        text = random.choice(COMPLAINTS)
        
        payload = {
            "phone_number": phone,
            "speech_text": text
        }
        
        try:
            response = requests.post(f"{API_BASE}/telephony/inbound", json=payload)
            if response.status_code == 200:
                data = response.json()
                print(f"[{i+1}/{count}] Registered Ticket: {data['ticket_id']} | Category: {data['category']}")
            else:
                print(f"Error simulating call: {response.text}")
        except Exception as e:
            print(f"Connection failed: {e}")
            
        time.sleep(0.5) # Throttle for simulation effect

if __name__ == "__main__":
    # Ensure server is running before executing this
    simulate_calls(50)
