from sqlalchemy import Column, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship

from app.db.database import Base


class Profile(Base):
    __tablename__ = "profiles"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        unique=True,
        nullable=False,
        index=True,
    )

    # ---------- Common Details ----------

    phone = Column(String, nullable=True)
    date_of_birth = Column(String, nullable=True)
    gender = Column(String, nullable=True)
    city = Column(String, nullable=True)
    state = Column(String, nullable=True)

    skills = Column(Text, nullable=True)
    interests = Column(Text, nullable=True)
    career_goal = Column(String, nullable=True)
    linkedin_url = Column(String, nullable=True)

    # ---------- High School ----------

    school_name = Column(String, nullable=True)

    student_class = Column(
        String,
        nullable=True,
        index=True,
    )

    stream = Column(
        String,
        nullable=True,
        index=True,
    )

    # ---------- College ----------

    college_name = Column(String, nullable=True)
    course = Column(String, nullable=True)

    branch = Column(
        String,
        nullable=True,
        index=True,
    )

    graduation_year = Column(Integer, nullable=True)

    # ---------- Working Professional ----------

    company_name = Column(String, nullable=True)
    job_title = Column(String, nullable=True)

    professional_domain = Column(
        String,
        nullable=True,
        index=True,
    )

    experience_level = Column(
        String,
        nullable=True,
        index=True,
    )

    years_of_experience = Column(
        Integer,
        nullable=True,
    )

    # ---------- Assets ----------

    profile_photo = Column(String, nullable=True)
    resume_url = Column(String, nullable=True)

    # ---------- Completion ----------

    profile_completion = Column(
        Integer,
        default=0,
        nullable=False,
    )

    user = relationship("User")