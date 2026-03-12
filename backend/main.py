from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.config import settings
from backend.api.v1.endpoints import tickets, telephony, analytics, citizens, departments, monitoring, admin
from backend.database.session import engine
from backend.models import all_models
from backend.middleware.standard_middleware import LoggingMiddleware, SecurityMiddleware
from backend.utils.logging_config import setup_logging
from backend.utils.error_handlers import setup_exception_handlers
from loguru import logger

# Initialize Logging
setup_logging()

# Initialize DB Tables
all_models.Base.metadata.create_all(bind=engine)
logger.info("Database tables initialized.")

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
    description="PALLAVI AI: Production-Scale Digital Governance Platform"
)

# Exception Handlers
setup_exception_handlers(app)

# Set up Standard Middleware
app.add_middleware(LoggingMiddleware)
app.add_middleware(SecurityMiddleware)

# Set up CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include Routers
app.include_router(tickets.router, prefix=f"{settings.API_V1_STR}/tickets", tags=["Tickets"])
app.include_router(telephony.router, prefix=f"{settings.API_V1_STR}/telephony", tags=["Telephony"])
app.include_router(analytics.router, prefix=f"{settings.API_V1_STR}/analytics", tags=["Analytics"])
app.include_router(citizens.router, prefix=f"{settings.API_V1_STR}/citizens", tags=["Citizens"])
app.include_router(departments.router, prefix=f"{settings.API_V1_STR}/departments", tags=["Departments"])
app.include_router(monitoring.router, prefix=f"{settings.API_V1_STR}/monitoring", tags=["Monitoring"])
app.include_router(admin.router, prefix=f"{settings.API_V1_STR}/admin", tags=["Administrator"])

@app.get("/")
def root():
    return {
        "message": "Welcome to PALLAVI AI Calling Agent Platform",
        "version": settings.VERSION,
        "docs": "/docs"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
