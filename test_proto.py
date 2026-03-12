import requests
import time
import subprocess
import sys
import os

def test_prototype():
    # Start the server
    server_process = subprocess.Popen(
        [sys.executable, "-m", "uvicorn", "backend.main:app", "--host", "127.0.0.1", "--port", "8000"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    
    print("Waiting for server to start...")
    time.sleep(3)
    
    try:
        # Test 1: Emergency Road Issue (High Priority)
        print("\n--- Test 1: High Priority Road Issue ---")
        payload = {
            "speech": "There is a broken traffic signal and an accident near Downtown",
            "citizen_id": "CIT-001",
            "location": "Downtown Intersection"
        }
        res = requests.post("http://127.0.0.1:8000/incoming-call", json=payload).json()
        print("Response:", res)
        ticket_id = res["ticket_id"]
        
        # Test 2: Water Leakage (Medium Priority)
        print("\n--- Test 2: Medium Priority Water Issue ---")
        payload = {
            "speech": "There is a water leakage in my street",
            "citizen_id": "CIT-002",
            "location": "North Suburb"
        }
        res = requests.post("http://127.0.0.1:8000/incoming-call", json=payload).json()
        print("Response:", res)

        # Test 3: Trigger Outbound Call
        print("\n--- Test 3: Trigger Outbound Call ---")
        payload = {"ticket_id": ticket_id, "reason": "SLA Update"}
        res = requests.post("http://127.0.0.1:8000/trigger-outbound", json=payload).json()
        print("Response:", res)
        
        # Test 4: Dashboard Stats
        print("\n--- Test 4: Dashboard Verification ---")
        # Start dashboard server briefly or just call it if we can
        dash_process = subprocess.Popen(
            [sys.executable, "-m", "uvicorn", "dashboard.server:app", "--host", "127.0.0.1", "--port", "8001"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        time.sleep(2)
        res = requests.get("http://127.0.0.1:8001/dashboard").json()
        print("Dashboard Analytics:", res)
        dash_process.terminate()

    finally:
        server_process.terminate()
        print("\nServers terminated.")

if __name__ == "__main__":
    test_prototype()
