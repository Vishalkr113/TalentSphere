from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from app.core.security import (
    hash_password,
    verify_password,
    create_access_token,
    decode_password_reset_token,
)

from app.crud.user import (
    get_user_by_email,
    create_user,
)

from app.models.user import User
from app.models.pending_user import PendingUser

from app.schemas.user import UserRegister

from app.services.otp_service import (
    create_email_otp,
    verify_email_otp,
)

from app.services.email_service import (
    send_otp_email,
)



# ==========================================================
# Register User
# ==========================================================

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
            status_code=400,
            detail="Email already registered",
        )


    existing_pending = db.query(
        PendingUser
    ).filter(
        PendingUser.email == user_data.email
    ).first()


    if existing_pending:

        db.delete(existing_pending)
        db.commit()



    pending_user = PendingUser(

    full_name=user_data.full_name,

    email=user_data.email,

    hashed_password=
    hash_password(
        user_data.password
    ),

    role=user_data.role,

    )


    db.add(pending_user)

    db.commit()

    db.refresh(pending_user)



    otp_record = create_email_otp(

        db=db,

        pending_user_id=pending_user.id,

        purpose="REGISTER",

    )



    email_sent = send_otp_email(

        recipient_email=pending_user.email,

        otp=otp_record.otp,

    )


    if not email_sent:

        raise HTTPException(
            status_code=500,
            detail="Unable to send OTP email.",
        )



    return {

        "message":
        "OTP sent successfully. Please verify your email.",

        "email":
        pending_user.email,

    }





# ==========================================================
# Verify Email
# ==========================================================

def verify_email(

    db: Session,

    email: str,

    otp: str,

):


    pending_user = db.query(
        PendingUser
    ).filter(
        PendingUser.email == email
    ).first()



    if pending_user is None:

        raise HTTPException(
            status_code=404,
            detail="Registration request not found.",
        )



    valid = verify_email_otp(

        db=db,

        pending_user_id=pending_user.id,

        otp=otp,

        purpose="REGISTER",

    )



    if not valid:

        raise HTTPException(
            status_code=400,
            detail="Invalid or expired OTP.",
        )



    user = User(

        full_name=pending_user.full_name,

        email=pending_user.email,

        hashed_password=pending_user.hashed_password,

        role=pending_user.role,

        is_verified=True,

    )


    create_user(
        db,
        user
    )



    db.delete(
        pending_user
    )


    db.commit()



    return {

        "message":
        "Email verified successfully. Account created.",

    }





# ==========================================================
# Resend OTP
# ==========================================================

def resend_email_otp(

    db: Session,

    email: str,

):


    pending_user = db.query(
        PendingUser
    ).filter(
        PendingUser.email == email
    ).first()



    if pending_user is None:

        raise HTTPException(
            status_code=404,
            detail="Registration request not found.",
        )



    otp_record = create_email_otp(

        db=db,

        pending_user_id=pending_user.id,

        purpose="REGISTER",

    )


    send_otp_email(

        recipient_email=pending_user.email,

        otp=otp_record.otp,

    )



    return {

        "message":
        "OTP resent successfully.",

        "email":
        pending_user.email,

    }





# ==========================================================
# Login
# ==========================================================

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
            status_code=401,
            detail="Incorrect email or password",
        )



    if not user.is_verified:

        raise HTTPException(
            status_code=403,
            detail="Please verify your email before logging in.",
        )



    token = create_access_token(

        data={
            "sub": user.email,
            "role": user.role,
        }

    )


    return {

        "access_token": token,

        "token_type": "bearer",

        "user": {

            "id": user.id,

            "full_name": user.full_name,

            "email": user.email,

            "role": user.role,

            "is_verified": user.is_verified,

        }

    }





# ==========================================================
# Change Password
# ==========================================================

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
            status_code=400,
            detail="Current password is incorrect",
        )



    user.hashed_password = hash_password(
        new_password
    )


    db.commit()


    return {
        "message":
        "Password changed successfully"
    }





# ==========================================================
# Password Reset
# ==========================================================

def request_password_reset(

    db: Session,

    email: str,

):

    return {

        "message":
        "If account exists, reset link sent."

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
            status_code=400,
            detail="Invalid reset token",
        )



    user = get_user_by_email(
        db,
        email,
    )


    if user is None:

        raise HTTPException(
            status_code=400,
            detail="User not found",
        )



    user.hashed_password = hash_password(
        new_password
    )


    db.commit()



    return {

        "message":
        "Password reset successfully"

    }