from datetime import datetime

from pydantic import BaseModel

from app.schemas.user import UserRole


# ---------------------------------------------------------
# User
# ---------------------------------------------------------

class DashboardUser(BaseModel):
    id: int
    full_name: str
    email: str
    role: UserRole


# ---------------------------------------------------------
# Profile
# ---------------------------------------------------------

class DashboardProfile(BaseModel):
    exists: bool
    profile_completion: int
    profile_photo: str | None = None
    resume_url: str | None = None


# ---------------------------------------------------------
# Career Recommendation
# ---------------------------------------------------------

class DashboardCareer(BaseModel):
    available: bool = False

    recommended_role: str | None = None

    confidence: int | None = None

    strengths: list[str] = []

    skill_gaps: list[str] = []

    learning_path: list[str] = []



# ---------------------------------------------------------
# Dashboard Sections
# ---------------------------------------------------------

class DashboardSection(BaseModel):
    key: str
    title: str
    available: bool



# ---------------------------------------------------------
# Individual Assessment Summary
# ---------------------------------------------------------

class DashboardAssessmentItem(BaseModel):
    completed: bool
    score: int | None = None
    correct_answers: int | None = None
    total_questions: int | None = None
    attempt_id: int | None = None
    completed_at: datetime | None = None



# ---------------------------------------------------------
# Assessment Summary
# ---------------------------------------------------------

class DashboardAssessment(BaseModel):
    available: bool
    total_completed: int

    aptitude: DashboardAssessmentItem
    coding: DashboardAssessmentItem



# ---------------------------------------------------------
# Dashboard Response
# ---------------------------------------------------------

class DashboardResponse(BaseModel):

    dashboard_type: UserRole

    user: DashboardUser

    profile: DashboardProfile

    assessment: DashboardAssessment

    career: DashboardCareer

    sections: list[DashboardSection]