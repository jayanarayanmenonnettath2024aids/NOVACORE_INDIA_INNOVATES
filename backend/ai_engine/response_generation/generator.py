from typing import Dict, Any, List
from loguru import logger
import random

class ResponseGenerator:
    """
    Simulates a generative AI response system (e.g. GPT-4 or fine-tuned Llama-3).
    Customized for government grievance handling across multiple Indian languages.
    """
    def __init__(self, model_path: str):
        self.model_path = model_path
        logger.info(f"ResponseGenerator initialized from {model_path}")
        
        self.templates = {
            "en": {
                "greeting": ["Hello, welcome to PALLAVI AI Support.", "Greetings, how can I assist you today?"],
                "confirmation": "Your complaint regarding {category} has been registered successfully. Your Ticket ID is {ticket_id}.",
                "status_update": "Your ticket {ticket_id} is currently in state: {status}.",
                "closing": ["Thank you for calling. We are here to help.", "Goodbye. Your issue is our priority."]
            },
            "hi": {
                "greeting": ["नमस्ते, पल्लवी एआई सहायता में आपका स्वागत है।", "नमसकार, मैं आपकी कैसे मदद कर सकता हूँ?"],
                "confirmation": "{category} के संबंध में आपकी शिकायत सफलतापूर्वक दर्ज कर ली गई है। आपका टिकट आईडी {ticket_id} है।",
                "status_update": "आपका टिकट {ticket_id} वर्तमान में {status} स्थिति में है।",
                "closing": ["फोन करने के लिए धन्यवाद। हम आपकी मदद के लिए यहाँ हैं।", "नमस्ते। आपकी समस्या हमारी प्राथमिकता है।"]
            },
            "ta": {
                "greeting": ["வணக்கம், பல்லவி AI ஆதரவிற்கு வரவேற்கிறோம்.", "வணக்கம், இன்று நான் உங்களுக்கு எவ்வாறு உதவ முடியும்?"],
                "confirmation": "{category} தொடர்பான உங்கள் புகார் வெற்றிகரமாக பதிவு செய்யப்பட்டது. உங்கள் டிக்கெட் ஐடி {ticket_id} ஆகும்.",
                "status_update": "உங்கள் டிக்கெட் {ticket_id} தற்போது {status} நிலையில் உள்ளது.",
                "closing": ["அழைத்ததற்கு நன்றி. நாங்கள் உங்களுக்கு உதவ இங்கே இருக்கிறோம்.", "வணக்கம். உங்கள் பிரச்சனை எங்களது முன்னுரிமை."]
            }
        }

    def generate_response(
        self, 
        intent: str, 
        language: str, 
        context: Dict[str, Any]
    ) -> str:
        """
        Generates a contextual response based on intent and language.
        """
        lang = language if language in self.templates else "en"
        tmpl_set = self.templates[lang]
        
        if intent == "GRIEVANCE_REGISTRATION":
            base = tmpl_set["confirmation"]
            return base.format(
                category=context.get("category", "General"),
                ticket_id=context.get("ticket_id", "TKT-PENDING")
            )
        elif intent == "STATUS_CHECK":
            base = tmpl_set["status_update"]
            return base.format(
                ticket_id=context.get("ticket_id", "Unknown"),
                status=context.get("status", "Received")
            )
        else:
            # Random greeting + generic help for unknown intents
            return random.choice(tmpl_set["greeting"]) + " Please state your grievance clearly."

    def generate_closing(self, language: str) -> str:
        lang = language if language in self.templates else "en"
        return random.choice(self.templates[lang]["closing"])

response_generator = ResponseGenerator("assets/models/response_model.bin")
