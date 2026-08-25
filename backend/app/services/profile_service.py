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


def calculate_profile_completion(profile, user_role) -> int:
    try:
        role = UserRole(user_role)
    except ValueError:
        return 0

    def has(value) -> bool:
        if value is None:
            return False
        if isinstance(value, str):
            return bool(value.strip())
        return True

    if role == UserRole.HIGH_SCHOOL_STUDENT:
        required = [
            profile.phone,
            profile.date_of_birth,
            profile.student_class,
            profile.board,
            profile.medium,
            profile.country,
            profile.state,
            profile.city,
        ]
        normalized_class = str(profile.student_class or '').strip().lower()
        if normalized_class in {
            '11', '12',
            'class 11', 'class11',
            'class 12', 'class12',
            '11th', '12th',
        }:
            required.append(profile.stream)
    elif role == UserRole.COLLEGE_STUDENT:
        required = [profile.phone, profile.city, profile.state, profile.course, profile.branch, profile.semester]
    elif role == UserRole.WORKING_PROFESSIONAL:
        required = [profile.phone, profile.city, profile.state, profile.company_name, profile.job_title, profile.professional_domain, profile.experience_level, profile.target_role]
    else:
        required = []

    if not required:
        return 0
    return round(sum(1 for value in required if has(value)) / len(required) * 100)


def get_or_create_user_profile(
    db: Session,
    user_id: int,
):
    profile = get_profile_by_user_id(db, user_id)
    if profile is not None:
        return profile

    profile = create_profile(db, user_id, ProfileCreate())
    db.commit()
    db.refresh(profile)
    return profile


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