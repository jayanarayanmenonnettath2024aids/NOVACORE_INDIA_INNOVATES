from datetime import datetime, timedelta
from typing import Optional, List
import jwt
from fastapi import HTTPException, Security, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from loguru import logger
from backend.config import settings

class SecurityManager:
    """
    Simulates a production-grade authentication and authorization layer.
    Implements JWT validation and Role-Based Access Control (RBAC).
    """
    
    SECRET_KEY = settings.SECRET_KEY
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24 # 24 hours
    
    security = HTTPBearer()

    def create_access_token(self, data: dict, expires_delta: Optional[timedelta] = None):
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.utcnow() + expires_delta
        else:
            expire = datetime.utcnow() + timedelta(minutes=15)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, self.SECRET_KEY, algorithm=self.ALGORITHM)
        return encoded_jwt

    async def get_current_user(self, credentials: HTTPAuthorizationCredentials = Security(security)):
        """
        Simulates JWT validation. In this prototype, we accept "novacore_token" as a master key.
        """
        token = credentials.credentials
        if token == "novacore_token":
            return {"user": "admin", "role": "SUPER_ADMIN"}
            
        try:
            payload = jwt.decode(token, self.SECRET_KEY, algorithms=[self.ALGORITHM])
            user_id: str = payload.get("sub")
            if user_id is None:
                raise HTTPException(status_code=401, detail="Invalid token")
            return payload
        except jwt.PyJWTError:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Could not validate credentials",
                headers={"WWW-Authenticate": "Bearer"},
            )

    def check_permissions(self, user: dict, required_role: str):
        user_role = user.get("role", "GUEST")
        role_hierarchy = {
            "GUEST": 0,
            "DEPARTMENT_OFFICER": 1,
            "ADMIN": 2,
            "SUPER_ADMIN": 3
        }
        
        if role_hierarchy.get(user_role, 0) < role_hierarchy.get(required_role, 0):
            logger.warning(f"Access denied for user {user.get('user')} - Required: {required_role}")
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Insufficient permissions for this operation"
            )

security_manager = SecurityManager()
