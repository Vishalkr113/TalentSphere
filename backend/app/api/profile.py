from io import BytesIO
from pathlib import Path
from uuid import uuid4

from fastapi import (
    APIRouter,
    Depends,
    File,
    HTTPException,
    UploadFile,
    status,
)
from PIL import Image, UnidentifiedImageError
from sqlalchemy.orm import Session

from app.core.dependencies import get_current_user
from app.db.dependencies import get_db
from app.schemas.profile import (
    ProfileCreate,
    ProfileResponse,
    ProfileUpdate,
)
from app.services.profile_service import (
    create_user_profile,
    get_user_profile,
    update_user_profile,
)

from app.services.profile_service import (
    create_user_profile,
    get_user_profile,
    update_user_profile,
    calculate_profile_completion,
)


router = APIRouter(
    prefix="/profile",
    tags=["Profile"],
)


# ---------------------------------------------------------
# Upload Directories
# ---------------------------------------------------------

PROFILE_PHOTO_DIR = Path("uploads/profile_photos")
RESUME_DIR = Path("uploads/resumes")

PROFILE_PHOTO_DIR.mkdir(
    parents=True,
    exist_ok=True,
)

RESUME_DIR.mkdir(
    parents=True,
    exist_ok=True,
)


# ---------------------------------------------------------
# Profile Photo Configuration
# ---------------------------------------------------------

ALLOWED_IMAGE_TYPES = {
    "image/jpeg",
    "image/png",
    "image/webp",
}

ALLOWED_IMAGE_FORMATS = {
    "JPEG": ".jpg",
    "PNG": ".png",
    "WEBP": ".webp",
}

MAX_IMAGE_SIZE = 5 * 1024 * 1024  # 5 MB


# ---------------------------------------------------------
# Resume Configuration
# ---------------------------------------------------------

ALLOWED_RESUME_TYPES = {
    "application/pdf",
}

MAX_RESUME_SIZE = 5 * 1024 * 1024  # 5 MB


# ---------------------------------------------------------
# Create Profile
# ---------------------------------------------------------

@router.post(
    "",
    response_model=ProfileResponse,
)
def create_profile(
    profile_data: ProfileCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    return create_user_profile(
        db=db,
        user_id=current_user.id,
        user_role=current_user.role,
        profile_data=profile_data,
    )

# ---------------------------------------------------------
# Get Current User Profile
# ---------------------------------------------------------

@router.get(
    "/me",
    response_model=ProfileResponse,
)
def get_my_profile(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    return get_user_profile(
        db=db,
        user_id=current_user.id,
    )


# ---------------------------------------------------------
# Update Current User Profile
# ---------------------------------------------------------

@router.patch(
    "/me",
    response_model=ProfileResponse,
)
def update_my_profile(
    profile_data: ProfileUpdate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    return update_user_profile(
        db=db,
        user_id=current_user.id,
        user_role=current_user.role,
        profile_data=profile_data,
    )
# ---------------------------------------------------------
# Upload Profile Photo
# ---------------------------------------------------------

@router.post(
    "/photo",
    response_model=ProfileResponse,
)
async def upload_profile_photo(
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    profile = get_user_profile(
        db=db,
        user_id=current_user.id,
    )

    # Check declared MIME type
    if file.content_type not in ALLOWED_IMAGE_TYPES:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Only JPEG, PNG and WEBP images are allowed",
        )

    file_content = await file.read()

    # Empty file check
    if not file_content:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Uploaded file is empty",
        )

    # File size check
    if len(file_content) > MAX_IMAGE_SIZE:
        raise HTTPException(
            status_code=status.HTTP_413_REQUEST_ENTITY_TOO_LARGE,
            detail="Profile photo must be 5 MB or smaller",
        )

    # Verify actual image content
    try:
        image = Image.open(BytesIO(file_content))

        image.verify()

        image_format = image.format

    except (
        UnidentifiedImageError,
        OSError,
        SyntaxError,
    ):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid or corrupted image file",
        )

    # Only allow supported actual image formats
    if image_format not in ALLOWED_IMAGE_FORMATS:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Unsupported image format",
        )

    extension = ALLOWED_IMAGE_FORMATS[image_format]

    filename = (
        f"user_{current_user.id}_{uuid4().hex}{extension}"
    )

    file_path = PROFILE_PHOTO_DIR / filename

    # Save new image first
    try:
        file_path.write_bytes(file_content)

    except OSError:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Could not save profile photo",
        )

    old_photo_path = None

    if profile.profile_photo:
        old_photo_path = Path(profile.profile_photo)

    # Update database
    
    profile.profile_photo = file_path.as_posix()

    profile.profile_completion = calculate_profile_completion(
        profile,
        current_user.role,
    )

    try:
        db.commit()
        db.refresh(profile)

    except Exception:
        db.rollback()

        # Remove newly created file if DB update fails
        if file_path.exists():
            file_path.unlink()

        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Could not update profile photo",
        )

    # Delete old photo only after DB update succeeds
    if (
        old_photo_path
        and old_photo_path.exists()
        and old_photo_path.is_file()
        and old_photo_path != file_path
    ):
        try:
            old_photo_path.unlink()
        except OSError:
            pass

    return profile


