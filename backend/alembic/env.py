from logging.config import fileConfig

from alembic import context
from sqlalchemy import engine_from_config, pool

from app.core.config import settings
from app.db.database import Base

# ---------------------------------------------------------
# Import all models
# ---------------------------------------------------------
# These imports register all database tables in Base.metadata
# so Alembic can detect schema changes.

from app.models.user import User  # noqa: F401
from app.models.profile import Profile  # noqa: F401
from app.models.assessment import (  # noqa: F401
    AssessmentAnswer,
    AssessmentAttempt,
    AssessmentAttemptQuestion,
    AssessmentQuestion,
)


# ---------------------------------------------------------
# Alembic Configuration
# ---------------------------------------------------------

config = context.config

# Always use the same database URL as the application.
config.set_main_option(
    "sqlalchemy.url",
    settings.DATABASE_URL,
)

if config.config_file_name is not None:
    fileConfig(config.config_file_name)


# ---------------------------------------------------------
# Metadata
# ---------------------------------------------------------

target_metadata = Base.metadata


# ---------------------------------------------------------
# Offline Migrations
# ---------------------------------------------------------

def run_migrations_offline() -> None:
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


# ---------------------------------------------------------
# Online Migrations
# ---------------------------------------------------------

def run_migrations_online() -> None:
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


# RUN

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()