from typing import Optional, List

from sqlalchemy.orm import Session

from app.models.assessment_result import AssessmentResult


# =========================================================
# CREATE RESULT
# =========================================================

def create_assessment_result(
    db: Session,
    data: dict,
) -> AssessmentResult:
    """
    Create new assessment result.
    """

    result = AssessmentResult(
        **data
    )

    db.add(result)

    db.flush()

    return result



# =========================================================
# GET RESULT BY ATTEMPT
# =========================================================

def get_result_by_attempt_id(
    db: Session,
    attempt_id: int,
) -> Optional[AssessmentResult]:
    """
    Fetch assessment result
    using attempt id.
    """

    return (
        db.query(AssessmentResult)
        .filter(
            AssessmentResult.attempt_id
            == attempt_id
        )
        .first()
    )



# =========================================================
# GET USER RESULT HISTORY
# =========================================================

def get_user_results(
    db: Session,
    user_id: int,
) -> List[AssessmentResult]:
    """
    Fetch complete assessment
    history of a user.
    """

    return (
        db.query(AssessmentResult)
        .filter(
            AssessmentResult.user_id
            == user_id
        )
        .order_by(
            AssessmentResult.created_at.desc()
        )
        .all()
    )



# =========================================================
# GET LATEST RESULT
# =========================================================

def get_latest_user_result(
    db: Session,
    user_id: int,
) -> Optional[AssessmentResult]:
    """
    Fetch latest completed
    assessment result.
    """

    return (
        db.query(AssessmentResult)
        .filter(
            AssessmentResult.user_id
            == user_id
        )
        .order_by(
            AssessmentResult.created_at.desc()
        )
        .first()
    )



# =========================================================
# CHECK EXISTING RESULT
# =========================================================

def result_exists(
    db: Session,
    attempt_id: int,
) -> bool:
    """
    Check whether result already exists
    for an attempt.
    """

    return (
        db.query(AssessmentResult.id)
        .filter(
            AssessmentResult.attempt_id
            == attempt_id
        )
        .first()
        is not None
    )



# =========================================================
# UPDATE RESULT
# =========================================================

def update_assessment_result(
    db: Session,
    result: AssessmentResult,
    data: dict,
) -> AssessmentResult:
    """
    Update existing assessment result.
    """

    for key, value in data.items():

        if hasattr(result, key):
            setattr(
                result,
                key,
                value
            )


    db.flush()

    return result



# =========================================================
# DELETE RESULT
# =========================================================

def delete_assessment_result(
    db: Session,
    result: AssessmentResult,
):
    """
    Delete assessment result.
    """

    db.delete(result)

    db.flush()


