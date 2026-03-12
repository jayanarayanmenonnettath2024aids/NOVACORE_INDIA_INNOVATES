from typing import Dict, Any
import uuid
import time
from backend.services.ai_service import ai_service
from backend.services.ticket_service import ticket_service
from backend.services.citizen_service import citizen_service
from backend.services.routing_service import routing_service
from backend.schemas.all_schemas import TicketCreate, CitizenCreate
from sqlalchemy.orm import Session

class TelephonyService:
    @staticmethod
    def process_inbound_call(db: Session, phone_number: str, speech_text: str) -> Dict[str, Any]:
        """
        Production-grade simulation of an incoming voice conversation with AI session tracking.
        """
        # Generate a unique session ID for this call
        call_session_id = f"SESSION_{uuid.uuid4().hex[:8]}"
        
        # 1. Citizen Identification
        citizen = citizen_service.get_citizen_by_phone(db, phone_number)
        if not citizen:
            citizen_in = CitizenCreate(phone_number=phone_number, full_name="Anonymous Citizen")
            citizen = citizen_service.create_citizen(db, citizen_in)
            
        # 2. AI Understanding (Deep Orchestration)
        ai_result = ai_orchestrator.process_utterance(call_session_id, speech_text)
        analysis = ai_result["classification"]
        
        # 3. Ticket Generation
        ticket_in = TicketCreate(
            complaint_text=speech_text,
            citizen_id=citizen.id,
            category=analysis["category"],
            priority=analysis["priority"],
            language_code=ai_result["language"],
            metadata_json={
                "call_session_id": call_session_id,
                "confidence": ai_result["confidence"],
                "sub_category": analysis["sub_category"]
            }
        )
        ticket = ticket_service.create_ticket(db, ticket_in)
        
        # 4. Auto-Routing
        routing_service.auto_route_ticket(db, ticket.id)
        
        # 5. Multichannel Notification
        from backend.services.notification_service import notification_service
        notification_service.notify_citizen_creation(db, ticket)
        
        return {
            "ticket_id": ticket.ticket_id,
            "category": ticket.category,
            "status": "Registered",
            "voice_response": ai_result["ai_response"]
        }

    @staticmethod
    def trigger_outbound_followup(db: Session, ticket_id_str: str):
        """
        Simulates an automated AI call to confirm resolution.
        """
        ticket = ticket_service.get_ticket(db, ticket_id_str)
        if not ticket:
            return False
            
        print(f"--- [TELEPHONY] Placing Outbound Call to {ticket.citizen.phone_number} ---")
        print(f"AI: 'Hello, your ticket {ticket_id_str} is now resolved. Please provide feedback.'")
        return True

telephony_service = TelephonyService()
