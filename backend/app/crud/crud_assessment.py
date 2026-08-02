from typing import Optional, List

from sqlalchemy.orm import Session
from sqlalchemy.sql.expression import func

from app.models.assessment import (
    AssessmentQuestion,
    AssessmentAttempt,
)


class CRUDAssessment:
    """
    CRUD operations for Assessment module.

    Responsibilities:
    - Question fetching
    - Attempt management
    - Assessment history queries
    """


    # ==================================================
    # QUESTION OPERATIONS
    # ==================================================


    def get_random_questions(
        self,
        db: Session,
        assessment_type: str,
        limit: int,
    ) -> List[AssessmentQuestion]:
        """
        Fetch random active questions
        for a specific assessment type.
        """

        return (
            db.query(AssessmentQuestion)
            .filter(
                AssessmentQuestion.assessment_type
                == assessment_type,

                AssessmentQuestion.is_active.is_(True),
            )
            .order_by(
                func.random()
            )
            .limit(limit)
            .all()
        )


    def get_question(
        self,
        db: Session,
        question_id: int,
    ) -> Optional[AssessmentQuestion]:
        """
        Fetch single question by ID.
        """

        return (
            db.query(AssessmentQuestion)
            .filter(
                AssessmentQuestion.id == question_id
            )
            .first()
        )


    def count_questions(
        self,
        db: Session,
        assessment_type: str,
    ) -> int:
        """
        Count available questions.
        """

        return (
            db.query(
                AssessmentQuestion.id
            )
            .filter(
                AssessmentQuestion.assessment_type
                == assessment_type,

                AssessmentQuestion.is_active.is_(True),
            )
            .count()
        )


    # ==================================================
    # ATTEMPT OPERATIONS
    # ==================================================


    def get_user_attempts(
        self,
        db: Session,
        user_id: int,
    ) -> List[AssessmentAttempt]:
        """
        Get all assessment attempts
        of a user.
        """

        return (
            db.query(AssessmentAttempt)
            .filter(
                AssessmentAttempt.user_id
                == user_id
            )
            .order_by(
                AssessmentAttempt.started_at.desc()
            )
            .all()
        )


    def get_latest_attempt(
        self,
        db: Session,
        user_id: int,
        assessment_type: str,
    ) -> Optional[AssessmentAttempt]:
        """
        Get latest attempt of specific type.
        """

        return (
            db.query(AssessmentAttempt)
            .filter(
                AssessmentAttempt.user_id
                == user_id,

                AssessmentAttempt.assessment_type
                == assessment_type,
            )
            .order_by(
                AssessmentAttempt.started_at.desc()
            )
            .first()
        )


    def get_in_progress_attempt(
        self,
        db: Session,
        user_id: int,
        assessment_type: str,
    ) -> Optional[AssessmentAttempt]:
        """
        Check if user already has
        unfinished assessment.
        """

        return (
            db.query(AssessmentAttempt)
            .filter(
                AssessmentAttempt.user_id
                == user_id,

                AssessmentAttempt.assessment_type
                == assessment_type,

                AssessmentAttempt.status
                == "in_progress",
            )
            .first()
        )


    def get_attempt_by_id(
        self,
        db: Session,
        attempt_id: int,
    ) -> Optional[AssessmentAttempt]:
        """
        Fetch attempt by ID.
        """

        return (
            db.query(AssessmentAttempt)
            .filter(
                AssessmentAttempt.id
                == attempt_id
            )
            .first()
        )


    def create_attempt(
        self,
        db: Session,
        attempt: AssessmentAttempt,
    ) -> AssessmentAttempt:
        """
        Create new assessment attempt.
        """

        db.add(attempt)

        db.commit()

        db.refresh(attempt)

        return attempt



    def update_attempt_status(
        self,
        db: Session,
        attempt: AssessmentAttempt,
        status: str,
    ):
        """
        Update attempt status.
        """

        attempt.status = status

        db.commit()

        db.refresh(attempt)

        return attempt



# Singleton CRUD object

crud_assessment = CRUDAssessment()