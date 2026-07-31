from contextlib import asynccontextmanager
from pathlib import Path

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

# Import models so SQLAlchemy registers all mappings
import app.models  # noqa: F401

# Import API routers
from app.api.auth import router as auth_router
from app.api.profile import router as profile_router
from app.api.dashboard import router as dashboard_router
from app.api.assessment import router as assessment_router


# ---------------------------------------------------------
# Application Lifespan
# ---------------------------------------------------------

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("🚀 TalentSphere Backend Started")
    yield
    print("🛑 TalentSphere Backend Stopped")


# ---------------------------------------------------------
# FastAPI Application
# ---------------------------------------------------------

app = FastAPI(
    title="TalentSphere API",
    description="Backend API for TalentSphere Career Development Platform",
    version="1.0.0",
    lifespan=lifespan,
)

# ---------------------------------------------------------
# CORS Configuration
# ---------------------------------------------------------

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------------------------------------------------------
# Upload Directory
# ---------------------------------------------------------

UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

# ---------------------------------------------------------
# Static Files
# ---------------------------------------------------------

app.mount(
    "/uploads",
    StaticFiles(directory=str(UPLOAD_DIR)),
    name="uploads",
)

# ---------------------------------------------------------
# Register API Routers
# ---------------------------------------------------------

app.include_router(
    auth_router,
    tags=["Authentication"],
)

app.include_router(
    profile_router,
    tags=["Profile"],
)

app.include_router(
    dashboard_router,
    tags=["Dashboard"],
)

app.include_router(
    assessment_router,
    tags=["Assessment"],
)

# ---------------------------------------------------------
# Root Endpoint
# ---------------------------------------------------------

@app.get("/", tags=["System"])
def root():
    return {
        "status": "success",
        "message": "TalentSphere Backend Running Successfully 🚀",
        "version": "1.0.0",
    }


# ---------------------------------------------------------
# Health Check
# ---------------------------------------------------------

@app.get("/health", tags=["System"])
def health():
    return {
        "status": "healthy",
        "service": "TalentSphere API",
        "version": "1.0.0",
    }