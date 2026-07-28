from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from app.core.security import (
    hash_password,
    verify_password,
    create_access_token,
    create_password_reset_token,
    decode_password_reset_token,
)
from app.crud.user import (
    get_user_by_email,
    create_user,
)
from app.models.user import User
from app.schemas.user import UserRegister

from app.services.otp_service import create_email_otp
from app.services.email_service import send_otp_email

from app.services.otp_service import verify_email_otp

def verify_email(
    db: Session,
    email: str,
    otp: str,
):
    user = get_user_by_email(db, email)

    if user is None:
        raise HTTPException(
            status_code=404,
            detail="User not found.",
        )

    valid = verify_email_otp(
        db=db,
        user_id=user.id,
        otp=otp,
        purpose="REGISTER",
    )

    if not valid:
        raise HTTPException(
            status_code=400,
            detail="Invalid or expired OTP.",
        )

    user.is_verified = True

    db.commit()

    return {
        "message": "Email verified successfully."
    }

def register_user(
    db: Session,
    user_data: UserRegister,
):
    existing_user = get_user_by_email(
        db,
        user_data.email,
    )

    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered",
        )

    user = User(
        full_name=user_data.full_name,
        email=user_data.email,
        hashed_password=hash_password(user_data.password),
        role=user_data.role,
        is_verified=False,
    )

    create_user(db, user)

    otp_record = create_email_otp(
        db=db,
        user_id=user.id,
        purpose="REGISTER",
    )

    email_sent = send_otp_email(
        recipient_email=user.email,
        otp=otp_record.otp,
    )

    if not email_sent:
        raise HTTPException(
            status_code=500,
            detail="Unable to send verification email.",
        )

    return {
        "message": "OTP sent successfully. Please verify your email.",
        "email": user.email,
    }

def authenticate_user(
    db: Session,
    email: str,
    password: str,
):
    user = get_user_by_email(
        db,
        email,
    )

    if user is None:
        return None

    if not verify_password(
        password,
        user.hashed_password,
    ):
        return None

    return user


def login_user(
    db: Session,
    email: str,
    password: str,
):
    user = authenticate_user(
        db,
        email,
        password,
    )

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
        )
    if not user.is_verified:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Please verify your email before logging in.",
        )

    access_token = create_access_token(
        data={
            "sub": user.email,
            "role": user.role,
        }
    )

    return {
        "access_token": access_token,
        "token_type": "bearer",
    }

def change_password(
    db: Session,
    user: User,
    current_password: str,
    new_password: str,
):
    if not verify_password(
        current_password,
        user.hashed_password,
    ):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Current password is incorrect",
        )

    if verify_password(
        new_password,
        user.hashed_password,
    ):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="New password must be different from current password",
        )

    user.hashed_password = hash_password(
        new_password
    )

    db.add(user)
    db.commit()

    return {
        "message": "Password changed successfully"
    }


def request_password_reset(
    db: Session,
    email: str,
):
    user = get_user_by_email(
        db,
        email,
    )

    if user is None:
        return {
            "message": (
                "If an account exists with this email, "
                "a password reset request has been created."
            )
        }

    reset_token = create_password_reset_token(
        user.email
    )

    return {
        "message": "Password reset request created successfully.",
        "reset_token": reset_token,
    }


def reset_password(
    db: Session,
    token: str,
    new_password: str,
):
    email = decode_password_reset_token(
        token
    )

    if email is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid or expired password reset token",
        )

    user = get_user_by_email(
        db,
        email,
    )

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid or expired password reset token",
        )

    user.hashed_password = hash_password(
        new_password
    )

    db.add(user)
    db.commit()

    return {
        "message": "Password reset successfully"
    }



