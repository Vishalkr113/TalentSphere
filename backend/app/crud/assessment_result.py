from sqlalchemy.orm import Session

from app.models.assessment_result import AssessmentResult


# ---------------------------------------------------------
# Create Assessment Result
# ---------------------------------------------------------

def create_assessment_result(
    db: Session,
    data: dict,
):

    result = AssessmentResult(
        **data
    )

    db.add(result)

    db.flush()

    return result



# ---------------------------------------------------------
# Get Result By Attempt
# ---------------------------------------------------------

def get_result_by_attempt_id(
    db: Session,
    attempt_id: int,
):

    return (
        db.query(AssessmentResult)
        .filter(
            AssessmentResult.attempt_id == attempt_id
        )
        .first()
    )



# ---------------------------------------------------------
# Get User Results
# ---------------------------------------------------------

def get_user_results(
    db: Session,
    user_id: int,
):

    return (
        db.query(AssessmentResult)
        .filter(
            AssessmentResult.user_id == user_id
        )
        .order_by(
            AssessmentResult.created_at.desc()
        )
        .all()
    )