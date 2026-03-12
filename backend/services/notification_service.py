from sqlalchemy.orm import Session
import json
from datetime import datetime
from backend.models.all_models import NotificationLog, Ticket
from typing import Dict, Any, Optional
from loguru import logger

class NotificationService:
    @staticmethod
    def send_sms(db: Session, ticket_id: int, message: str, phone: str) -> bool:
        """
        Simulates sending an SMS notification.
        In production, this would use MSG91 or Twilio SMS API.
        """
        try:
            logger.info(f"[SMS] Sending notification to {phone}: {message[:50]}...")
            
            # Simulation delay
            # time.sleep(0.1) 
            
            log = NotificationLog(
                ticket_id=ticket_id,
                channel="SMS",
                recipient=phone,
                template_name="complaint_reg",
                status="Sent"
            )
            db.add(log)
            db.commit()
            return True
        except Exception as e:
            logger.error(f"Failed to send SMS: {e}")
            return False

    @staticmethod
    def send_whatsapp(db: Session, ticket_id: int, message: str, phone: str) -> bool:
        """
        Simulates sending a WhatsApp notification.
        """
        try:
            logger.info(f"[WhatsApp] Sending notification to {phone}: {message[:50]}...")
            
            log = NotificationLog(
                ticket_id=ticket_id,
                channel="WhatsApp",
                recipient=phone,
                template_name="complaint_update",
                status="Delivered"
            )
            db.add(log)
            db.commit()
            return True
        except Exception as e:
            logger.error(f"Failed to send WhatsApp: {e}")
            return False

    @staticmethod
    def notify_citizen_creation(db: Session, ticket: Ticket):
        """
        Orchestrates multi-channel notifications for new tickets.
        """
        message = (
            f"PALLAVI AI: Your complaint ({ticket.ticket_id}) has been registered. "
            f"Department: {ticket.department.name if ticket.department else 'Pending'}. "
            f"Status: {ticket.status.value}."
        )
        # Send both for redundancy in production simulation
        NotificationService.send_sms(db, ticket.id, message, ticket.citizen.phone_number)
        NotificationService.send_whatsapp(db, ticket.id, message, ticket.citizen.phone_number)

    @staticmethod
    def notify_status_change(db: Session, ticket: Ticket, old_status: str, new_status: str):
        """
        Notifies citizen when ticket status changes.
        """
        message = f"PALLAVI AI Update: Ticket {ticket.ticket_id} moved from {old_status} to {new_status}."
        NotificationService.send_whatsapp(db, ticket.id, message, ticket.citizen.phone_number)

notification_service = NotificationService()
