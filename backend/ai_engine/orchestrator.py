from typing import Dict, Any
from loguru import logger
import uuid

# Import engine modules
from backend.ai_engine.language_detection.detector import language_detector
from backend.ai_engine.complaint_classifier.classifier import complaint_classifier
from backend.ai_engine.embeddings.generator import embedding_gen
from backend.ai_engine.response_generation.generator import response_generator
from backend.ai_engine.conversation_memory.manager import conversation_memory

class AIEngineOrchestrator:
    """
    The central intelligence hub of the PALLAVI platform.
    Orchestrates the full pipeline from raw text to cognitive understanding and response.
    """
    
    def __init__(self):
        logger.info("PALLAVI AI Engine Orchestrator initialized.")

    def process_utterance(self, session_id: str, text: str) -> Dict[str, Any]:
        """
        Comprehensive processing pipeline:
        1. Context Loading
        2. Language Detection
        3. Semantic Embedding
        4. Grievance Classification
        5. Response Synthesis
        6. Memory Persistence
        """
        logger.info(f"Processing utterance for session: {session_id}")
        
        # 1. Update Memory
        conversation_memory.add_interaction(session_id, "CITIZEN", text)
        context_str = conversation_memory.get_context(session_id)
        
        # 2. Language Detection
        lang_res = language_detector.detect(text)
        language = lang_res["language"]
        
        # 3. Embedding (for semantic search simulation)
        vector = embedding_gen.generate(text)
        
        # 4. Classification
        classification = complaint_classifier.classify(text)
        
        # 5. Response Generation
        ai_response = response_generator.generate_response(
            intent="GRIEVANCE_REGISTRATION",
            language=language,
            context={
                "category": classification["category"],
                "ticket_id": context_str.split("\n")[0][:10] # Mock ticket id retrieval from context
            }
        )
        
        # 6. Save AI Response to Memory
        conversation_memory.add_interaction(session_id, "AI", ai_response)
        
        return {
            "session_id": session_id,
            "language": language,
            "classification": classification,
            "ai_response": ai_response,
            "vector_preview": vector[:5], # Just first 5 dims
            "confidence": classification["confidence"]
        }

    def generate_final_closing(self, session_id: str, language: str) -> str:
        return response_generator.generate_closing(language)

ai_orchestrator = AIEngineOrchestrator()
