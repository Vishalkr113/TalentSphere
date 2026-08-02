from fastapi import (
    APIRouter,
    Depends,
    Query,
)

from sqlalchemy.orm import Session


from app.core.dependencies import (
    get_current_user,
)

from app.db.dependencies import (
    get_db,
)


from app.schemas.assessment import (
    AssessmentHistoryResponse,
    AssessmentResultResponse,
    AssessmentSubmit,
    AssessmentType,
    AttemptResponse,
    QuestionResponse,
)


from app.services.assessment_service import (
    get_assessment_history,
    get_assessment_result,
    start_assessment,
    submit_assessment,
)



router = APIRouter(
    prefix="/assessment",
    tags=["Assessment"],
)



# =========================================================
# Assessment History
# =========================================================

@router.get(
    "/results",
    response_model=AssessmentHistoryResponse,
)
def get_user_assessment_history(

    page: int = Query(
        default=1,
        ge=1,
        description="Page number",
    ),

    limit: int = Query(
        default=10,
        ge=1,
        le=50,
        description="Items per page",
    ),

    db: Session = Depends(get_db),

    current_user=Depends(get_current_user),

):

    return get_assessment_history(

        db=db,

        user_id=current_user.id,

        page=page,

        limit=limit,

    )



# =========================================================
# Specific Assessment Result
# =========================================================

@router.get(
    "/results/{attempt_id}",
    response_model=AssessmentResultResponse,
)
def get_user_assessment_result(

    attempt_id: int,

    db: Session = Depends(get_db),

    current_user=Depends(get_current_user),

):

    return get_assessment_result(

        db=db,

        user_id=current_user.id,

        attempt_id=attempt_id,

    )



# =========================================================
# Start Assessment
# =========================================================

@router.post(
    "/{assessment_type}/start",
)
def start_user_assessment(

    assessment_type: AssessmentType,

    db: Session = Depends(get_db),

    current_user=Depends(get_current_user),

):


    result = start_assessment(

        db=db,

        user_id=current_user.id,

        user_role=current_user.role,

        assessment_type=assessment_type,

    )


    return {

        "attempt":

            AttemptResponse.model_validate(

                result["attempt"]

            ),



        "questions":

            [

                QuestionResponse.model_validate(
                    question
                )

                for question in result["questions"]

            ],

    }



# =========================================================
# Submit Assessment
# =========================================================

@router.post(
    "/{attempt_id}/submit",
    response_model=AssessmentResultResponse,
)
def submit_user_assessment(

    attempt_id: int,

    submission: AssessmentSubmit,

    db: Session = Depends(get_db),

    current_user=Depends(get_current_user),

):


    return submit_assessment(

        db=db,

        user_id=current_user.id,

        attempt_id=attempt_id,

        submission=submission,

    )