# ---------------------------------------------------------
# Upload Resume
# ---------------------------------------------------------

@router.post(
    "/resume",
    response_model=ProfileResponse,
)
async def upload_resume(
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    profile = get_user_profile(
        db=db,
        user_id=current_user.id,
    )

    # Check declared MIME type
    if file.content_type not in ALLOWED_RESUME_TYPES:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Only PDF resume files are allowed",
        )

    file_content = await file.read()

    # Empty file check
    if not file_content:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Uploaded resume is empty",
        )

    # File size check
    if len(file_content) > MAX_RESUME_SIZE:
        raise HTTPException(
            status_code=status.HTTP_413_REQUEST_ENTITY_TOO_LARGE,
            detail="Resume must be 5 MB or smaller",
        )

    # Check actual PDF signature
    if not file_content.startswith(b"%PDF-"):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid PDF file",
        )

    filename = (
        f"user_{current_user.id}_{uuid4().hex}.pdf"
    )

    file_path = RESUME_DIR / filename

    # Save new resume first
    try:
        file_path.write_bytes(file_content)

    except OSError:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Could not save resume",
        )

    old_resume_path = None

    if profile.resume_url:
        old_resume_path = Path(profile.resume_url)

    # Update database
    profile.resume_url = file_path.as_posix()

    profile.profile_completion = calculate_profile_completion(
        profile,
        current_user.role,
    )

    try:
        db.commit()
        db.refresh(profile)

    except Exception:
        db.rollback()

        # Remove new file if DB update fails
        if file_path.exists():
            file_path.unlink()

        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Could not update resume",
        )

    # Delete old resume only after DB update succeeds
    if (
        old_resume_path
        and old_resume_path.exists()
        and old_resume_path.is_file()
        and old_resume_path != file_path
    ):
        try:
            old_resume_path.unlink()
        except OSError:
            pass

    return profile

# ---------------------------------------------------------
# Delete Profile Photo
# ---------------------------------------------------------

@router.delete(
    "/photo",
    response_model=ProfileResponse,
)
def delete_profile_photo(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    profile = get_user_profile(
        db=db,
        user_id=current_user.id,
    )

    if not profile.profile_photo:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Profile photo not found",
        )

    photo_path = Path(profile.profile_photo)

    # Remove photo reference from database

    profile.profile_photo = None

    try:
        db.commit()
        db.refresh(profile)

    except Exception:
        db.rollback()

        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Could not remove profile photo",
        )

    # Delete physical file after database update succeeds
    if photo_path.exists() and photo_path.is_file():
        try:
            photo_path.unlink()
        except OSError:
            pass

    return profile

# ---------------------------------------------------------
# Delete Resume
# ---------------------------------------------------------

@router.delete(
    "/resume",
    response_model=ProfileResponse,
)
def delete_resume(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    profile = get_user_profile(
        db=db,
        user_id=current_user.id,
    )

    # No resume uploaded
    if not profile.resume_url:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Resume not found",
        )

    resume_path = Path(profile.resume_url)

    # Remove resume reference from database
    profile.resume_url = None

    try:
        db.commit()
        db.refresh(profile)

    except Exception:
        db.rollback()

        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Could not delete resume",
        )

    # Delete physical file only after DB update succeeds
    if resume_path.exists() and resume_path.is_file():
        try:
            resume_path.unlink()
        except OSError:
            pass

    return profile