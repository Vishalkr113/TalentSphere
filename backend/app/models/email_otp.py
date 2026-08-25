from datetime import datetime

from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
    Boolean,
    ForeignKey,
)

from sqlalchemy.orm import relationship

from app.db.database import Base


class EmailOTP(Base):

    __tablename__ = "email_otps"


    id = Column(
        Integer,
        primary_key=True,
        index=True
    )


    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=True,
    )


    pending_user_id = Column(
        Integer,
        ForeignKey("pending_users.id"),
        nullable=True,
    )


    otp = Column(
        String,
        nullable=False,
    )


    purpose = Column(
        String,
        nullable=False,
    )


    is_used = Column(
        Boolean,
        default=False,
        nullable=False,
    )


    expires_at = Column(
        DateTime,
        nullable=False,
    )


    created_at = Column(
        DateTime,
        default=datetime.utcnow,
    )


    user = relationship(
        "User",
        back_populates="email_otps",
    )


    pending_user = relationship(
        "PendingUser",
        back_populates="email_otps",
    )