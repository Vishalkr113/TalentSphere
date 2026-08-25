import json
import logging
import random
import re
from datetime import datetime, timedelta, timezone

from fastapi import HTTPException, status
from sqlalchemy.orm import Session


from app.crud.assessment import (
    create_answer,
    create_attempt,
    create_attempt_questions,
    get_active_questions,
    get_attempt_questions,
    get_user_attempt,
    get_user_attempts,
    get_in_progress_attempt,
)

from app.crud.assessment_result import (
    create_assessment_result,
    get_result_by_attempt_id,
    result_exists,
)

from app.crud.profile import (
    get_profile_by_user_id,
)

from app.schemas.assessment import (
    AssessmentSubmit,
    AssessmentType,
)

from app.services.assessment_scoring import (
    AssessmentScorer,
)

from app.services.assessment_recommendation import (
    AssessmentRecommendationService,
)

from app.services.assessment_report import (
    AssessmentReportService,
)

from app.utils.json_helper import (
    safe_json_load,
)
from app.assessment_data.schemas import Question

logger = logging.getLogger(__name__)


QUESTIONS_PER_ASSESSMENT = 10

ASSESSMENT_DURATION_MINUTES = 30

# ---------------------------------------------------------
# High School Mapping
# ---------------------------------------------------------

HIGH_SCHOOL_ASSESSMENTS = {
    AssessmentType.HS_FOUNDATION.value, AssessmentType.HS_PCM.value,
    AssessmentType.HS_PCB.value, AssessmentType.HS_COMMERCE.value,
    AssessmentType.HS_ARTS.value, AssessmentType.HS_APTITUDE.value,
    AssessmentType.HS_REASONING.value,
}

def normalize_stream(stream: str | None) -> str | None:
    if not stream: return None
    value = stream.strip().lower()
    if "pcmb" in value: return "pcmb"
    if "pcm" in value or ("physics" in value and "chemistry" in value and ("math" in value or "mathematics" in value)): return "pcm"
    if "pcb" in value or ("physics" in value and "chemistry" in value and "biology" in value): return "pcb"
    if value in {"science", "scientific", "science stream"}: return "pcm"
    if "commerce" in value or "business" in value: return "commerce"
    if "humanities" in value or "arts" in value: return "arts"
    return value

def normalize_student_class(student_class: str | None) -> str | None:
    if not student_class: return None
    value=student_class.strip().lower()
    aliases={"class 9":"9","class 10":"10","class 11":"11","class 12":"12","9th":"9","10th":"10","11th":"11","12th":"12"}
    if value in aliases: return aliases[value]
    m=re.fullmatch(r"(?:class\s*)?(9|10|11|12)(?:st|nd|rd|th)?",value)
    return m.group(1) if m else student_class.strip()

def validate_high_school_assessment_profile(profile) -> None:
    required={"mobile number":profile.phone,"date of birth":profile.date_of_birth,"class":profile.student_class,"board":profile.board,"medium":profile.medium,"country":getattr(profile,"country",None),"state":profile.state,"city":profile.city}
    missing=[k for k,v in required.items() if v is None or (isinstance(v,str) and not v.strip())]
    if missing: raise HTTPException(status_code=400,detail="Complete your required profile information before starting the assessment: "+", ".join(missing))

def resolve_high_school_bank(student_class: str|None, stream: str|None) -> str:
    cls=normalize_student_class(student_class)
    if cls in {"9","10"}: return "high_school_foundation"
    if cls in {"11","12"}:
        bank={"pcm":"high_school_pcm","pcb":"high_school_pcb","commerce":"high_school_commerce","arts":"high_school_arts"}.get(normalize_stream(stream) or "")
        if bank: return bank
        raise HTTPException(status_code=400,detail="A supported high school stream is required")
    raise HTTPException(status_code=400,detail="Unsupported high school class")

