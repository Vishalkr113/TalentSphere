from sqlalchemy import create_engine
from sqlalchemy.orm import (
    declarative_base,
    sessionmaker,
    Session,
)

from app.core.config import settings



# ==========================================================
# Database Engine
# ==========================================================


database_url = settings.DATABASE_URL



connect_args = {}


# SQLite specific configuration
if database_url.startswith(
    "sqlite"
):

    connect_args = {
        "check_same_thread": False
    }



engine = create_engine(

    database_url,

    connect_args=connect_args,

    pool_pre_ping=True,

    future=True,

)



# ==========================================================
# Session Factory
# ==========================================================


SessionLocal = sessionmaker(

    autocommit=False,

    autoflush=False,

    bind=engine,

    expire_on_commit=False,

)



# ==========================================================
# Base Model
# ==========================================================


Base = declarative_base()



# ==========================================================
# Database Dependency
# ==========================================================


def get_db():

    db: Session = SessionLocal()


    try:

        yield db


    except Exception:

        db.rollback()

        raise


    finally:

        db.close()