import sys
from loguru import logger
from backend.config import settings

def setup_logging():
    # Remove default handler
    logger.remove()
    
    # Standard format for PALLAVI system
    log_format = (
        "<green>{time:YYYY-MM-DD HH:mm:ss}</green> | "
        "<level>{level: <8}</level> | "
        "<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - "
        "<level>{message}</level>"
    )
    
    # Console handler
    logger.add(sys.stdout, format=log_format, level="INFO")
    
    # File handler for audit logs
    logger.add(
        "logs/pallavi_audit.log", 
        rotation="10 MB", 
        retention="30 days", 
        format=log_format,
        level="DEBUG"
    )
    
    logger.info("Logging system initialized for PALLAVI AI.")

# Initialize immediately
setup_logging()
