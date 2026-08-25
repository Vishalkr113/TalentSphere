from datetime import datetime

from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
)

from sqlalchemy.orm import relationship

from app.db.database import Base



class PendingUser(Base):

    __tablename__ = "pending_users"


    id = Column(
        Integer,
        primary_key=True,
        index=True
    )


    full_name = Column(
        String,
        nullable=False
    )


    email = Column(
        String,
        unique=True,
        index=True,
        nullable=False
    )


    hashed_password = Column(
        String,
        nullable=False
    )


    role = Column(
        String,
        nullable=False
    )


    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )


    email_otps = relationship(
        "EmailOTP",
        back_populates="pending_user",
        cascade="all, delete-orphan",
    )