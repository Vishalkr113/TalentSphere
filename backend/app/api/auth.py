from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.db.dependencies import get_db
from app.core.dependencies import get_current_user
from app.schemas.user import (
    ForgotPasswordRequest,
    PasswordChange,
    ResetPasswordRequest,
    UserRegister,
    VerifyEmailRequest,
    ResendOTPRequest,
)

from app.services.auth_service import verify_email

from app.services.auth_service import (
    register_user,
    login_user,
    change_password,
    request_password_reset,
    reset_password,
)

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
)


@router.post("/register")
def register(
    user: UserRegister,
    db: Session = Depends(get_db),
):
    return register_user(db, user)


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


@router.get("/me")
def me(
    current_user=Depends(get_current_user),
):
    return {
        "id": current_user.id,
        "full_name": current_user.full_name,
        "email": current_user.email,
        "role": current_user.role,
    }


@router.get("/test")
def test():
    return {
        "message": "Authentication Router Working Successfully"
    }


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

@router.post("/forgot-password")
def forgot_password(
    request: ForgotPasswordRequest,
    db: Session = Depends(get_db),
):
    return request_password_reset(
        db=db,
        email=request.email,
    )


@router.post("/reset-password")
def update_forgotten_password(
    request: ResetPasswordRequest,
    db: Session = Depends(get_db),
):
    return reset_password(
        db=db,
        token=request.token,
        new_password=request.new_password,
    )
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
