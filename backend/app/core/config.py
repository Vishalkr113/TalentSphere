from functools import lru_cache

from pydantic import EmailStr, Field, model_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):

    # ---------------------------------------------------------
    # Application
    # ---------------------------------------------------------

    APP_NAME: str = "TalentSphere API"

    APP_VERSION: str = "1.0.0"

    DEBUG: bool = False


    # ---------------------------------------------------------
    # Database
    # ---------------------------------------------------------

    DATABASE_URL: str = Field(
        default="sqlite:///./talentsphere.db",
        description="Database connection URL",
    )


    # ---------------------------------------------------------
    # JWT Security
    # ---------------------------------------------------------

    SECRET_KEY: str = Field(
        ...,
        description="JWT Secret Key",
    )


    ALGORITHM: str = "HS256"


    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60



    # ---------------------------------------------------------
    # SMTP Email Configuration
    # ---------------------------------------------------------

    SMTP_HOST: str = ""

    SMTP_PORT: int = 465

    SMTP_EMAIL: EmailStr | str = ""

    SMTP_PASSWORD: str = ""

    SMTP_FROM: EmailStr | str = ""



    # ---------------------------------------------------------
    # CORS
    # ---------------------------------------------------------

    CORS_ORIGINS: str = (
    "https://talentsphere-1-yqpn.onrender.com,"
    "http://localhost:5173,"
    "http://127.0.0.1:5173"

    )

    # ---------------------------------------------------------
    # Upload Configuration
    # ---------------------------------------------------------

    UPLOAD_DIR: str = "uploads"



    # ---------------------------------------------------------
    # AI Configuration
    # ---------------------------------------------------------

    GEMINI_API_KEY: str = ""

    GEMINI_MODEL: str = "gemini-3.5-flash"



    # ---------------------------------------------------------
    # Production Validation
    # ---------------------------------------------------------

    @model_validator(mode="after")
    def validate_security(self):

        insecure_keys = {
            "",
            "CHANGE_THIS_IN_.ENV_FILE",
            "replace_with_secure_random_secret_key",
            "change_me",
            "changeme",
            "secret",
            "secret-key",
        }

        if not self.DEBUG and (
            self.SECRET_KEY.strip() in insecure_keys
            or len(self.SECRET_KEY.strip()) < 32
        ):
            raise ValueError(
                "SECRET_KEY must be a strong random value of at least 32 characters."
            )

        return self



    # ---------------------------------------------------------
    # Pydantic Settings
    # ---------------------------------------------------------

    model_config = SettingsConfigDict(

        env_file=".env",

        env_file_encoding="utf-8",

        case_sensitive=False,

        extra="ignore",

    )



@lru_cache
def get_settings() -> Settings:

    return Settings()



settings = get_settings()