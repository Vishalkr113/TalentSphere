from datetime import datetime, timedelta

from sqlalchemy.orm import Session

from app.models.email_otp import EmailOTP

from app.utils.otp_generator import generate_otp


OTP_EXPIRY_MINUTES = 5



def create_email_otp(
    db: Session,
    user_id: int | None = None,
    pending_user_id: int | None = None,
    purpose: str = "REGISTER",
):


    if user_id is None and pending_user_id is None:
        raise ValueError(
            "Either user_id or pending_user_id is required"
        )


    db.query(EmailOTP).filter(
        EmailOTP.is_used == False,
        EmailOTP.purpose == purpose,
    ).update(
        {
            "is_used": True
        }
    )


    otp = generate_otp()


    record = EmailOTP(

        user_id=user_id,

        pending_user_id=pending_user_id,

        otp=otp,

        purpose=purpose,

        expires_at=
        datetime.utcnow()
        +
        timedelta(
            minutes=OTP_EXPIRY_MINUTES
        ),

    )


    db.add(record)

    db.commit()

    db.refresh(record)


    return record





def verify_email_otp(
    db: Session,
    user_id: int | None = None,
    pending_user_id: int | None = None,
    otp: str = "",
    purpose: str = "REGISTER",
):


    query = db.query(
        EmailOTP
    ).filter(
        EmailOTP.otp == otp,
        EmailOTP.purpose == purpose,
        EmailOTP.is_used == False,
    )


    if user_id:
        query = query.filter(
            EmailOTP.user_id == user_id
        )


    if pending_user_id:
        query = query.filter(
            EmailOTP.pending_user_id == pending_user_id
        )


    record = query.first()


    if record is None:
        return False


    if record.expires_at < datetime.utcnow():
        return False



    record.is_used = True


    db.commit()


    return True