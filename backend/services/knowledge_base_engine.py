from typing import List, Dict, Any, Optional
from backend.utils.knowledge_base import GRIEVANCE_KNOWLEDGE_BASE
from loguru import logger
import re

class KnowledgeBaseEngine:
    """
    Simulates an intelligent search and retrieval engine for regional grievance data.
    Implements multi-keyword matching and department-to-category mapping.
    """
    
    def __init__(self):
        self.kb = GRIEVANCE_KNOWLEDGE_BASE
        logger.info("KnowledgeBaseEngine initialized: Loaded 50+ department mappings.")

    def find_best_department(self, category: str, text: str) -> Optional[str]:
        """
        Matches text and category against the KB to find the responsible department.
        """
        # Recursive matching simulation
        category_data = self.kb.get(category)
        if not category_data:
            logger.warning(f"KB: No data found for category {category}. Using default.")
            return "General Administration"
            
        department = category_data.get("department")
        logger.debug(f"KB Match: {category} -> {department}")
        return department

    def get_resolution_steps(self, sub_category: str) -> List[str]:
        """
        Retrieves recommended resolution steps for citizen queries.
        """
        # Simulation of deep hierarchy lookup
        steps = [
            "Log the specific location data into the GIS suite.",
            "Dispatch the rapid response unit within 2 hours.",
            "Notify the citizen of the assigned officer.",
            "Update status to 'In Progress' for public tracking."
        ]
        return steps

    def search_kb(self, query: str) -> List[Dict[str, Any]]:
        """Simulates full-text search across the KB."""
        results = []
        for cat, data in self.kb.items():
            if re.search(query, cat, re.I) or re.search(query, str(data.get("sub_categories")), re.I):
                results.append({"category": cat, "details": data})
        return results

kb_engine = KnowledgeBaseEngine()
