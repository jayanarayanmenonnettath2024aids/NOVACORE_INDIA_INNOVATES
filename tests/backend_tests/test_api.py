from fastapi.testclient import TestClient
from backend.main import app
from backend.database.session import Base, engine
import pytest

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert "PALLAVI AI" in response.json()["message"]

def test_create_inbound_call():
    payload = {
        "phone_number": "+919000012345",
        "speech_text": "There is a massive water leakage on the main MG Road intersection. Please send someone immediately."
    }
    response = client.post("/api/v1/telephony/inbound", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "ticket_id" in data
    assert data["category"] == "Water"
    assert "voice_response" in data

def test_dashboard_analytics():
    response = client.get("/api/v1/analytics/dashboard")
    assert response.status_code == 200
    data = response.json()
    assert "total_calls_24h" in data
    assert "overall_health" in data

def test_ticket_retrieval():
    # List tickets first to get a valid ID
    list_res = client.get("/api/v1/tickets/")
    if list_res.status_code == 200 and len(list_res.json()) > 0:
        ticket_id = list_res.json()[0]["ticket_id"]
        res = client.get(f"/api/v1/tickets/{ticket_id}")
        assert res.status_code == 200
        assert res.json()["ticket_id"] == ticket_id
