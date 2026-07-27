from datetime import datetime
from enum import Enum

from pydantic import BaseModel, ConfigDict


# ---------------------------------------------------------
# Assessment Types
# ---------------------------------------------------------

class AssessmentType(str, Enum):
    # High School
    HS_APTITUDE = "hs_aptitude"
    HS_MATHEMATICS = "hs_mathematics"
    HS_SCIENCE = "hs_science"
    HS_ENGLISH = "hs_english"
    HS_REASONING = "hs_reasoning"

    # College
    COLLEGE_APTITUDE = "college_aptitude"
    COLLEGE_TECHNICAL = "college_technical"
    COLLEGE_CODING = "college_coding"

    # Working Professional
    PROFESSIONAL_SKILLS = "professional_skills"
    PROFESSIONAL_TECHNICAL = "professional_technical"
    PROFESSIONAL_READINESS = "professional_readiness"


# ---------------------------------------------------------
# Difficulty
# ---------------------------------------------------------

class DifficultyLevel(str, Enum):
    EASY = "easy"
    MEDIUM = "medium"
    HARD = "hard"


# ---------------------------------------------------------
# Attempt Status
# ---------------------------------------------------------

class AttemptStatus(str, Enum):
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"


# ---------------------------------------------------------
# Question Response
# ---------------------------------------------------------

class QuestionResponse(BaseModel):
    id: int
    assessment_type: str

    # Question classification
    category: str | None = None
    skill: str | None = None

    question_text: str

    option_a: str | None = None
    option_b: str | None = None
    option_c: str | None = None
    option_d: str | None = None

    difficulty: DifficultyLevel

    model_config = ConfigDict(
        from_attributes=True
    )


# ---------------------------------------------------------
# Answer Submission
# ---------------------------------------------------------

class AnswerSubmit(BaseModel):
    question_id: int
    selected_answer: str | None = None


class AssessmentSubmit(BaseModel):
    answers: list[AnswerSubmit]


# ---------------------------------------------------------
# Assessment Attempt
# ---------------------------------------------------------

class AttemptResponse(BaseModel):
    id: int
    assessment_type: AssessmentType
    total_questions: int
    status: AttemptStatus
    started_at: datetime

    model_config = ConfigDict(
        from_attributes=True
    )


# ---------------------------------------------------------
# Assessment Result
# ---------------------------------------------------------

class AssessmentResultResponse(BaseModel):
    attempt_id: int
    assessment_type: AssessmentType
    total_questions: int
    correct_answers: int
    score: int
    status: AttemptStatus
    completed_at: datetime | None = None


# ---------------------------------------------------------
# Assessment History
# ---------------------------------------------------------

class AssessmentHistoryItem(BaseModel):
    attempt_id: int
    assessment_type: str
    total_questions: int
    correct_answers: int
    score: int
    status: AttemptStatus
    started_at: datetime
    completed_at: datetime | None = None


class AssessmentHistoryResponse(BaseModel):
    total_attempts: int
    attempts: list[AssessmentHistoryItem]