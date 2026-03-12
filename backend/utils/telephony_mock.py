from typing import Dict, Any, List
import random
import time
from loguru import logger

class TelephonyMock:
    """
    Highly detailed mock for telephony provider interactions (e.g. Twilio, Vonage).
    Simulates call signals, media buffering, and websocket stream connectivity.
    """
    def __init__(self):
        self.active_calls: Dict[str, Dict[str, Any]] = {}

    def simulate_incoming_webhook(self, from_phone: str, to_phone: str) -> str:
        """
        Simulates the arrival of a POST request from a telephony carrier.
        """
        call_sid = f"CA{uuid.uuid4().hex}"
        self.active_calls[call_sid] = {
            "from": from_phone,
            "to": to_phone,
            "start_time": time.time(),
            "status": "ringing",
            "media_buffer": []
        }
        logger.info(f"TelephonyMock: Incoming Call {call_sid} from {from_phone}")
        return call_sid

    def mock_speech_streaming(self, call_sid: str, chunks: List[str]):
        """
        Simulates the transmission of real-time speech chunks via a websocket.
        """
        if call_sid not in self.active_calls:
            return
            
        logger.debug(f"TelephonyMock: Streaming {len(chunks)} audio chunks for {call_sid}")
        for chunk in chunks:
            self.active_calls[call_sid]["media_buffer"].append(chunk)
            # Simulated network jitter
            time.sleep(0.05)

    def terminate_call(self, call_sid: str):
        if call_sid in self.active_calls:
            self.active_calls[call_sid]["status"] = "completed"
            logger.info(f"TelephonyMock: Call {call_sid} terminated.")

import uuid # Fix for missing import
telephony_mock = TelephonyMock()
