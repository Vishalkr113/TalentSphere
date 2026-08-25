from fastapi import APIRouter, Depends

from app.core.dependencies import get_current_user
from app.schemas.ai import AIGenerateRequest, AIGenerateResponse
from app.core.config import settings
from app.services.gemini_gateway import generate_ai_response


router = APIRouter(prefix="/ai", tags=["AI"])


@router.post("/generate", response_model=AIGenerateResponse)
def generate_ai(
    payload: AIGenerateRequest,
    current_user=Depends(get_current_user),
):
    # Authentication is mandatory; user-specific context is supplied by the caller.
    text = generate_ai_response(
        action=payload.action,
        prompt=payload.prompt,
        context=payload.context,
    )

    return AIGenerateResponse(
        action=payload.action,
        text=text,
        model=settings.GEMINI_MODEL,
    )
