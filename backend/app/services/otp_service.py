from datetime import datetime, timedelta

from sqlalchemy.orm import Session

from app.models.email_otp import EmailOTP
from app.utils.otp_generator import generate_otp


OTP_EXPIRY_MINUTES = 5


def create_email_otp(
    db: Session,
    user_id: int,
    purpose: str,
):
    # Old unused OTP expire
    db.query(EmailOTP).filter(
        EmailOTP.user_id == user_id,
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
        otp=otp,
        purpose=purpose,
        expires_at=datetime.utcnow()
        + timedelta(minutes=OTP_EXPIRY_MINUTES),
    )

    db.add(record)
    db.commit()
    db.refresh(record)

    return record

def verify_email_otp(
    db: Session,
    user_id: int,
    otp: str,
    purpose: str,
):
    record = (
        db.query(EmailOTP)
        .filter(
            EmailOTP.user_id == user_id,
            EmailOTP.otp == otp,
            EmailOTP.purpose == purpose,
            EmailOTP.is_used == False,
        )
        .first()
    )

    if record is None:
        return False

    if record.expires_at < datetime.utcnow():
        return False

    record.is_used = True

    db.commit()

    return True