def get_assessment_questions(db: Session,user_id:int,user_role:str,assessment_type:AssessmentType):
    profile=get_profile_by_user_id(db=db,user_id=user_id)
    if profile is None: raise HTTPException(status_code=400,detail="Complete your profile before starting an assessment")
    at=assessment_type.value
    if user_role=="high_school_student":
        validate_high_school_assessment_profile(profile)
        if at==AssessmentType.HS_APTITUDE.value:
            return get_active_questions(db=db,assessment_type="college_aptitude",user_role=None)
        if at==AssessmentType.HS_REASONING.value:
            # Existing reasoning bank is seeded under logical_reasoning.
            return get_active_questions(db=db,assessment_type="logical_reasoning",user_role=None)
        if at not in HIGH_SCHOOL_ASSESSMENTS: raise HTTPException(status_code=400,detail="This assessment is not available for high school students")
        return get_active_questions(db=db,assessment_type=at,user_role=None)
    if user_role=="college_student":
        allowed={"college_common","college_aptitude","college_coding","college_dsa","college_technical","college_career"}
        if at not in allowed: raise HTTPException(status_code=400,detail="This assessment is not currently available for college students")
        return get_active_questions(db=db,assessment_type=at,user_role=None,degree=profile.course,branch=profile.branch)
    if user_role=="working_professional":
        allowed={"professional_skill","professional_common","professional_technical","professional_dsa","professional_situational"}
        if at not in allowed: raise HTTPException(status_code=400,detail="This assessment is not available for working professionals")
        # professional_skill remains backwards compatible with the existing professional bank.
        return get_active_questions(db=db,assessment_type=at,user_role=None,experience_level=profile.experience_level,domain=profile.professional_domain)
    raise HTTPException(status_code=400,detail="Unsupported user role")

# ---------------------------------------------------------
# Start Assessment
# ---------------------------------------------------------

def start_assessment(
    db: Session,
    user_id: int,
    user_role: str,
    assessment_type: AssessmentType,
):

    logger.info(
        "Starting assessment '%s' for user %s",
        assessment_type.value,
        user_id,
    )

    # -----------------------------------------------------
    # Prevent Multiple Active Attempts
    # -----------------------------------------------------
    
    active_attempt = get_in_progress_attempt(
        db=db,
        user_id=user_id,
        assessment_type=assessment_type.value,
    )

    if active_attempt:

        logger.warning(
            "User %s already has an active attempt.",
            user_id,
        )

        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=(
                "You already have an active assessment."
            ),
        )

    # -----------------------------------------------------
    # Load Questions
    # -----------------------------------------------------

    available_questions = get_assessment_questions(
        db=db,
        user_id=user_id,
        user_role=user_role,
        assessment_type=assessment_type,
    )

    if len(available_questions) < QUESTIONS_PER_ASSESSMENT:

        logger.error(
            "Insufficient questions for assessment %s",
            assessment_type.value,
        )

        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=(
                "Not enough active questions "
                "available."
            ),
        )

    # -----------------------------------------------------
    # Random Selection
    # -----------------------------------------------------

    selected_questions = random.sample(
        available_questions,
        QUESTIONS_PER_ASSESSMENT,
    )

    # -----------------------------------------------------
    # Create Attempt
    # -----------------------------------------------------

    try:

        # The attempt type must remain the type the user selected.
        # Some high-school compatibility banks (aptitude/reasoning) reuse
        # legacy question-bank types internally; storing that legacy type on
        # the attempt breaks report/history/final-guidance synchronization.
        attempt = create_attempt(
            db=db,
            user_id=user_id,
            assessment_type=assessment_type.value,
            total_questions=len(selected_questions),
        )

        create_attempt_questions(
            db=db,
            attempt_id=attempt.id,
            questions=selected_questions,
        )

        logger.info(
            "Assessment attempt %s created.",
            attempt.id,
        )

    except Exception:

        db.rollback()

        logger.exception(
            "Failed creating assessment."
        )

        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=(
                "Unable to start assessment."
            ),
        )

    return {
        "attempt": attempt,
        "questions": selected_questions,
    }


# ---------------------------------------------------------
# Resume Active Assessment
# ---------------------------------------------------------

def get_active_assessment(
    db: Session,
    user_id: int,
    user_role: str,
    assessment_type: AssessmentType,
):
    attempt = get_in_progress_attempt(
        db=db,
        user_id=user_id,
        assessment_type=assessment_type.value,
    )

    if attempt is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No active assessment found",
        )

    validate_attempt_time(db=db, attempt=attempt)

    questions = get_attempt_questions(
        db=db,
        attempt_id=attempt.id,
    )

    if not questions:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Active assessment has no assigned questions",
        )

    return {"attempt": attempt, "questions": questions}


# ---------------------------------------------------------
# Assessment Expiry Validation
# ---------------------------------------------------------

