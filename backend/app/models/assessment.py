from datetime import datetime, timezone

from sqlalchemy import (
    Boolean,
    Column,
    DateTime,
    ForeignKey,
    Integer,
    String,
    Text,
)

from app.db.database import Base


def utc_now():
    return datetime.now(timezone.utc)


class AssessmentQuestion(Base):
    __tablename__ = "assessment_questions"

    id = Column(
        Integer,
        primary_key=True,
        index=True,
    )

    # Main assessment identifier:
    # aptitude, coding, math, english, science,
    # reasoning, professional_skill, etc.
    assessment_type = Column(
        String,
        nullable=False,
        index=True,
    )

    # Role for which this question is intended:
    # high_school_student, college_student,
    # working_professional
    user_role = Column(
        String,
        nullable=True,
        index=True,
    )

    # More specific assessment category.
    category = Column(
        String,
        nullable=True,
        index=True,
    )

    # Skill measured by this question.
    # Example: Logical Reasoning, Python,
    # Communication, Leadership.
    skill = Column(
        String,
        nullable=True,
        index=True,
    )

    # ---------- High School context ----------

    student_class = Column(
        String,
        nullable=True,
        index=True,
    )

    stream = Column(
        String,
        nullable=True,
        index=True,
    )

    # ---------- College context ----------

    degree = Column(
        String,
        nullable=True,
        index=True,
    )

    branch = Column(
        String,
        nullable=True,
        index=True,
    )

    # ---------- Professional context ----------

    experience_level = Column(
        String,
        nullable=True,
        index=True,
    )

    domain = Column(
        String,
        nullable=True,
        index=True,
    )

    # ---------- Question ----------

    question_text = Column(
        Text,
        nullable=False,
    )

    option_a = Column(
        String,
        nullable=True,
    )

    option_b = Column(
        String,
        nullable=True,
    )

    option_c = Column(
        String,
        nullable=True,
    )

    option_d = Column(
        String,
        nullable=True,
    )

    correct_answer = Column(
        String,
        nullable=False,
    )

    explanation = Column(
        Text,
        nullable=True,
    )

    difficulty = Column(
        String,
        nullable=False,
        default="medium",
    )

    is_active = Column(
        Boolean,
        nullable=False,
        default=True,
    )

    created_at = Column(
        DateTime(timezone=True),
        nullable=False,
        default=utc_now,
    )

class AssessmentAttempt(Base):
    __tablename__ = "assessment_attempts"

    id = Column(
        Integer,
        primary_key=True,
        index=True,
    )

    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False,
        index=True,
    )

    assessment_type = Column(
        String,
        nullable=False,
        index=True,
    )

    total_questions = Column(
        Integer,
        nullable=False,
        default=0,
    )

    correct_answers = Column(
        Integer,
        nullable=False,
        default=0,
    )

    score = Column(
        Integer,
        nullable=False,
        default=0,
    )

    status = Column(
        String,
        nullable=False,
        default="in_progress",
    )

    started_at = Column(
        DateTime(timezone=True),
        nullable=False,
        default=utc_now,
    )

    completed_at = Column(
        DateTime(timezone=True),
        nullable=True,
    )
class AssessmentAttemptQuestion(Base):
    __tablename__ = "assessment_attempt_questions"

    id = Column(
        Integer,
        primary_key=True,
        index=True,
    )

    attempt_id = Column(
        Integer,
        ForeignKey("assessment_attempts.id"),
        nullable=False,
        index=True,
    )

    question_id = Column(
        Integer,
        ForeignKey("assessment_questions.id"),
        nullable=False,
        index=True,
    )

    question_order = Column(
        Integer,
        nullable=False,
    )

    created_at = Column(
        DateTime(timezone=True),
        nullable=False,
        default=utc_now,
    )

class AssessmentAnswer(Base):
    __tablename__ = "assessment_answers"

    id = Column(
        Integer,
        primary_key=True,
        index=True,
    )

    attempt_id = Column(
        Integer,
        ForeignKey("assessment_attempts.id"),
        nullable=False,
        index=True,
    )

    question_id = Column(
        Integer,
        ForeignKey("assessment_questions.id"),
        nullable=False,
        index=True,
    )

    selected_answer = Column(
        String,
        nullable=True,
    )

    is_correct = Column(
        Boolean,
        nullable=False,
        default=False,
    )

    answered_at = Column(
        DateTime(timezone=True),
        nullable=False,
        default=utc_now,
    )