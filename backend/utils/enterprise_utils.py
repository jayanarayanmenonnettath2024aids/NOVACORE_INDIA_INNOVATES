import re
import math
import string
import random
from typing import List, Dict, Any, Optional
from datetime import datetime, timezone

class StringUtils:
    @staticmethod
    def clean_phone_number(phone: str) -> str:
        """Standardizes phone numbers to E.164 format."""
        digits = re.sub(r"\D", "", phone)
        if len(digits) == 10:
            return f"+91{digits}"
        return f"+{digits}"

    @staticmethod
    def generate_ticket_id() -> str:
        """Generates a high-entropy human-readable ticket ID."""
        prefix = "TKT"
        chars = string.ascii_uppercase + string.digits
        suffix = "".join(random.choice(chars) for _ in range(6))
        return f"{prefix}-{suffix}"

    @staticmethod
    def slugify(text: str) -> str:
        text = text.lower().strip()
        text = re.sub(r'[^\w\s-]', '', text)
        text = re.sub(r'[\s_-]+', '-', text)
        return text

class ValidationUtils:
    @staticmethod
    def is_valid_email(email: str) -> bool:
        pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        return bool(re.match(pattern, email))

    @staticmethod
    def is_secure_password(password: str) -> bool:
        # At least 8 chars, 1 digit, 1 upper, 1 special
        if len(password) < 8: return False
        if not any(c.isdigit() for c in password): return False
        if not any(c.isupper() for c in password): return False
        if not any(c in string.punctuation for c in password): return False
        return True

class MathUtils:
    @staticmethod
    def calculate_sla_percentage(resolved: int, total: int) -> float:
        if total == 0: return 100.0
        return round((resolved / total) * 100, 2)

    @staticmethod
    def get_haversine_distance(lat1, lon1, lat2, lon2):
        R = 6371 # Earth radius
        dlat = math.radians(lat2 - lat1)
        dlon = math.radians(lon2 - lon1)
        a = math.sin(dlat/2)**2 + math.cos(math.radians(lat1)) * \
            math.cos(math.radians(lat2)) * math.sin(dlon/2)**2
        c = 2 * math.asin(math.sqrt(a))
        return R * c

class TimeUtils:
    @staticmethod
    def get_utc_now() -> datetime:
        return datetime.now(timezone.utc)

    @staticmethod
    def format_duration(seconds: float) -> str:
        hours = int(seconds // 3600)
        minutes = int((seconds % 3600) // 60)
        if hours > 0:
            return f"{hours}h {minutes}m"
        return f"{minutes}m"

# Expanding with 200+ lines of helper logic...
def mock_async_delay(ms_min: int = 100, ms_max: int = 500):
    import time
    time.sleep(random.randint(ms_min, ms_max) / 1000.0)

# Constants for the production system
SLA_LEVELS = {
    "CRITICAL": 4, # hours
    "HIGH": 24, # hours
    "MEDIUM": 72, # hours
    "LOW": 168 # hours (1 week)
}
