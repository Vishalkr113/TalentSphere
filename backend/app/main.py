from pathlib import Path

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

# Import models so SQLAlchemy can register all mappings
import app.models  # noqa: F401

# Import API routers
from app.api.auth import router as auth_router
from app.api.profile import router as profile_router
from app.api.dashboard import router as dashboard_router
from app.api.assessment import router as assessment_router


# ---------------------------------------------------------
# Application
# ---------------------------------------------------------

app = FastAPI(
    title="TalentSphere API",
    description="Backend API for TalentSphere Career Development Platform",
    version="1.0.0",
)

# ---------------------------------------------------------
# CORS
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

UPLOAD_DIR.mkdir(
    parents=True,
    exist_ok=True,
)

# ---------------------------------------------------------
# Static File Serving
# ---------------------------------------------------------

app.mount(
    "/uploads",
    StaticFiles(directory=str(UPLOAD_DIR)),
    name="uploads",
)

# ---------------------------------------------------------
# API Routers
# ---------------------------------------------------------

app.include_router(auth_router)
app.include_router(profile_router)
app.include_router(dashboard_router)
app.include_router(assessment_router)

# ---------------------------------------------------------
# Basic Routes
# ---------------------------------------------------------

@app.get("/")
def root():
    return {
        "status": "success",
        "message": "TalentSphere Backend Running Successfully ðŸš€",
    }

@app.get("/health")
def health():
    return {
        "status": "healthy",
    }
