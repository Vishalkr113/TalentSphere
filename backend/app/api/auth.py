from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.core.dependencies import get_current_user
from app.db.dependencies import get_db

from app.schemas.user import (
    ForgotPasswordRequest,
    PasswordChange,
    ResetPasswordRequest,
    UserRegister,
    VerifyEmailRequest,
    ResendOTPRequest,
)

from app.services.auth_service import (
    change_password,
    login_user,
    register_user,
    request_password_reset,
    reset_password,
    verify_email,
    resend_email_otp,
)


router = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
)


# ==========================================================
# Register
# ==========================================================

@router.post("/register")
def register(
    user: UserRegister,
    db: Session = Depends(get_db),
):
    return register_user(db, user)


# ==========================================================
# Login
# ==========================================================

@router.post("/login")
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db),
):
    return login_user(
        db=db,
        email=form_data.username,
        password=form_data.password,
    )


# ==========================================================
# Current User
# ==========================================================

@router.get("/me")
def get_me(
    current_user=Depends(get_current_user),
):
    return {
        "id": current_user.id,
        "full_name": current_user.full_name,
        "email": current_user.email,
        "role": current_user.role,
    }


# ==========================================================
# Change Password
# ==========================================================

@router.post("/change-password")
def update_password(
    password_data: PasswordChange,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    return change_password(
        db=db,
        user=current_user,
        current_password=password_data.current_password,
        new_password=password_data.new_password,
    )


# ==========================================================
# Forgot Password
# ==========================================================

@router.post("/forgot-password")
def forgot_password(
    request: ForgotPasswordRequest,
    db: Session = Depends(get_db),
):
    return request_password_reset(
        db=db,
        email=request.email,
    )


# ==========================================================
# Reset Password
# ==========================================================

@router.post("/reset-password")
def reset_password_route(
    request: ResetPasswordRequest,
    db: Session = Depends(get_db),
):
    return reset_password(
        db=db,
        token=request.token,
        new_password=request.new_password,
    )


# ==========================================================
# Verify Email
# ==========================================================

@router.post("/verify-email")
def verify_email_route(
    request: VerifyEmailRequest,
    db: Session = Depends(get_db),
):
    return verify_email(
        db=db,
        email=request.email,
        otp=request.otp,
    )


# ==========================================================
# Resend OTP
# ==========================================================

@router.post("/resend-otp")
def resend_otp(
    request: ResendOTPRequest,
    db: Session = Depends(get_db),
):
    return resend_email_otp(
        db=db,
        email=request.email,
    )


# ==========================================================
# Health Check
# ==========================================================

@router.get("/test")
def auth_test():
    return {
        "status": "success",
        "message": "Authentication API is working.",
    }