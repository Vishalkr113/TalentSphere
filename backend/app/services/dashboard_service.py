from sqlalchemy.orm import Session

from app.crud.assessment import get_user_attempts
from app.crud.profile import get_profile_by_user_id
from app.schemas.user import UserRole


DASHBOARD_SECTIONS = {
    UserRole.HIGH_SCHOOL_STUDENT: [
        {
            "key": "learning_progress",
            "title": "Learning Progress",
            "available": False,
        },
        {
            "key": "career_exploration",
            "title": "Career Exploration",
            "available": False,
        },
        {
            "key": "skill_assessment",
            "title": "Skill Assessment",
            "available": True,
        },
        {
            "key": "daily_tasks",
            "title": "Daily Tasks",
            "available": False,
        },
    ],

    UserRole.COLLEGE_STUDENT: [
        {
            "key": "placement",
            "title": "Placement",
            "available": False,
        },
        {
            "key": "coding_progress",
            "title": "Coding Progress",
            "available": False,
        },
        {
            "key": "resume",
            "title": "Resume",
            "available": False,
        },
        {
            "key": "skill_assessment",
            "title": "Skill Assessment",
            "available": True,
        },
        {
            "key": "daily_tasks",
            "title": "Daily Tasks",
            "available": False,
        },
    ],

    UserRole.WORKING_PROFESSIONAL: [
        {
            "key": "skill_growth",
            "title": "Skill Growth",
            "available": False,
        },
        {
            "key": "promotion_readiness",
            "title": "Promotion Readiness",
            "available": False,
        },
        {
            "key": "certifications",
            "title": "Certifications",
            "available": False,
        },
        {
            "key": "career_growth",
            "title": "Career Growth",
            "available": False,
        },
        {
            "key": "daily_tasks",
            "title": "Daily Tasks",
            "available": False,
        },
    ],
}


def empty_assessment_item():
    return {
        "completed": False,
        "score": None,
        "correct_answers": None,
        "total_questions": None,
        "attempt_id": None,
        "completed_at": None,
    }


def build_assessment_summary(
    db: Session,
    user_id: int,
):
    attempts = get_user_attempts(
        db=db,
        user_id=user_id,
    )

    completed_attempts = [
        attempt
        for attempt in attempts
        if attempt.status == "completed"
    ]

    aptitude = empty_assessment_item()
    coding = empty_assessment_item()

    for attempt in completed_attempts:
        if (
            attempt.assessment_type == "aptitude"
            and not aptitude["completed"]
        ):
            aptitude = {
                "completed": True,
                "score": attempt.score,
                "correct_answers": attempt.correct_answers,
                "total_questions": attempt.total_questions,
                "attempt_id": attempt.id,
                "completed_at": attempt.completed_at,
            }

        elif (
            attempt.assessment_type == "coding"
            and not coding["completed"]
        ):
            coding = {
                "completed": True,
                "score": attempt.score,
                "correct_answers": attempt.correct_answers,
                "total_questions": attempt.total_questions,
                "attempt_id": attempt.id,
                "completed_at": attempt.completed_at,
            }

    return {
        "available": True,
        "total_completed": len(completed_attempts),
        "aptitude": aptitude,
        "coding": coding,
    }

def build_dashboard_sections(
    user_role,
    profile=None,
    assessment=None,
):

    sections = [
        section.copy()
        for section in DASHBOARD_SECTIONS[user_role]
    ]


    if user_role == UserRole.COLLEGE_STUDENT:

        for section in sections:


            # Resume unlock
            if section["key"] == "resume":

                section["available"] = bool(
                    profile
                    and profile.resume_url
                )


            # Placement unlock
            elif section["key"] == "placement":

                profile_completed = (
                    profile
                    and profile.profile_completion == 100
                )

                resume_uploaded = (
                    profile
                    and profile.resume_url
                )

                assessment_completed = (
                    assessment
                    and assessment["total_completed"] > 0
                )


                section["available"] = bool(
                    profile_completed
                    and resume_uploaded
                    and assessment_completed
                )


    return sections

def get_dashboard_data(
    db: Session,
    current_user,
):

    profile = get_profile_by_user_id(
        db,
        current_user.id,
    )


    if profile is None:

        profile_data = {
            "exists": False,
            "profile_completion": 0,
            "profile_photo": None,
            "resume_url": None,
        }

    else:

        profile_data = {
            "exists": True,
            "profile_completion": profile.profile_completion,
            "profile_photo": profile.profile_photo,
            "resume_url": profile.resume_url,
        }


    user_role = UserRole(current_user.role)


    assessment_data = build_assessment_summary(
        db=db,
        user_id=current_user.id,
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

        "assessment": assessment_data,

        "sections": build_dashboard_sections(
            user_role=user_role,
            profile=profile,
            assessment=assessment_data,
        ),
    }