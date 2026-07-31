from sqlalchemy.orm import Session
from sqlalchemy.sql.expression import func

from app.models.assessment import AssessmentQuestion


class CRUDAssessment:

    # --------------------------------------------------
    # Get Random Questions
    # --------------------------------------------------

    def get_random_questions(
        self,
        db: Session,
        assessment_type: str,
        limit: int,
    ):

        return (
            db.query(AssessmentQuestion)
            .filter(
                AssessmentQuestion.assessment_type == assessment_type,
                AssessmentQuestion.is_active.is_(True),
            )
            .order_by(func.random())
            .limit(limit)
            .all()
        )

    # --------------------------------------------------
    # Get Question By ID
    # --------------------------------------------------

    def get_question(
        self,
        db: Session,
        question_id: int,
    ):

        return (
            db.query(AssessmentQuestion)
            .filter(
                AssessmentQuestion.id == question_id,
            )
            .first()
        )

    # --------------------------------------------------
    # Count Questions
    # --------------------------------------------------

    def count_questions(
        self,
        db: Session,
        assessment_type: str,
    ):

        return (
            db.query(AssessmentQuestion)
            .filter(
                AssessmentQuestion.assessment_type == assessment_type,
                AssessmentQuestion.is_active.is_(True),
            )
            .count()
        )


crud_assessment = CRUDAssessment()