from sqlalchemy import or_
from sqlalchemy.orm import Session

from app.models.assessment import (
    AssessmentAnswer,
    AssessmentAttempt,
    AssessmentAttemptQuestion,
    AssessmentQuestion,
)


# ---------------------------------------------------------
# Questions
# ---------------------------------------------------------

def get_active_questions(
    db: Session,
    assessment_type: str,
    user_role: str | None = None,
    student_class: str | None = None,
    stream: str | None = None,
    degree: str | None = None,
    branch: str | None = None,
    experience_level: str | None = None,
    domain: str | None = None,
):
    query = (
        db.query(AssessmentQuestion)
        .filter(
            AssessmentQuestion.assessment_type
            == assessment_type,
            AssessmentQuestion.is_active.is_(True),
        )
    )

    # Role-specific questions + generic questions
    if user_role:
        query = query.filter(
            or_(
                AssessmentQuestion.user_role
                == user_role,
                AssessmentQuestion.user_role.is_(None),
            )
        )

    # High School context
    if student_class:
        query = query.filter(
            or_(
                AssessmentQuestion.student_class
                == student_class,
                AssessmentQuestion.student_class.is_(None),
            )
        )

    if stream:
        query = query.filter(
            or_(
                AssessmentQuestion.stream == stream,
                AssessmentQuestion.stream.is_(None),
            )
        )

    # College context
    if degree:
        query = query.filter(
            or_(
                AssessmentQuestion.degree == degree,
                AssessmentQuestion.degree.is_(None),
            )
        )

    if branch:
        query = query.filter(
            or_(
                AssessmentQuestion.branch == branch,
                AssessmentQuestion.branch.is_(None),
            )
        )

    # Professional context
    if experience_level:
        query = query.filter(
            or_(
                AssessmentQuestion.experience_level
                == experience_level,
                AssessmentQuestion.experience_level.is_(None),
            )
        )

    if domain:
        query = query.filter(
            or_(
                AssessmentQuestion.domain == domain,
                AssessmentQuestion.domain.is_(None),
            )
        )

    return (
        query
        .order_by(AssessmentQuestion.id)
        .all()
    )


def get_question_by_id(
    db: Session,
    question_id: int,
):
    return (
        db.query(AssessmentQuestion)
        .filter(
            AssessmentQuestion.id == question_id
        )
        .first()
    )


# ---------------------------------------------------------
# Attempts
# ---------------------------------------------------------

def create_attempt(
    db: Session,
    user_id: int,
    assessment_type: str,
    total_questions: int,
):
    attempt = AssessmentAttempt(
        user_id=user_id,
        assessment_type=assessment_type,
        total_questions=total_questions,
        correct_answers=0,
        score=0,
        status="in_progress",
    )

    db.add(attempt)
    db.commit()
    db.refresh(attempt)

    return attempt


def get_attempt_by_id(
    db: Session,
    attempt_id: int,
):
    return (
        db.query(AssessmentAttempt)
        .filter(
            AssessmentAttempt.id == attempt_id
        )
        .first()
    )


def get_user_attempt(
    db: Session,
    attempt_id: int,
    user_id: int,
):
    return (
        db.query(AssessmentAttempt)
        .filter(
            AssessmentAttempt.id == attempt_id,
            AssessmentAttempt.user_id == user_id,
        )
        .first()
    )


def get_user_attempts(
    db: Session,
    user_id: int,
):
    return (
        db.query(AssessmentAttempt)
        .filter(
            AssessmentAttempt.user_id == user_id
        )
        .order_by(
            AssessmentAttempt.started_at.desc()
        )
        .all()
    )


# ---------------------------------------------------------
# Attempt Questions
# ---------------------------------------------------------

def create_attempt_questions(
    db: Session,
    attempt_id: int,
    questions: list[AssessmentQuestion],
):
    attempt_questions = []

    for index, question in enumerate(
        questions,
        start=1,
    ):
        attempt_question = AssessmentAttemptQuestion(
            attempt_id=attempt_id,
            question_id=question.id,
            question_order=index,
        )

        db.add(attempt_question)
        attempt_questions.append(
            attempt_question
        )

    try:
        db.commit()
    except Exception:
        db.rollback()
        raise

    return attempt_questions

def get_attempt_questions(
    db: Session,
    attempt_id: int,
):
    return (
        db.query(AssessmentQuestion)
        .join(
            AssessmentAttemptQuestion,
            AssessmentAttemptQuestion.question_id
            == AssessmentQuestion.id,
        )
        .filter(
            AssessmentAttemptQuestion.attempt_id
            == attempt_id
        )
        .order_by(
            AssessmentAttemptQuestion.question_order
        )
        .all()
    )


# ---------------------------------------------------------
# Answers
# ---------------------------------------------------------

def create_answer(
    db: Session,
    attempt_id: int,
    question_id: int,
    selected_answer: str | None,
    is_correct: bool,
):
    answer = AssessmentAnswer(
        attempt_id=attempt_id,
        question_id=question_id,
        selected_answer=selected_answer,
        is_correct=is_correct,
    )

    db.add(answer)

    return answer


def get_attempt_answers(
    db: Session,
    attempt_id: int,
):
    return (
        db.query(AssessmentAnswer)
        .filter(
            AssessmentAnswer.attempt_id
            == attempt_id
        )
        .all()
    )