def validate_attempt_time(
    db: Session,
    attempt,
):

    now = datetime.now(timezone.utc)

    started_at = attempt.started_at


    if started_at.tzinfo is None:
        started_at = started_at.replace(
            tzinfo=timezone.utc
        )


    expires_at = started_at + timedelta(
        minutes=ASSESSMENT_DURATION_MINUTES
    )


    if now > expires_at:

        attempt.status = "expired"

        db.commit()

        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Assessment time expired",
        )
    
# ---------------------------------------------------------
# Submit Assessment
# ---------------------------------------------------------

def submit_assessment(
    db: Session,
    user_id: int,
    attempt_id: int,
    submission: AssessmentSubmit,
):

    attempt = get_user_attempt(
        db=db,
        attempt_id=attempt_id,
        user_id=user_id,
    )

    if attempt is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Assessment attempt not found",
        )


    if attempt.status == "completed":
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Assessment already submitted",
        )


    validate_attempt_time(
        db=db,
        attempt=attempt,
    )


    assigned_questions = get_attempt_questions(
        db=db,
        attempt_id=attempt.id,
    )


    if not assigned_questions:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="No questions assigned",
        )


    if len(submission.answers) != len(assigned_questions):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="All questions must be answered",
        )


    assigned_question_map = {
        q.id: q
        for q in assigned_questions
    }


    submitted_ids = [
        answer.question_id
        for answer in submission.answers
    ]


    if len(submitted_ids) != len(set(submitted_ids)):

        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Duplicate answers found",
        )


    if set(submitted_ids) != set(assigned_question_map.keys()):

        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid questions submitted",
        )


    try:

        answers_map = {}


        for answer in submission.answers:


            question = assigned_question_map.get(
                answer.question_id
            )


            selected = (
                answer.selected_answer or ""
            ).strip()


            correct = (
                question.correct_answer
                .strip()
                .upper()
            )


            option_map = {

                "A": question.option_a,

                "B": question.option_b,

                "C": question.option_c,

                "D": question.option_d,

            }


            if correct in option_map:

                is_correct = (

                    selected.upper() == correct

                    or

                    selected.lower()
                    ==
                    str(
                        option_map[correct]
                    ).lower()

                )


            else:

                is_correct = (

                    selected.lower()
                    ==
                    correct.lower()

                )


            answers_map[
                str(question.id)
            ] = selected



            create_answer(
                db=db,
                attempt_id=attempt.id,
                question_id=question.id,
                selected_answer=selected,
                is_correct=is_correct,
            )


        # -----------------------------
        # Calculate Score
        # -----------------------------

        scorer = AssessmentScorer()


        assessment_result = scorer.evaluate(
            questions=assigned_questions,
            answers=answers_map,
        )


        # -----------------------------
        # Career Recommendation
        # -----------------------------

        recommendation = (
            AssessmentRecommendationService()
            .generate(
                assessment_result
            )
        )


        # -----------------------------
        # Report Generation
        # -----------------------------

        report = (
            AssessmentReportService()
            .generate(
                assessment_result,
                recommendation,
            )
        )


        # -----------------------------
        # Save Result
        # -----------------------------

        if result_exists(
            db=db,
            attempt_id=attempt.id,
        ):

            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Assessment result already exists",
            )


        create_assessment_result(
            db=db,
            data={

                "attempt_id": attempt.id,

                "user_id": user_id,

                "score":
                    assessment_result["score"],

                "percentage":
                    assessment_result["percentage"],

                "grade":
                    assessment_result["grade"],


                "strengths":
                    json.dumps(
                        assessment_result["strengths"]
                    ),


                "weaknesses":
                    json.dumps(
                        assessment_result["weaknesses"]
                    ),


                "recommendation":
                    json.dumps(
                        recommendation
                    ),


                "report":
                    json.dumps(
                        report
                    ),
            },
        )


        # -----------------------------
        # Complete Attempt
        # -----------------------------

        attempt.correct_answers = (
            assessment_result["correct"]
        )


        attempt.score = (
            assessment_result["percentage"]
        )


        attempt.status = "completed"


        attempt.completed_at = datetime.now(
            timezone.utc
        )


        db.commit()

        db.refresh(attempt)


        logger.info(
            "Assessment %s completed successfully",
            attempt.id,
        )


    except HTTPException:

        db.rollback()
        raise


    except Exception:

        db.rollback()

        logger.exception(
            "Assessment submission failed user=%s attempt=%s",
            user_id,
            attempt_id,
        )


        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Assessment submission failed",
        )


    return {

        "attempt_id":
            attempt.id,


        "assessment_type":
            attempt.assessment_type,


        "total_questions":
            attempt.total_questions,


        "correct_answers":
            attempt.correct_answers,


        "score":
            attempt.score,


        "percentage":
            assessment_result["percentage"],


        "grade":
            assessment_result["grade"],


        "strengths":
            assessment_result["strengths"],


        "weaknesses":
            assessment_result["weaknesses"],


        "recommendation":
            recommendation,


        "report":
            report,


        "status":
            attempt.status,


        "completed_at":
            attempt.completed_at,
    }

