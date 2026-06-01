"""
FastAPI application entry point
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .admin import setup_admin
from .core.config import settings
from .routes import health

app = FastAPI(
    title="supply-chain-scenario-rag API",
    description="Supply chain scenario dashboard with RAG chat on OpenShift AI",
    version="0.0.0",
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_HOSTS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(health.router, prefix="/health", tags=["health"])

# Setup SQLAdmin dashboard at /admin
setup_admin(app)

@app.get("/")
async def root() -> dict[str, str]:
    """Root endpoint"""
    return {"message": "Welcome to supply-chain-scenario-rag API"}
