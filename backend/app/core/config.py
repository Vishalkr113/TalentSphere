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
    # Upload Configuration
    # ---------------------------------------------------------

    UPLOAD_DIR: str = "uploads"



    # ---------------------------------------------------------
    # AI Configuration
    # ---------------------------------------------------------

    GEMINI_API_KEY: str = ""



    # ---------------------------------------------------------
    # Production Validation
    # ---------------------------------------------------------

    @model_validator(mode="after")
    def validate_security(self):

        if (
            not self.DEBUG
            and self.SECRET_KEY
            in [
                "",
                "CHANGE_THIS_IN_.ENV_FILE",
            ]
        ):

            raise ValueError(
                "SECRET_KEY must be configured in .env file"
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