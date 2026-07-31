from datetime import datetime, timezone

from sqlalchemy import (
    Column,
    Integer,
    String,
    Float,
    Text,
    DateTime,
    ForeignKey,
)

from app.db.database import Base


def utc_now():
    return datetime.now(timezone.utc)


class AssessmentResult(Base):

    __tablename__ = "assessment_results"


    id = Column(
        Integer,
        primary_key=True,
        index=True,
    )


    attempt_id = Column(
        Integer,
        ForeignKey("assessment_attempts.id"),
        nullable=False,
        unique=True,
        index=True,
    )


    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False,
        index=True,
    )


    score = Column(
        Float,
        nullable=False,
    )


    percentage = Column(
        Float,
        nullable=False,
    )


    grade = Column(
        String,
        nullable=False,
    )


    strengths = Column(
        Text,
        nullable=True,
    )


    weaknesses = Column(
        Text,
        nullable=True,
    )


    recommendation = Column(
        Text,
        nullable=True,
    )


    report = Column(
        Text,
        nullable=True,
    )


    created_at = Column(
        DateTime(timezone=True),
        nullable=False,
        default=utc_now,
    )