from contextlib import asynccontextmanager
from pathlib import Path
import logging

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles


from app.core.config import settings


# Register Models
import app.models  # noqa: F401


# Routers
from app.api.auth import router as auth_router
from app.api.profile import router as profile_router
from app.api.dashboard import router as dashboard_router
from app.api.assessment import router as assessment_router



# ==========================================================
# Logger
# ==========================================================

logger = logging.getLogger(
    "talentsphere"
)



# ==========================================================
# Lifespan
# ==========================================================


@asynccontextmanager
async def lifespan(app: FastAPI):

    logger.info(
        "🚀 TalentSphere Backend Started"
    )

    yield


    logger.info(
        "🛑 TalentSphere Backend Stopped"
    )



# ==========================================================
# FastAPI App
# ==========================================================


app = FastAPI(

    title=settings.APP_NAME,

    description=(
        "Backend API for "
        "TalentSphere Career "
        "Development Platform"
    ),

    version=settings.APP_VERSION,

    debug=settings.DEBUG,

    lifespan=lifespan,

)



# ==========================================================
# CORS
# ==========================================================


app.add_middleware(

    CORSMiddleware,

    allow_origins=[

        "http://localhost:5173",

        "http://127.0.0.1:5173",

    ],

    allow_credentials=True,

    allow_methods=[

        "GET",

        "POST",

        "PUT",

        "PATCH",

        "DELETE",

    ],

    allow_headers=[

        "Authorization",

        "Content-Type",

    ],

)



# ==========================================================
# Uploads
# ==========================================================


UPLOAD_DIR = Path(
    settings.UPLOAD_DIR
)


UPLOAD_DIR.mkdir(

    parents=True,

    exist_ok=True,

)



app.mount(

    "/uploads",

    StaticFiles(
        directory=str(UPLOAD_DIR)
    ),

    name="uploads",

)



# ==========================================================
# Routers
# ==========================================================


app.include_router(
    auth_router,
    tags=["Authentication"],
)


app.include_router(
    profile_router,
    tags=["Profile"],
)


app.include_router(
    dashboard_router,
    tags=["Dashboard"],
)


app.include_router(
    assessment_router,
    tags=["Assessment"],
)



# ==========================================================
# System Routes
# ==========================================================


@app.get(
    "/",
    tags=["System"],
)
def root():

    return {

        "status": "success",

        "message":
            "TalentSphere Backend Running Successfully 🚀",

        "version":
            settings.APP_VERSION,

    }




@app.get(
    "/health",
    tags=["System"],
)
def health():

    return {

        "status":
            "healthy",

        "service":
            settings.APP_NAME,

        "version":
            settings.APP_VERSION,

    }