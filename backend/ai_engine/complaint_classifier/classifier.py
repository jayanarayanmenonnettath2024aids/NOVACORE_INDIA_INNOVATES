from typing import Dict, Any, List
import random
from loguru import logger
from backend.models.all_models import Priority
from backend.utils.knowledge_base import GRIEVANCE_KNOWLEDGE_BASE

class ComplaintClassifier:
    """
    Simulates a fine-tuned Transformer model for multi-label grievance classification.
    """
    def __init__(self, model_path: str):
        self.model_path = model_path
        self.categories = list(GRIEVANCE_KNOWLEDGE_BASE.keys())
        logger.info(f"ComplaintClassifier loaded from {model_path}")

    def classify(self, text: str) -> Dict[str, Any]:
        """
        Classifies the complaint into category, sub-category, and priority.
        """
        text_lower = text.lower()
        
        detected_category = "General"
        detected_sub = "Miscellaneous"
        priority = Priority.MEDIUM
        
        # 1. Category Detection using Knowledge Base logic
        for cat, details in GRIEVANCE_KNOWLEDGE_BASE.items():
            # Simulated semantic search
            if any(k.lower() in text_lower for k in [cat] + details.get("sub_categories", [])):
                detected_category = cat
                # Randomly pick a sub-category from the KB if not explicitly found
                subs = details.get("sub_categories", [])
                detected_sub = random.choice(subs) if subs else "General"
                
                # Check priority rules
                rules = details.get("priority_rules", {})
                priority_str = rules.get(detected_sub, "Medium")
                priority = getattr(Priority, priority_str.upper(), Priority.MEDIUM)
                break
                
        # 2. Urgency Signal Overrides
        emergency_signals = ["immediate", "danger", "dying", "accident", "fire", "shock", "burst"]
        if any(s in text_lower for s in emergency_signals):
            priority = Priority.CRITICAL
            
        # 3. Model Confidence Simulation
        confidence = random.uniform(0.75, 0.98)
        
        return {
            "category": detected_category,
            "sub_category": detected_sub,
            "priority": priority,
            "confidence": confidence,
            "entities": self._extract_entities(text),
            "summary": f"Citizen reporting {detected_sub} under {detected_category}. Priority {priority.value}."
        }

    def _extract_entities(self, text: str) -> List[Dict[str, str]]:
        """Simulates NER for locations and names."""
        # Simple simulation for 10k LOC project
        entities = []
        locations = ["Sector 4", "Main Square", "MG Road", "Airport Area", "West Layout"]
        for loc in locations:
            if loc.lower() in text.lower():
                entities.append({"type": "LOCATION", "value": loc})
        return entities

complaint_classifier = ComplaintClassifier("assets/models/complaint_classifier.bin")
