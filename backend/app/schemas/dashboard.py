from datetime import datetime
from pydantic import BaseModel, Field
from app.schemas.user import UserRole


class DashboardUser(BaseModel):
    id: int
    full_name: str
    email: str
    role: UserRole


class DashboardProfile(BaseModel):
    exists: bool
    profile_completion: int
    profile_photo: str | None = None
    resume_url: str | None = None
    student_class: str | None = None
    stream: str | None = None
    board: str | None = None
    school_name: str | None = None
    college_name: str | None = None
    course: str | None = None
    branch: str | None = None
    semester: str | None = None
    cgpa: str | None = None
    company_name: str | None = None
    job_title: str | None = None
    target_role: str | None = None
    skills: list[str] = Field(default_factory=list)


class DashboardCareer(BaseModel):
    available: bool = False
    recommended_role: str | None = None
    confidence: float | None = None
    strengths: list[str] = Field(default_factory=list)
    skill_gaps: list[str] = Field(default_factory=list)
    learning_path: list[str] = Field(default_factory=list)


class DashboardProgress(BaseModel):
    resume: int
    assessment: int
    coding: int
    placement: int


class DashboardSection(BaseModel):
    key: str
    title: str
    available: bool


class DashboardAssessmentItem(BaseModel):
    completed: bool
    score: float | None = None
    percentage: float | None = None
    grade: str | None = None
    correct_answers: int | None = None
    total_questions: int | None = None
    attempt_id: int | None = None
    completed_at: datetime | None = None
    assessment_type: str | None = None


class DashboardAssessment(BaseModel):
    available: bool
    total_completed: int
    latest_score: float | None = None
    latest_grade: str | None = None
    latest_assessment: str | None = None
    latest_completed_at: datetime | None = None
    aptitude: DashboardAssessmentItem
    coding: DashboardAssessmentItem
    professional: DashboardAssessmentItem
    high_school: DashboardAssessmentItem
    recent_attempts: list[DashboardAssessmentItem] = Field(default_factory=list)


class DashboardResponse(BaseModel):
    dashboard_type: UserRole
    user: DashboardUser
    profile: DashboardProfile
    assessment: DashboardAssessment
    career: DashboardCareer
    progress: DashboardProgress
    sections: list[DashboardSection]
