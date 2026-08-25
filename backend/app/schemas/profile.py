from datetime import date

from pydantic import BaseModel, ConfigDict


class ProfileBase(BaseModel):

    # ---------- Common ----------

    phone: str | None = None
    date_of_birth: date | None = None
    gender: str | None = None
    city: str | None = None
    state: str | None = None
    country: str | None = None

    skills: list[str] | None = None
    interests: list[str] | None = None

    career_goal: str | None = None

    linkedin_url: str | None = None
    github_url: str | None = None
    portfolio_url: str | None = None


    # ---------- High School ----------

    school_name: str | None = None
    student_class: str | None = None
    stream: str | None = None


    # ---------- College ----------

    college_name: str | None = None
    course: str | None = None
    branch: str | None = None
    graduation_year: int | None = None
    university_name: str | None = None
    semester: str | None = None
    cgpa: str | None = None
    target_role: str | None = None


    # ---------- High School Extended ----------

    board: str | None = None
    medium: str | None = None
    roll_number: str | None = None
    admission_year: int | None = None
    percentage: str | None = None
    blood_group: str | None = None
    district: str | None = None
    pin_code: str | None = None
    parent_name: str | None = None
    parent_mobile: str | None = None
    parent_email: str | None = None
    parent_occupation: str | None = None
    favorite_subject: str | None = None
    weak_subject: str | None = None
    hobbies: list[str] | None = None
    languages: list[str] | None = None


    # ---------- Professional ----------

    company_name: str | None = None
    job_title: str | None = None
    professional_domain: str | None = None
    experience_level: str | None = None
    years_of_experience: int | None = None
    expected_salary: str | None = None



class ProfileCreate(ProfileBase):
    pass



class ProfileUpdate(ProfileBase):
    pass



class ProfileResponse(ProfileBase):

    id: int
    user_id: int

    profile_photo: str | None = None
    resume_url: str | None = None

    profile_completion: int

    model_config = ConfigDict(
        from_attributes=True
    )