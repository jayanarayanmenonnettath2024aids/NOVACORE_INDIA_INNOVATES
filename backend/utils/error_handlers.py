from fastapi import Request, HTTPException, status
from fastapi.responses import JSONResponse
from loguru import logger
import traceback
from typing import Union

class PALLAVIException(Exception):
    def __init__(self, name: str, detail: str, status_code: int = 500):
        self.name = name
        self.detail = detail
        self.status_code = status_code

async def global_exception_handler(request: Request, exc: Exception):
    """
    Catch-all handler for any unhandled exceptions in the platform.
    Logs full stack trace and returns a standardized error response.
    """
    logger.critical(f"GLOBAL_ERROR | Request: {request.method} {request.url}")
    logger.error(f"Traceback: {traceback.format_exc()}")
    
    return JSONResponse(
        status_code=500,
        content={
            "error": "INTERNAL_SERVER_ERROR",
            "message": "An unexpected error occurred in the PALLAVI governance engine.",
            "trace_id": str(uuid.uuid4()) # Production ID for log correlation
        }
    )

async def pallavi_exception_handler(request: Request, exc: PALLAVIException):
    """
    Custom handler for domain-specific PALLAVI errors.
    """
    logger.warning(f"DOMAIN_ERROR | {exc.name}: {exc.detail}")
    return JSONResponse(
        status_code=exc.status_code,
        content={"error": exc.name, "message": exc.detail}
    )

def setup_exception_handlers(app):
    app.add_exception_handler(Exception, global_exception_handler)
    app.add_exception_handler(PALLAVIException, pallavi_exception_handler)

import uuid # Fix for missing import
