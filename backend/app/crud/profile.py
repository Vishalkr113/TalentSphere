from sqlalchemy.orm import Session

from app.models.profile import Profile
from app.schemas.profile import ProfileCreate, ProfileUpdate


def get_profile_by_user_id(
    db: Session,
    user_id: int,
) -> Profile | None:
    return (
        db.query(Profile)
        .filter(Profile.user_id == user_id)
        .first()
    )


def create_profile(
    db: Session,
    user_id: int,
    profile_data: ProfileCreate,
) -> Profile:
    profile = Profile(
        user_id=user_id,
        **profile_data.model_dump(),
    )

    db.add(profile)
    db.flush()

    return profile


def update_profile(
    db: Session,
    profile: Profile,
    profile_data: ProfileUpdate,
) -> Profile:
    update_data = profile_data.model_dump(
        exclude_unset=True
    )

    for field, value in update_data.items():
        setattr(profile, field, value)

    db.flush()

    return profile


def delete_profile(
    db: Session,
    profile: Profile,
) -> None:
    db.delete(profile)
    db.flush()