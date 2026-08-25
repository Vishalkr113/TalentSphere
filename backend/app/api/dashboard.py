from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.dependencies import get_current_user
from app.db.dependencies import get_db
from app.schemas.dashboard import DashboardResponse
from app.services.dashboard_service import get_dashboard_data


router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"],
)


@router.get(
    "",
    response_model=DashboardResponse,
)
def get_dashboard(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    return get_dashboard_data(
        db=db,
        current_user=current_user,
    )