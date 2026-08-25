from logging.config import fileConfig

from alembic import context

from sqlalchemy import (
    engine_from_config,
)

from sqlalchemy import pool


from app.core.config import settings

from app.db.database import Base



# ==========================================================
# Import Models
# ==========================================================


# User
from app.models.user import User  # noqa: F401


# Pending User (OTP verification flow)
from app.models.pending_user import PendingUser  # noqa: F401


# Email OTP
from app.models.email_otp import EmailOTP  # noqa: F401


# Profile
from app.models.profile import Profile  # noqa: F401


# Assessment
from app.models.assessment import (
    AssessmentAnswer,
    AssessmentAttempt,
    AssessmentAttemptQuestion,
    AssessmentQuestion,
)  # noqa: F401


# Assessment Result
from app.models.assessment_result import (
    AssessmentResult,
)  # noqa: F401





# ==========================================================
# Alembic Config
# ==========================================================


config = context.config



# Always use application database

config.set_main_option(
    "sqlalchemy.url",
    settings.DATABASE_URL,
)



if config.config_file_name:

    fileConfig(
        config.config_file_name
    )





# ==========================================================
# Metadata
# ==========================================================


target_metadata = Base.metadata





# ==========================================================
# Offline Migration
# ==========================================================


def run_migrations_offline():

    url = config.get_main_option(
        "sqlalchemy.url"
    )


    context.configure(

        url=url,

        target_metadata=target_metadata,

        literal_binds=True,

        dialect_opts={
            "paramstyle": "named",
        },

        compare_type=True,

    )


    with context.begin_transaction():

        context.run_migrations()








# ==========================================================
# Online Migration
# ==========================================================


def run_migrations_online():

    connectable = engine_from_config(

        config.get_section(
            config.config_ini_section,
            {},
        ),

        prefix="sqlalchemy.",

        poolclass=pool.NullPool,

    )


    with connectable.connect() as connection:


        context.configure(

            connection=connection,

            target_metadata=target_metadata,

            compare_type=True,

            render_as_batch=True,

        )


        with context.begin_transaction():

            context.run_migrations()



# ==========================================================
# Run Migration
# ==========================================================


if context.is_offline_mode():

    run_migrations_offline()


else:

    run_migrations_online()