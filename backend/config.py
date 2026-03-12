from pydantic_settings import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    PROJECT_NAME: str = "PALLAVI AI Calling Agent"
    VERSION: str = "3.0.0"
    API_V1_STR: str = "/api/v1"
    
    POSTGRES_SERVER: str = "localhost"
    POSTGRES_USER: str = "admin"
    POSTGRES_PASSWORD: str = "password"
    POSTGRES_DB: str = "pallavi_db"
    DATABASE_URL: Optional[str] = None

    @property
    def get_database_url(self) -> str:
        if self.DATABASE_URL:
            return self.DATABASE_URL
        return f"postgresql://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_SERVER}/{self.POSTGRES_DB}"

    REDIS_URL: str = "redis://localhost:6379/0"
    
    SECRET_KEY: str = "DEVELOPMENT_SECRET_KEY_REPLACE_IN_PROD"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8
    
    # Twilio Simulation
    TWILIO_ACCOUNT_SID: Optional[str] = "AC_SIMULATED"
    TWILIO_AUTH_TOKEN: Optional[str] = "TOKEN_SIMULATED"
    
    # SLA Settings
    HIGH_PRIORITY_SLA_HOURS: int = 4
    MEDIUM_PRIORITY_SLA_HOURS: int = 24
    LOW_PRIORITY_SLA_HOURS: int = 72

    class Config:
        env_file = ".env"
        case_sensitive = True

settings = Settings()
