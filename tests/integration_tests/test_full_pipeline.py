import pytest
from fastapi.testclient import TestClient
from backend.main import app
from backend.database.session import get_db
from sqlalchemy import create_all

client = TestClient(app)

def test_root_endpoint():
    response = client.get("/")
    assert response.status_code == 200
    assert "PALLAVI AI" in response.json()["message"]

def test_telephony_inbound_simulation():
    payload = {
        "phone_number": "+919999999999",
        "speech_text": "Greetings, I am calling to report a water leak in Sector 4."
    }
    response = client.post("/api/v1/telephony/inbound", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "ticket_id" in data
    assert "voice_response" in data
    assert data["category"] == "Water" # Based on our engine logic

def test_monitoring_endpoints():
    # Test Health
    response = client.get("/api/v1/monitoring/health")
    assert response.status_code == 200
    assert "cpu_percent" in response.json()

    # Test Telemetry
    response = client.get("/api/v1/monitoring/telemetry")
    assert response.status_code == 200
    assert "current_load" in response.json()

def test_citizen_api():
    # Identifying the citizen created in previous test
    response = client.get("/api/v1/citizens/phone/%2B919999999999")
    assert response.status_code == 200
    assert response.json()["phone_number"] == "+919999999999"

def test_department_listing():
    response = client.get("/api/v1/departments/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
