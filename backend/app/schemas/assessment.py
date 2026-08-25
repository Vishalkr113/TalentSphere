"""
Assessment Schemas

Production schemas for:
- Start Assessment
- Submit Assessment
- Attempts
- History
- Results
"""

from __future__ import annotations

from datetime import datetime
from enum import Enum

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
)



# ==========================================================
# Assessment Types
# ==========================================================


class AssessmentType(str, Enum):

    # High School

    HS_FOUNDATION = "high_school_foundation"

    HS_PCM = "high_school_pcm"

    HS_PCB = "high_school_pcb"

    HS_COMMERCE = "high_school_commerce"

    HS_ARTS = "high_school_arts"
    HS_APTITUDE = "high_school_aptitude"
    HS_REASONING = "high_school_reasoning"


    # College

    COLLEGE_COMMON = "college_common"
    
    COLLEGE_APTITUDE = "college_aptitude"

    COLLEGE_CODING = "college_coding"
    COLLEGE_DSA = "college_dsa"
    COLLEGE_TECHNICAL = "college_technical"
    COLLEGE_CAREER = "college_career"


    # Working Professional

    PROFESSIONAL_SKILL = "professional_skill"
    PROFESSIONAL_COMMON = "professional_common"
    PROFESSIONAL_TECHNICAL = "professional_technical"
    PROFESSIONAL_DSA = "professional_dsa"
    PROFESSIONAL_SITUATIONAL = "professional_situational"


    # General

    APTITUDE = "aptitude"

    CODING = "coding"

    LOGICAL_REASONING = "logical_reasoning"



# ==========================================================
# Question Response
# ==========================================================


class QuestionResponse(BaseModel):

    id: int

    question_text: str


    option_a: str | None = None

    option_b: str | None = None

    option_c: str | None = None

    option_d: str | None = None


    difficulty: str


    category: str | None = None

    skill: str | None = None



    model_config = ConfigDict(
        from_attributes=True
    )




# ==========================================================
# Attempt Response
# ==========================================================


class AttemptResponse(BaseModel):

    id: int

    assessment_type: str

    total_questions: int

    correct_answers: int

    score: float

    status: str

    started_at: datetime

    completed_at: datetime | None = None



    model_config = ConfigDict(
        from_attributes=True
    )




# ==========================================================
# Submit Assessment
# ==========================================================


class SubmitAnswer(BaseModel):

    question_id: int

    # Empty answers are allowed so an assessment can be auto-submitted
    # when the timer expires; unanswered questions are scored as incorrect.
    selected_answer: str = ""



class AssessmentSubmit(BaseModel):

    answers: list[SubmitAnswer] = Field(
        min_length=1
    )





# ==========================================================
# Recommendation Response
# ==========================================================


class RecommendationResponse(BaseModel):

    career: str


    learning_path: list[str] = Field(
        default_factory=list
    )


    recommended_projects: list[str] = Field(
        default_factory=list
    )


    recommended_certifications: list[str] = Field(
        default_factory=list
    )


    skill_gaps: list[str] = Field(
        default_factory=list
    )


    next_goal: str | None = None





# ==========================================================
# Report Response
# ==========================================================


class ReportResponse(BaseModel):

    summary: dict

    performance: dict

    skill_matrix: list[dict]


    career: dict | None = None


    placement_readiness: str | None = None


    interview_readiness: str | None = None


    next_steps: list[str] = Field(
        default_factory=list
    )





# ==========================================================
# Assessment Result
# ==========================================================


class AssessmentResultResponse(BaseModel):

    attempt_id: int


    assessment_type: str


    total_questions: int


    correct_answers: int


    score: float


    percentage: float | None = None


    grade: str | None = None



    strengths: list[str] = Field(
        default_factory=list
    )


    weaknesses: list[str] = Field(
        default_factory=list
    )


    recommendation: RecommendationResponse | None = None


    report: ReportResponse | None = None



    status: str


    completed_at: datetime | None = None



# ==========================================================
# Assessment History
# ==========================================================


class AssessmentHistoryItem(BaseModel):

    attempt_id: int

    assessment_type: str

    total_questions: int

    correct_answers: int

    score: float

    status: str

    started_at: datetime

    completed_at: datetime | None = None



    model_config = ConfigDict(
        from_attributes=True
    )



class AssessmentHistoryResponse(BaseModel):

    total_attempts: int

    attempts: list[AssessmentHistoryItem]


    model_config = ConfigDict(
        from_attributes=True
    )


# ==========================================================
# Start Assessment Request
# ==========================================================


class StartAssessmentRequest(BaseModel):

    assessment_type: AssessmentType


# ==========================================================
# End
# ==========================================================