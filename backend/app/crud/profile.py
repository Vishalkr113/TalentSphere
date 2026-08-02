from typing import Optional

from sqlalchemy.orm import Session

from app.models.profile import Profile
from app.schemas.profile import (
    ProfileCreate,
    ProfileUpdate,
)


# =========================================================
# GET PROFILE
# =========================================================

def get_profile_by_user_id(
    db: Session,
    user_id: int,
) -> Optional[Profile]:
    """
    Fetch profile using user id.
    """

    return (
        db.query(Profile)
        .filter(
            Profile.user_id == user_id
        )
        .first()
    )



# =========================================================
# CHECK PROFILE
# =========================================================

def profile_exists(
    db: Session,
    user_id: int,
) -> bool:
    """
    Check whether user profile exists.
    """

    return (
        db.query(Profile.id)
        .filter(
            Profile.user_id == user_id
        )
        .first()
        is not None
    )



# =========================================================
# CREATE PROFILE
# =========================================================

def create_profile(
    db: Session,
    user_id: int,
    profile_data: ProfileCreate,
) -> Profile:
    """
    Create new user profile.
    """

    profile = Profile(
        user_id=user_id,
        **profile_data.model_dump(),
    )

    db.add(profile)

    db.flush()

    return profile



# =========================================================
# UPDATE PROFILE
# =========================================================

def update_profile(
    db: Session,
    profile: Profile,
    profile_data: ProfileUpdate,
) -> Profile:
    """
    Update profile fields.
    """

    update_data = profile_data.model_dump(
        exclude_unset=True
    )


    for field, value in update_data.items():

        if hasattr(profile, field):

            setattr(
                profile,
                field,
                value,
            )


    db.flush()

    return profile



# =========================================================
# PROFILE MEDIA UPDATE
# =========================================================

def update_profile_photo(
    db: Session,
    profile: Profile,
    photo_url: str,
) -> Profile:
    """
    Update profile photo.
    """

    profile.profile_photo = photo_url

    db.flush()

    return profile



def update_resume(
    db: Session,
    profile: Profile,
    resume_url: str,
) -> Profile:
    """
    Update resume URL.
    """

    profile.resume_url = resume_url

    db.flush()

    return profile



# =========================================================
# DELETE MEDIA
# =========================================================

def remove_profile_photo(
    db: Session,
    profile: Profile,
) -> Profile:
    """
    Remove profile photo.
    """

    profile.profile_photo = None

    db.flush()

    return profile



def remove_resume(
    db: Session,
    profile: Profile,
) -> Profile:
    """
    Remove resume.
    """

    profile.resume_url = None

    db.flush()

    return profile



# =========================================================
# DELETE PROFILE
# =========================================================

def delete_profile(
    db: Session,
    profile: Profile,
) -> None:
    """
    Delete complete profile.
    """

    db.delete(profile)

    db.flush()