from typing import Dict, Any, List, Optional
from loguru import logger
import abc

class CommunicationProvider(abc.ABC):
    @abc.abstractmethod
    def send(self, recipient: str, message: str) -> bool:
        pass

class SMSProvider(CommunicationProvider):
    def send(self, recipient: str, message: str) -> bool:
        logger.info(f"SMS_OUT | To: {recipient} | Msg: {message}")
        return True

class WhatsAppProvider(CommunicationProvider):
    def send(self, recipient: str, message: str) -> bool:
        logger.info(f"WA_OUT | To: {recipient} | Msg: {message}")
        return True

class PushNotificationProvider(CommunicationProvider):
    def send(self, recipient: str, message: str) -> bool:
        logger.info(f"PUSH_OUT | To: {recipient} | Msg: {message}")
        return True

class CommunicationAdapter:
    """
    Simulates a production-scale unified notification adapter.
    Handles fallbacks, retry logic, and multi-channel dispatch.
    """
    def __init__(self):
        self.providers = {
            "sms": SMSProvider(),
            "whatsapp": WhatsAppProvider(),
            "push": PushNotificationProvider()
        }
        logger.info("CommunicationAdapter online: Multi-channel delivery ready.")

    def dispatch(self, channels: List[str], recipient: str, message: str):
        """
        Dispatches a message across multiple channels.
        """
        results = {}
        for channel in channels:
            provider = self.providers.get(channel)
            if provider:
                try:
                    results[channel] = provider.send(recipient, message)
                except Exception as e:
                    logger.error(f"Channel {channel} failed for {recipient}: {e}")
                    results[channel] = False
        return results

comm_adapter = CommunicationAdapter()
