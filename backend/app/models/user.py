from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import relationship

from app.db.database import Base


class User(Base):

    __tablename__ = "users"


    id = Column(
        Integer,
        primary_key=True,
        index=True,
    )


    full_name = Column(
        String,
        nullable=False,
    )


    email = Column(
        String,
        unique=True,
        index=True,
        nullable=False,
    )


    hashed_password = Column(
        String,
        nullable=False,
    )


    role = Column(
        String,
        nullable=False,
    )


    is_verified = Column(
        Boolean,
        default=False,
        nullable=False,
    )


    # ==========================
    # Profile Relation
    # ==========================

    profile = relationship(
        "Profile",
        back_populates="user",
        uselist=False,
        cascade="all, delete-orphan",
    )


    # ==========================
    # Email OTP Relation
    # ==========================

    email_otps = relationship(
        "EmailOTP",
        back_populates="user",
        cascade="all, delete-orphan",
    )