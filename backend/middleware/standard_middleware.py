from fastapi import Request, HTTPException
from loguru import logger
import time
from starlette.middleware.base import BaseHTTPMiddleware

class LoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        start_time = time.time()
        
        # Log request info
        client_host = request.client.host if request.client else "unknown"
        logger.info(f"Incoming {request.method} {request.url.path} from {client_host}")
        
        try:
            response = await call_next(request)
            
            process_time = time.time() - start_time
            response.headers["X-Process-Time"] = str(process_time)
            
            logger.info(f"Completed {request.method} {request.url.path} in {process_time:.4f}s - Status: {response.status_code}")
            return response
            
        except Exception as e:
            logger.exception(f"Request failed: {request.method} {request.url.path} - Error: {str(e)}")
            raise

class SecurityMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        # Basic security headers
        response = await call_next(request)
        response.headers["X-Content-Type-Options"] = "nosniff"
        response.headers["X-Frame-Options"] = "DENY"
        response.headers["X-XSS-Protection"] = "1; mode=block"
        response.headers["Strict-Transport-Security"] = "max-age=31536000; includeSubDomains"
        return response
