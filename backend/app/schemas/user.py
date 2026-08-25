from enum import Enum

from pydantic import (
    BaseModel,
    ConfigDict,
    EmailStr,
)



# ==========================================================
# User Role
# ==========================================================


class UserRole(str, Enum):

    HIGH_SCHOOL_STUDENT = "high_school_student"

    COLLEGE_STUDENT = "college_student"

    WORKING_PROFESSIONAL = "working_professional"




# ==========================================================
# Register
# ==========================================================


class UserRegister(BaseModel):

    full_name: str

    email: EmailStr

    password: str

    role: UserRole





# ==========================================================
# Login
# ==========================================================


class LoginRequest(BaseModel):

    email: EmailStr

    password: str

    role: UserRole





# ==========================================================
# User Response
# ==========================================================


class UserResponse(BaseModel):

    id: int

    full_name: str

    email: EmailStr

    role: UserRole


    model_config = ConfigDict(
        from_attributes=True
    )





# ==========================================================
# Token
# ==========================================================


class Token(BaseModel):

    access_token: str

    token_type: str





class TokenData(BaseModel):

    email: str | None = None





# ==========================================================
# Password
# ==========================================================


class PasswordChange(BaseModel):

    current_password: str

    new_password: str





class ForgotPasswordRequest(BaseModel):

    email: EmailStr





class ResetPasswordRequest(BaseModel):

    token: str

    new_password: str



# ==========================================================
# Email Verification
# ==========================================================


class VerifyEmailRequest(BaseModel):

    email: EmailStr

    otp: str



class ResendOTPRequest(BaseModel):

    email: EmailStr