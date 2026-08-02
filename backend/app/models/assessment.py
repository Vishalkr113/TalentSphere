from datetime import datetime, timezone

from sqlalchemy import (
    Boolean,
    Column,
    DateTime,
    ForeignKey,
    Integer,
    Float,
    String,
    Text,
    Index,
    UniqueConstraint,
)

from app.db.database import Base


def utc_now():
    return datetime.now(timezone.utc)


# =========================================================
# Assessment Question Bank
# =========================================================

class AssessmentQuestion(Base):

    __tablename__ = "assessment_questions"


    id = Column(
        Integer,
        primary_key=True,
        index=True,
    )


    # Unique Question Identifier
    # Example:
    # APT-MATH-001
    # DSA-PY-ARRAY-001
    question_code = Column(
        String(100),
        unique=True,
        nullable=False,
        index=True,
    )


    # Main Assessment Type
    # college_aptitude
    # college_coding
    # high_school_pcm
    # professional_skill
    assessment_type = Column(
        String(100),
        nullable=False,
        index=True,
    )


    # -----------------------------------------------------
    # User Context
    # -----------------------------------------------------

    user_role = Column(
        String(100),
        nullable=True,
        index=True,
    )


    student_class = Column(
        String(50),
        nullable=True,
        index=True,
    )


    stream = Column(
        String(100),
        nullable=True,
        index=True,
    )


    degree = Column(
        String(100),
        nullable=True,
        index=True,
    )


    branch = Column(
        String(100),
        nullable=True,
        index=True,
    )


    experience_level = Column(
        String(100),
        nullable=True,
        index=True,
    )


    domain = Column(
        String(100),
        nullable=True,
        index=True,
    )


    # -----------------------------------------------------
    # Question Classification
    # -----------------------------------------------------

    category = Column(
        String(100),
        nullable=True,
        index=True,
    )


    topic = Column(
        String(100),
        nullable=True,
        index=True,
    )


    sub_topic = Column(
        String(100),
        nullable=True,
        index=True,
    )


    skill = Column(
        String(100),
        nullable=True,
        index=True,
    )


    # Python / Java / C++ / JavaScript
    # Mainly for DSA & Coding
    language = Column(
        String(50),
        nullable=True,
        index=True,
    )


    # MCQ
    # Coding
    # Debugging
    # Theory
    question_type = Column(
        String(50),
        nullable=False,
        default="mcq",
        index=True,
    )


    # -----------------------------------------------------
    # Question Content
    # -----------------------------------------------------

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
        String(10),
        nullable=False,
    )


    explanation = Column(
        Text,
        nullable=True,
    )


    difficulty = Column(
        String(50),
        nullable=False,
        default="medium",
        index=True,
    )


    is_active = Column(
        Boolean,
        nullable=False,
        default=True,
        index=True,
    )


    created_at = Column(
        DateTime(timezone=True),
        nullable=False,
        default=utc_now,
    )


    updated_at = Column(
        DateTime(timezone=True),
        nullable=False,
        default=utc_now,
        onupdate=utc_now,
    )


    __table_args__ = (

        Index(
            "idx_question_filter",
            "assessment_type",
            "category",
            "difficulty",
        ),

    )



# =========================================================
# Assessment Attempt
# =========================================================

class AssessmentAttempt(Base):

    __tablename__ = "assessment_attempts"


    id = Column(
        Integer,
        primary_key=True,
        index=True,
    )


    user_id = Column(
        Integer,
        ForeignKey(
            "users.id",
            ondelete="CASCADE",
        ),
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
        Float,
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


    __table_args__ = (

        Index(
            "idx_active_assessment_attempt",
            "user_id",
            "assessment_type",
            "status",
        ),

    )



# =========================================================
# Attempt Questions Mapping
# =========================================================

class AssessmentAttemptQuestion(Base):

    __tablename__ = "assessment_attempt_questions"


    __table_args__ = (

        UniqueConstraint(
            "attempt_id",
            "question_id",
            name="uq_attempt_question",
        ),

    )


    id = Column(
        Integer,
        primary_key=True,
        index=True,
    )


    attempt_id = Column(
        Integer,
        ForeignKey(
            "assessment_attempts.id"
        ),
        nullable=False,
        index=True,
    )


    question_id = Column(
        Integer,
        ForeignKey(
            "assessment_questions.id"
        ),
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



# =========================================================
# Assessment Answers
# =========================================================

class AssessmentAnswer(Base):

    __tablename__ = "assessment_answers"


    __table_args__ = (

        UniqueConstraint(
            "attempt_id",
            "question_id",
            name="uq_attempt_answer",
        ),

    )


    id = Column(
        Integer,
        primary_key=True,
        index=True,
    )


    attempt_id = Column(
        Integer,
        ForeignKey(
            "assessment_attempts.id"
        ),
        nullable=False,
        index=True,
    )


    question_id = Column(
        Integer,
        ForeignKey(
            "assessment_questions.id"
        ),
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