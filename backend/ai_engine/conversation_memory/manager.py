from typing import List, Dict, Any, Optional
from loguru import logger
import json

class ConversationMemory:
    """
    Simulates a session-based conversation memory with vector recall logic.
    Supports multi-turn interactions for citizen helpline calls.
    """
    def __init__(self, max_history: int = 10):
        self.sessions: Dict[str, List[Dict[str, str]]] = {}
        self.max_history = max_history
        logger.info(f"ConversationMemory manager initialized (Max History: {max_history})")

    def add_interaction(self, session_id: str, role: str, content: str):
        """
        Adds a new interaction (User/AI) to the session history.
        """
        if session_id not in self.sessions:
            self.sessions[session_id] = []
            
        self.sessions[session_id].append({
            "role": role,
            "content": content,
            "timestamp": "now" # In real app, use datetime
        })
        
        # Trim history
        if len(self.sessions[session_id]) > self.max_history:
            self.sessions[session_id] = self.sessions[session_id][-self.max_history:]
            
        logger.debug(f"Memory updated for {session_id}. History depth: {len(self.sessions[session_id])}")

    def get_context(self, session_id: str) -> str:
        """
        Flattens the history into a context string for the AI reasoning engine.
        """
        history = self.sessions.get(session_id, [])
        return "\n".join([f"{h['role']}: {h['content']}" for h in history])

    def clear_session(self, session_id: str):
        if session_id in self.sessions:
            del self.sessions[session_id]
            logger.info(f"Session memory cleared: {session_id}")

conversation_memory = ConversationMemory()
