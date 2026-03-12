from fastapi import APIRouter, Depends, BackgroundTasks
from sqlalchemy.orm import Session
from backend.database.session import get_db
from backend.services.telephony_service import telephony_service
from typing import Dict, Any

router = APIRouter()

@router.post("/inbound")
def handle_inbound_call(
    data: Dict[str, Any], 
    db: Session = Depends(get_db)
):
    phone = data.get("phone_number")
    speech = data.get("speech_text")
    if not phone or not speech:
        return {"error": "Missing phone_number or speech_text"}
        
    return telephony_service.process_inbound_call(db, phone, speech)

@router.post("/outbound/{ticket_id}")
def trigger_outbound_call(
    ticket_id: str, 
    background_tasks: BackgroundTasks,
    db: Session = Depends(get_db)
):
    background_tasks.add_task(telephony_service.trigger_outbound_followup, db, ticket_id)
    return {"status": "Outbound call queued"}
