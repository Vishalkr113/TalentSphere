import json
import logging
import random
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


QUESTIONS_PER_ASSESSMENT = 15

ASSESSMENT_DURATION_MINUTES = 30

# ---------------------------------------------------------
# High School Mapping
# ---------------------------------------------------------

HIGH_SCHOOL_CATEGORY_MAP = {
    AssessmentType.HS_APTITUDE: "aptitude",
    AssessmentType.HS_MATHEMATICS: "math",
    AssessmentType.HS_SCIENCE: "science",
    AssessmentType.HS_ENGLISH: "english",
    AssessmentType.HS_REASONING: "reasoning",
}

# ---------------------------------------------------------
# Helpers
# ---------------------------------------------------------

def normalize_stream(
    stream: str | None,
) -> str | None:

    if not stream:
        return None

    value = stream.strip().lower()

    if "pcmb" in value:
        return "pcmb"

    if (
        "pcm" in value
        or (
            "physics" in value
            and "chemistry" in value
            and (
                "math" in value
                or "mathematics" in value
            )
        )
    ):
        return "pcm"

    if (
        "pcb" in value
        or (
            "physics" in value
            and "chemistry" in value
            and "biology" in value
        )
    ):
        return "pcb"

    return value


# ---------------------------------------------------------
# High School Question Bank Resolver
# ---------------------------------------------------------

def resolve_high_school_bank(
    student_class: str | None,
    stream: str | None,
) -> str:

    if not student_class:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=(
                "Student class is required before "
                "starting a high school assessment"
            ),
        )

    student_class = student_class.strip()

    if student_class in {"9", "10"}:
        return "high_school_foundation"

    if student_class == "11":

        normalized_stream = normalize_stream(stream)

        if normalized_stream == "pcm":
            return "high_school_pcm"

        if normalized_stream == "pcb":
            return "high_school_pcb"

        if normalized_stream == "pcmb":
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=(
                    "Class 11 PCMB assessment bank "
                    "is not available yet"
                ),
            )

        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=(
                "A supported Class 11 stream "
                "(PCM or PCB) is required"
            ),
        )

    if student_class == "12":
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=(
                "Class 12 assessment bank "
                "is not available yet"
            ),
        )

    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail="Unsupported high school class",
    )


# ---------------------------------------------------------
# Question Selection
# ---------------------------------------------------------

def get_assessment_questions(
    db: Session,
    user_id: int,
    user_role: str,
    assessment_type: AssessmentType,
):


    # =====================================================
    # High School Student
    # =====================================================

    if user_role == "high_school_student":

        category = HIGH_SCHOOL_CATEGORY_MAP.get(
            assessment_type
        )


        if category is None:

            raise HTTPException(

                status_code=status.HTTP_400_BAD_REQUEST,

                detail=(
                    "This assessment is not available "
                    "for high school students"
                ),

            )


        profile = get_profile_by_user_id(

            db=db,

            user_id=user_id,

        )


        if profile is None:

            raise HTTPException(

                status_code=status.HTTP_400_BAD_REQUEST,

                detail=(
                    "Complete your profile before "
                    "starting an assessment"
                ),

            )


        bank_type = resolve_high_school_bank(

            student_class=profile.student_class,

            stream=profile.stream,

        )


        questions = get_active_questions(

            db=db,

            assessment_type=bank_type,

            user_role=user_role,

        )


        questions = [

            question

            for question in questions

            if question.category == category

        ]


        return questions




    # =====================================================
    # College Student
    # =====================================================

    if user_role == "college_student":


        allowed_assessments = {

            "college_aptitude",

            "college_coding",

        }


        if assessment_type.value not in allowed_assessments:

            raise HTTPException(

                status_code=status.HTTP_400_BAD_REQUEST,

                detail=(
                    "This assessment is not currently "
                    "available for college students"
                ),

            )



        college_map = {

            AssessmentType.APTITUDE:
                "college_aptitude",


            AssessmentType.CODING:
                "college_coding",


            AssessmentType.LOGICAL_REASONING:
                "college_aptitude",

        }



        return get_active_questions(

            db=db,

            assessment_type=college_map.get(

                assessment_type,

                assessment_type.value,

            ),

            user_role=user_role,

        )




    # =====================================================
    # Professional
    # =====================================================

    if user_role == "working_professional":

        raise HTTPException(

            status_code=status.HTTP_400_BAD_REQUEST,

            detail=(
                "Professional assessments "
                "are not available yet"
            ),

        )



    raise HTTPException(

        status_code=status.HTTP_400_BAD_REQUEST,

        detail="Unsupported user role",

    )


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

        attempt = create_attempt(
            db=db,
            user_id=user_id,
            assessment_type=selected_questions[0].assessment_type,
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