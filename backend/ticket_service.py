import uuid
import json
import os
from datetime import datetime

DB_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "tickets.json")

def load_tickets():
    if not os.path.exists(DB_PATH):
        return []
    try:
        with open(DB_PATH, "r") as f:
            return json.load(f)
    except:
        return []

def save_tickets(tickets):
    with open(DB_PATH, "w") as f:
        json.dump(tickets, f, indent=4)

def create_ticket(data, citizen_id="CIT-123", location="Unknown"):
    tickets = load_tickets()

    ticket = {
        "ticket_id": str(uuid.uuid4())[:8].upper(),
        "citizen_id": citizen_id,
        "complaint_text": data["text"],
        "category": data["category"],
        "priority": data["priority"],
        "language": data["language"],
        "location": location,
        "status": "Received",
        "department": "Pending Assignment",
        "created_at": datetime.now().isoformat(),
        "resolved_at": None
    }

    tickets.append(ticket)
    save_tickets(tickets)

    return ticket

def update_ticket_status(ticket_id, new_status, department=None):
    tickets = load_tickets()
    for t in tickets:
        if t["ticket_id"] == ticket_id:
            t["status"] = new_status
            if department:
                t["department"] = department
            if new_status == "Resolved":
                t["resolved_at"] = datetime.now().isoformat()
            break
    save_tickets(tickets)