# ---------------------------------------------------------
# Assessment History
# ---------------------------------------------------------

def get_assessment_history(
    db: Session,
    user_id: int,
    page: int = 1,
    limit: int = 10,
):

    offset = (
        (page - 1)
        * limit
    )


    attempts = (
        get_user_attempts(
            db=db,
            user_id=user_id,
        )
    )


    total_attempts = len(attempts)


    attempts = attempts[
        offset:
        offset + limit
    ]


    history = []


    for attempt in attempts:

        result = get_result_by_attempt_id(
            db=db,
            attempt_id=attempt.id,
        )


        history.append(
            {

                "attempt_id":
                    attempt.id,


                "assessment_type":
                    attempt.assessment_type,


                "total_questions":
                    attempt.total_questions,


                "correct_answers":
                    attempt.correct_answers,


                "score":
                    attempt.score,


                "percentage":
                    result.percentage
                    if result else 0,


                "grade":
                    result.grade
                    if result else None,


                "strengths":
                    safe_json_load(
                        result.strengths
                    )
                    if result else [],


                "weaknesses":
                    safe_json_load(
                        result.weaknesses
                    )
                    if result else [],


                "status":
                    attempt.status,


                "started_at":
                    attempt.started_at,


                "completed_at":
                    attempt.completed_at,

            }
        )


    return {

        "total_attempts":
            total_attempts,


        "page":
            page,


        "limit":
            limit,


        "attempts":
            history,

    }

    attempts = get_user_attempts(
        db=db,
        user_id=user_id,
    )

    history = []

    for attempt in attempts:

        result = get_result_by_attempt_id(
            db=db,
            attempt_id=attempt.id,
        )

        history.append(
            {
                "attempt_id": attempt.id,

                "assessment_type":
                    attempt.assessment_type,

                "total_questions":
                    attempt.total_questions,

                "correct_answers":
                    attempt.correct_answers,

                "score":
                    attempt.score,

                "percentage":
                    result.percentage
                    if result else 0,

                "grade":
                    result.grade
                    if result else None,

                "strengths":
                    safe_json_load(
                        result.strengths
                    )
                    if result else [],

                "weaknesses":
                    safe_json_load(
                        result.weaknesses
                    )
                    if result else [],

                "status":
                    attempt.status,

                "started_at":
                    attempt.started_at,

                "completed_at":
                    attempt.completed_at,
            }
        )

    return {
        "total_attempts": len(history),
        "attempts": history,
    }

# ---------------------------------------------------------
# Assessment Result
# ---------------------------------------------------------

def get_assessment_result(
    db: Session,
    user_id: int,
    attempt_id: int,
):

    attempt = get_user_attempt(
        db=db,
        attempt_id=attempt_id,
        user_id=user_id,
    )


    if attempt is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Assessment attempt not found",
        )


    result = get_result_by_attempt_id(
        db=db,
        attempt_id=attempt.id,
    )


    return {
    "attempt_id": attempt.id,

    "assessment_type": attempt.assessment_type,

    "total_questions": attempt.total_questions,

    "correct_answers": attempt.correct_answers,

    "score": attempt.score,

    "percentage": result.percentage if result else 0,

    "grade": result.grade if result else "",

    "strengths": safe_json_load(
        result.strengths,
        default=[]
    ) if result else [],


    "weaknesses": safe_json_load(
        result.weaknesses,
        default=[]
    ) if result else [],


    "recommendation": safe_json_load(
        result.recommendation
    ) if result else {},


    "report": safe_json_load(
        result.report
    ) if result else {},


    "status": attempt.status,

    "completed_at": attempt.completed_at,
}