from typing import Dict, Any
from backend.ai_engine.orchestrator import ai_orchestrator
from backend.models.all_models import Priority

class AIService:
    @staticmethod
    def detect_language(text: str) -> str:
        """Uses the orchestrated language detector."""
        res = ai_orchestrator.process_utterance("system-check", text)
        return res["language"]

    @staticmethod
    def classify_complaint(text: str) -> Dict[str, Any]:
        """Uses the orchestrated classifier and return standard structure."""
        res = ai_orchestrator.process_utterance("classification-task", text)
        
        # Mapping orchestrated results back to the service interface
        return {
            "category": res["classification"]["category"],
            "sub_category": res["classification"]["sub_category"],
            "priority": res["classification"]["priority"],
            "language": res["language"],
            "summary": res["classification"]["summary"],
            "confidence": res["confidence"]
        }

    @staticmethod
    def generate_response(ticket_id: str, language: str, category: str = "General") -> str:
        """Uses the generative response engine."""
        # Note: In a real flow, the orchestrator would have already generated this.
        # This wrapper maintains compatibility with existing service calls.
        return ai_orchestrator.generate_final_closing(ticket_id, language)

ai_service = AIService()
