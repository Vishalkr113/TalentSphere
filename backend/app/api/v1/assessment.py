"""
Assessment API

Endpoints

POST    /assessment/start

GET     /assessment/{assessment_id}

POST    /assessment/{assessment_id}/submit

GET     /assessment/{assessment_id}/result

GET     /assessment/{assessment_id}/report

GET     /assessment/{assessment_id}/recommendation
"""

from __future__ import annotations

from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi import status

from app.services.assessment_engine import AssessmentEngine
from app.services.assessment_report import AssessmentReportService
from app.services.assessment_recommendation import (
    AssessmentRecommendationService,
)
from app.services.assessment_scoring import AssessmentScorer

router = APIRouter(
    prefix="/assessment",
    tags=["Assessment"],
)

engine = AssessmentEngine()

scorer = AssessmentScorer()

recommendation_service = AssessmentRecommendationService()

report_service = AssessmentReportService()


# =====================================================
# START ASSESSMENT
# =====================================================

@router.post(
    "/start",
    status_code=status.HTTP_201_CREATED,
)
async def start_assessment():

    """
    Create a new assessment.
    """

    return {
        "message": "Not Implemented Yet"
    }


# =====================================================
# GET ASSESSMENT
# =====================================================

@router.get(
    "/{assessment_id}",
)
async def get_assessment(
    assessment_id: str,
):

    return {
        "assessment_id": assessment_id,
        "message": "Not Implemented Yet",
    }


# =====================================================
# SUBMIT
# =====================================================

@router.post(
    "/{assessment_id}/submit",
)
async def submit_assessment(
    assessment_id: str,
):

    return {
        "assessment_id": assessment_id,
        "message": "Not Implemented Yet",
    }


# =====================================================
# RESULT
# =====================================================

@router.get(
    "/{assessment_id}/result",
)
async def get_result(
    assessment_id: str,
):

    return {
        "assessment_id": assessment_id,
        "message": "Not Implemented Yet",
    }


# =====================================================
# REPORT
# =====================================================

@router.get(
    "/{assessment_id}/report",
)
async def get_report(
    assessment_id: str,
):

    return {
        "assessment_id": assessment_id,
        "message": "Not Implemented Yet",
    }


# =====================================================
# RECOMMENDATION
# =====================================================

@router.get(
    "/{assessment_id}/recommendation",
)
async def get_recommendation(
    assessment_id: str,
):

    return {
        "assessment_id": assessment_id,
        "message": "Not Implemented Yet",
    }