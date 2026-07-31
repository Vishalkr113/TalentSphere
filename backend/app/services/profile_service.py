from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.crud.profile import (
    create_profile,
    get_profile_by_user_id,
    update_profile,
)
from app.schemas.profile import ProfileCreate, ProfileUpdate
from app.schemas.user import UserRole


def _has_value(value) -> bool:
    if value is None:
        return False

    if isinstance(value, str):
        return bool(value.strip())

    return True


def calculate_profile_completion(
    profile,
    user_role,
) -> int:

    try:
        role = UserRole(user_role)
    except ValueError:
        return 0

    # Fields required for every user type
    common_fields = [
        profile.phone,
        profile.date_of_birth,
        profile.gender,
        profile.city,
        profile.state,
        profile.skills,
        profile.interests,
        profile.career_goal,
        profile.profile_photo,
        profile.resume_url,
    ]

    if role == UserRole.HIGH_SCHOOL_STUDENT:
        role_fields = [
            profile.school_name,
            profile.student_class,
            profile.stream,
        ]

    elif role == UserRole.COLLEGE_STUDENT:
        role_fields = [
            profile.college_name,
            profile.course,
            profile.branch,
            profile.graduation_year,
        ]

    elif role == UserRole.WORKING_PROFESSIONAL:
        role_fields = [
            profile.company_name,
            profile.job_title,
            profile.professional_domain,
            profile.experience_level,
            profile.years_of_experience,
        ]

    else:
        role_fields = []

    fields = common_fields + role_fields

    completed_fields = sum(
        1
        for value in fields
        if _has_value(value)
    )

    if not fields:
        return 0

    return round(
        (completed_fields / len(fields)) * 100
    )


def get_user_profile(
    db: Session,
    user_id: int,
):
    profile = get_profile_by_user_id(
        db,
        user_id,
    )

    if profile is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Profile not found",
        )

    return profile


def create_user_profile(
    db: Session,
    user_id: int,
    user_role,
    profile_data: ProfileCreate,
):
    existing_profile = get_profile_by_user_id(
        db,
        user_id,
    )

    if existing_profile:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Profile already exists",
        )

    profile = create_profile(
        db,
        user_id,
        profile_data,
    )

    profile.profile_completion = (
        calculate_profile_completion(
            profile,
            user_role,
        )
    )

    try:
        db.commit()
        db.refresh(profile)
    except Exception:
        db.rollback()
        raise

    return profile


def update_user_profile(
    db: Session,
    user_id: int,
    user_role,
    profile_data: ProfileUpdate,
):
    profile = get_profile_by_user_id(
        db,
        user_id,
    )

    if profile is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Profile not found",
        )

    profile = update_profile(
        db,
        profile,
        profile_data,
    )

    profile.profile_completion = (
        calculate_profile_completion(
            profile,
            user_role,
        )
    )
    try:
        db.commit()
        db.refresh(profile)
    except Exception:
        db.rollback()
        raise

    return profile