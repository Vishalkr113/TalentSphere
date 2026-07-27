import random
from datetime import datetime, timezone

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
)
from app.crud.profile import get_profile_by_user_id
from app.schemas.assessment import (
    AssessmentSubmit,
    AssessmentType,
)


QUESTIONS_PER_ASSESSMENT = 15


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
        )

        questions = [
            question
            for question in questions
            if question.category == category
        ]

        return questions

    if user_role == "college_student":
        if assessment_type not in {
            AssessmentType.COLLEGE_APTITUDE,
            AssessmentType.COLLEGE_CODING,
        }:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=(
                    "This assessment is not currently "
                    "available for college students"
                ),
            )

        return get_active_questions(
            db=db,
            assessment_type=assessment_type.value,
        )

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
    available_questions = get_assessment_questions(
        db=db,
        user_id=user_id,
        user_role=user_role,
        assessment_type=assessment_type,
    )

    if len(available_questions) < QUESTIONS_PER_ASSESSMENT:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=(
                "Not enough active questions available "
                "for this assessment"
            ),
        )

    selected_questions = random.sample(
        available_questions,
        QUESTIONS_PER_ASSESSMENT,
    )

    attempt = create_attempt(
        db=db,
        user_id=user_id,
        assessment_type=assessment_type.value,
        total_questions=len(selected_questions),
    )

    try:
        create_attempt_questions(
            db=db,
            attempt_id=attempt.id,
            questions=selected_questions,
        )

    except Exception:
        db.rollback()

        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Could not prepare assessment questions",
        )

    return {
        "attempt": attempt,
        "questions": selected_questions,
    }


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
            detail=(
                "Assessment attempt has already "
                "been completed"
            ),
        )

    assigned_questions = get_attempt_questions(
        db=db,
        attempt_id=attempt.id,
    )

    if len(assigned_questions) != attempt.total_questions:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Assessment question assignment is invalid",
        )

    if len(submission.answers) != attempt.total_questions:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="All assessment questions must be answered",
        )

    submitted_question_ids = [
        answer.question_id
        for answer in submission.answers
    ]

    if len(submitted_question_ids) != len(
        set(submitted_question_ids)
    ):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Duplicate question answers are not allowed",
        )

    assigned_question_ids = {
        question.id
        for question in assigned_questions
    }

    if set(submitted_question_ids) != assigned_question_ids:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=(
                "Submitted questions do not match "
                "the assigned assessment questions"
            ),
        )

    questions_by_id = {
        question.id: question
        for question in assigned_questions
    }

    correct_answers = 0

    try:
        for submitted_answer in submission.answers:
            question = questions_by_id[
                submitted_answer.question_id
            ]

            if not question.is_active:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail=(
                        "One or more questions are "
                        "no longer active"
                    ),
                )

            selected_answer = (
                submitted_answer.selected_answer.strip().upper()
                if submitted_answer.selected_answer
                else None
            )

            correct_answer = (
                question.correct_answer.strip().upper()
            )

            is_correct = (
                selected_answer == correct_answer
            )

            if is_correct:
                correct_answers += 1

            create_answer(
                db=db,
                attempt_id=attempt.id,
                question_id=question.id,
                selected_answer=selected_answer,
                is_correct=is_correct,
            )

        score = round(
            (
                correct_answers
                / attempt.total_questions
            )
            * 100
        )

        attempt.correct_answers = correct_answers
        attempt.score = score
        attempt.status = "completed"
        attempt.completed_at = datetime.now(
            timezone.utc
        )

        db.commit()
        db.refresh(attempt)

    except HTTPException:
        db.rollback()
        raise

    except Exception:
        db.rollback()

        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Could not submit assessment",
        )

    return {
        "attempt_id": attempt.id,
        "assessment_type": attempt.assessment_type,
        "total_questions": attempt.total_questions,
        "correct_answers": attempt.correct_answers,
        "score": attempt.score,
        "status": attempt.status,
        "completed_at": attempt.completed_at,
    }


# ---------------------------------------------------------
# Assessment History
# ---------------------------------------------------------

def get_assessment_history(
    db: Session,
    user_id: int,
):
    attempts = get_user_attempts(
        db=db,
        user_id=user_id,
    )

    history = []

    for attempt in attempts:
        history.append(
            {
                "attempt_id": attempt.id,
                "assessment_type": attempt.assessment_type,
                "total_questions": attempt.total_questions,
                "correct_answers": attempt.correct_answers,
                "score": attempt.score,
                "status": attempt.status,
                "started_at": attempt.started_at,
                "completed_at": attempt.completed_at,
            }
        )

    return {
        "total_attempts": len(history),
        "attempts": history,
    }


# ---------------------------------------------------------
# Specific Assessment Result
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

    return {
        "attempt_id": attempt.id,
        "assessment_type": attempt.assessment_type,
        "total_questions": attempt.total_questions,
        "correct_answers": attempt.correct_answers,
        "score": attempt.score,
        "status": attempt.status,
        "started_at": attempt.started_at,
        "completed_at": attempt.completed_at,
    }