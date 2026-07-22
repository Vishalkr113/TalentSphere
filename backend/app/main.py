from fastapi import FastAPI
from app.db.database import Base, engine
from app.models.user import User
from app.api.auth import router as auth_router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="TalentSphere API",
    description="Backend API for TalentSphere Career Development Platform",
    version="1.0.0"
)

app.include_router(auth_router)

@app.get("/")
def root():
    return {
        "status": "success",
        "message": "TalentSphere Backend Running Successfully 🚀"
    }

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }