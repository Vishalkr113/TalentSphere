import json
from datetime import datetime

from sqlalchemy.orm import Session

from app.crud.assessment import get_user_attempts
from app.crud.assessment_result import get_user_results
from app.crud.profile import get_profile_by_user_id
from app.schemas.user import UserRole


def safe_json_load(value) -> list:
    """
    Safely convert a JSON/list-like value into a Python list.

    Supports:
    - None
    - Python list
    - JSON list string
    - Comma-separated string
    """
    if value is None:
        return []

    if isinstance(value, list):
        return value

    if not isinstance(value, str):
        return []

    value = value.strip()

    if not value:
        return []

    try:
        parsed = json.loads(value)
        return parsed if isinstance(parsed, list) else []
    except (json.JSONDecodeError, TypeError):
        return []


def normalize_skills(value) -> list:
    """
    Normalize profile skills into a clean list of strings.

    Handles:
    - None
    - ["Python", "SQL"]
    - '["Python", "SQL"]'
    - "Python, SQL, React"
    """
    if value is None:
        return []

    if isinstance(value, list):
        return [
            str(skill).strip()
            for skill in value
            if str(skill).strip()
        ]

    if isinstance(value, str):
        value = value.strip()

        if not value:
            return []

        # JSON list stored as text
        if value.startswith("["):
            parsed = safe_json_load(value)
            return [
                str(skill).strip()
                for skill in parsed
                if str(skill).strip()
            ]

        # Normal comma-separated skills
        return [
            skill.strip()
            for skill in value.split(",")
            if skill.strip()
        ]

    return []


def safe_json_object(value) -> dict:
    """
    Safely convert a JSON object value into a Python dict.
    """
    if value is None:
        return {}

    if isinstance(value, dict):
        return value

    if not isinstance(value, str):
        return {}

    value = value.strip()

    if not value:
        return {}

    try:
        parsed = json.loads(value)
        return parsed if isinstance(parsed, dict) else {}
    except (json.JSONDecodeError, TypeError):
        return {}


def normalize_learning_path(value) -> list:
    """
    Ensure learning_path is always returned as a list.
    """
    if value is None:
        return []

    if isinstance(value, list):
        return value

    if isinstance(value, str):
        parsed = safe_json_load(value)

        if parsed:
            return parsed

        return [
            item.strip()
            for item in value.split(",")
            if item.strip()
        ]

    return []


def empty_assessment_item() -> dict:
    return {
        "completed": False,
        "score": None,
        "percentage": None,
        "grade": None,
        "correct_answers": None,
        "total_questions": None,
        "attempt_id": None,
        "completed_at": None,
        "assessment_type": None,
    }


def _attempt_item(attempt, result_by_attempt: dict) -> dict:
    result = result_by_attempt.get(attempt.id)

    completed = (attempt.status or "").lower() == "completed"

    return {
        "completed": completed,
        "score": attempt.score if completed else None,
        "percentage": (
            result.percentage
            if result
            else (attempt.score if completed else None)
        ),
        "grade": result.grade if result else None,
        "correct_answers": (
            attempt.correct_answers
            if completed
            else None
        ),
        "total_questions": attempt.total_questions,
        "attempt_id": attempt.id,
        "completed_at": attempt.completed_at,
        "assessment_type": attempt.assessment_type,
    }


def build_assessment_summary(
    db: Session,
    user_id: int,
) -> dict:
    attempts = get_user_attempts(
        db=db,
        user_id=user_id,
    )

    results = get_user_results(
        db=db,
        user_id=user_id,
    )

    result_by_attempt = {
        result.attempt_id: result
        for result in results
    }

    completed = [
        attempt
        for attempt in attempts
        if (attempt.status or "").lower() == "completed"
    ]

    completed.sort(
        key=lambda attempt: (
            attempt.completed_at or datetime.min
        ),
        reverse=True,
    )

    items = [
        _attempt_item(
            attempt,
            result_by_attempt,
        )
        for attempt in completed
    ]

    latest = (
        items[0]
        if items
        else empty_assessment_item()
    )

    def latest_for(predicate):
        for item in items:
            assessment_type = (
                item.get("assessment_type") or ""
            )

            if predicate(assessment_type):
                return item

        return empty_assessment_item()

    return {
        "available": True,
        "total_completed": len(completed),
        "latest_score": latest["percentage"],
        "latest_grade": latest["grade"],
        "latest_assessment": latest["assessment_type"],
        "latest_completed_at": latest["completed_at"],

        "aptitude": latest_for(
            lambda assessment_type:
                "aptitude" in assessment_type
        ),

        "coding": latest_for(
            lambda assessment_type:
                "coding" in assessment_type
        ),

        "professional": latest_for(
            lambda assessment_type:
                "professional" in assessment_type
        ),

        "high_school": latest_for(
            lambda assessment_type:
                assessment_type.startswith(
                    "high_school_"
                )
        ),

        "recent_attempts": items[:10],
    }


def build_career_summary(
    db: Session,
    user_id: int,
) -> dict:
    results = get_user_results(
        db=db,
        user_id=user_id,
    )

    if not results:
        return {
            "available": False,
            "recommended_role": None,
            "confidence": None,
            "strengths": [],
            "skill_gaps": [],
            "learning_path": [],
        }

    latest = sorted(
        results,
        key=lambda result: (
            result.created_at or datetime.min
        ),
        reverse=True,
    )[0]

    recommendation = safe_json_object(
        latest.recommendation
    )

    return {
        "available": True,
        "recommended_role": recommendation.get(
            "career"
        ),
        "confidence": latest.percentage,
        "strengths": normalize_skills(
            latest.strengths
        ),
        "skill_gaps": normalize_skills(
            latest.weaknesses
        ),
        "learning_path": normalize_learning_path(
            recommendation.get("learning_path")
        ),
    }


def build_progress_summary(
    profile,
    assessment,
    career,
    user_role,
) -> dict:
    resume = (
        100
        if profile and profile.resume_url
        else 0
    )

    assessment_progress = (
        100
        if assessment.get("total_completed", 0) > 0
        else 0
    )

    coding_item = assessment.get(
        "coding",
        {},
    )

    coding = (
        round(
            coding_item.get("percentage") or 0
        )
        if coding_item.get("completed")
        else 0
    )

    placement = (
        round(
            career.get("confidence") or 0
        )
        if career.get("available")
        else 0
    )

    if user_role == UserRole.HIGH_SCHOOL_STUDENT:
        return {
            "resume": resume,
            "assessment": assessment_progress,
            "coding": 0,
            "placement": placement,
        }

    if user_role == UserRole.WORKING_PROFESSIONAL:
        professional = assessment.get(
            "professional",
            {},
        )

        professional_percentage = (
            round(
                professional.get("percentage") or 0
            )
            if professional.get("completed")
            else 0
        )

        return {
            "resume": resume,
            "assessment": professional_percentage,
            "coding": 0,
            "placement": placement,
        }

    return {
        "resume": resume,
        "assessment": assessment_progress,
        "coding": coding,
        "placement": placement,
    }


def build_dashboard_sections(
    user_role,
    profile=None,
    assessment=None,
):
    assessment = assessment or {}

    completed = (
        assessment.get("total_completed", 0) > 0
    )

    resume_uploaded = bool(
        profile and profile.resume_url
    )

    profile_completed = bool(
        profile
        and profile.profile_completion >= 100
    )

    if user_role == UserRole.HIGH_SCHOOL_STUDENT:
        return [
            {
                "key": "learning_progress",
                "title": "Learning Progress",
                "available": True,
            },
            {
                "key": "career_exploration",
                "title": "Career Exploration",
                "available": True,
            },
            {
                "key": "skill_assessment",
                "title": "Skill Assessment",
                "available": completed,
            },
            {
                "key": "daily_tasks",
                "title": "Daily Tasks",
                "available": True,
            },
        ]

    if user_role == UserRole.COLLEGE_STUDENT:
        return [
            {
                "key": "placement",
                "title": "Placement",
                "available": (
                    profile_completed
                    and resume_uploaded
                    and completed
                ),
            },
            {
                "key": "coding_progress",
                "title": "Coding Progress",
                "available": bool(
                    assessment
                    .get("coding", {})
                    .get("completed")
                ),
            },
            {
                "key": "resume",
                "title": "Resume",
                "available": resume_uploaded,
            },
            {
                "key": "skill_assessment",
                "title": "Skill Assessment",
                "available": completed,
            },
            {
                "key": "daily_tasks",
                "title": "Daily Tasks",
                "available": True,
            },
        ]

    return [
        {
            "key": "skill_growth",
            "title": "Skill Growth",
            "available": bool(
                assessment
                .get("professional", {})
                .get("completed")
            ),
        },
        {
            "key": "promotion_readiness",
            "title": "Promotion Readiness",
            "available": bool(
                profile
                and profile.profile_completion >= 70
            ),
        },
        {
            "key": "certifications",
            "title": "Certifications",
            "available": True,
        },
        {
            "key": "career_growth",
            "title": "Career Growth",
            "available": bool(
                assessment
                .get("professional", {})
                .get("completed")
            ),
        },
        {
            "key": "daily_tasks",
            "title": "Daily Tasks",
            "available": True,
        },
    ]


def get_dashboard_data(
    db: Session,
    current_user,
):
    profile = get_profile_by_user_id(
        db,
        current_user.id,
    )

    user_role = UserRole(
        current_user.role
    )

    profile_data = {
        "exists": profile is not None,

        "profile_completion": (
            profile.profile_completion
            if profile
            else 0
        ),

        "profile_photo": (
            profile.profile_photo
            if profile
            else None
        ),

        "resume_url": (
            profile.resume_url
            if profile
            else None
        ),

        "student_class": (
            profile.student_class
            if profile
            else None
        ),

        "stream": (
            profile.stream
            if profile
            else None
        ),

        "board": (
            profile.board
            if profile
            else None
        ),

        "school_name": (
            profile.school_name
            if profile
            else None
        ),

        "college_name": (
            profile.college_name
            if profile
            else None
        ),

        "course": (
            profile.course
            if profile
            else None
        ),

        "branch": (
            profile.branch
            if profile
            else None
        ),

        "semester": (
            profile.semester
            if profile
            else None
        ),

        "cgpa": (
            profile.cgpa
            if profile
            else None
        ),

        "company_name": (
            profile.company_name
            if profile
            else None
        ),

        "job_title": (
            profile.job_title
            if profile
            else None
        ),

        "target_role": (
            profile.target_role
            if profile
            else None
        ),

        # IMPORTANT:
        # Always return skills as a list.
        "skills": normalize_skills(
            profile.skills
            if profile
            else None
        ),
    }

    assessment = build_assessment_summary(
        db,
        current_user.id,
    )

    career = build_career_summary(
        db,
        current_user.id,
    )

    return {
        "dashboard_type": user_role,

        "user": {
            "id": current_user.id,
            "full_name": current_user.full_name,
            "email": current_user.email,
            "role": user_role,
        },

        "profile": profile_data,

        "assessment": assessment,

        "career": career,

        "progress": build_progress_summary(
            profile,
            assessment,
            career,
            user_role,
        ),

        "sections": build_dashboard_sections(
            user_role,
            profile,
            assessment,
        ),
    }