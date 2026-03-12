from fastapi import FastAPI
import sys
import os

# Ensure backend can be imported
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from backend.ticket_service import load_tickets

app = FastAPI(title="PALLAVI Admin Dashboard")

@app.get("/dashboard")
def dashboard():
    tickets = load_tickets()
    
    total = len(tickets)
    active = len([t for t in tickets if t["status"] != "Resolved"])
    resolved = len([t for t in tickets if t["status"] == "Resolved"])
    
    # Priority Breakdown
    high_priority = len([t for t in tickets if t["priority"] == "High"])
    
    # Category Distribution
    categories = {}
    for t in tickets:
        cat = t["category"]
        categories[cat] = categories.get(cat, 0) + 1

    return {
        "overview": {
            "total_tickets": total,
            "active_tickets": active,
            "resolved_cases": resolved,
            "high_priority_alerts": high_priority
        },
        "category_breakdown": categories,
        "last_updated": tickets[-1]["created_at"] if tickets else None
    }
