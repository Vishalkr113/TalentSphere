from functools import lru_cache

from fastapi import HTTPException, status
from google import genai

from app.core.config import settings
from app.schemas.ai import AIAction


SYSTEM_INSTRUCTIONS: dict[AIAction, str] = {
    "chat": (
        "You are TalentSphere AI, a practical career assistant. "
        "Answer clearly, accurately, and concisely. Do not invent user facts. "
        "Use the supplied context when present."
    ),
    "learning_support": (
        "You are TalentSphere's learning and career support assistant. "
        "Give actionable study, skill-building, and career guidance grounded in the supplied user context. "
        "Do not claim certainty about career outcomes."
    ),
    "resume_analysis": (
        "You are an ATS-aware resume reviewer. Analyze only the supplied resume and profile context. "
        "Return practical strengths, weaknesses, missing evidence, role alignment, and concrete improvements. "
        "Never invent experience, projects, skills, or achievements."
    ),
    "career_recommendation": (
        "You are a career guidance specialist. Recommend realistic roles and next steps using only the supplied profile, "
        "assessment, and skill-gap context. Explain the reasoning briefly and distinguish guidance from guarantees."
    ),
    "mock_interview": (
        "You are a professional interview coach. Review the candidate's answer against the supplied question and role. "
        "Give concise feedback on relevance, structure, technical/content quality, clarity, and one concrete improvement. "
        "Do not make hiring decisions or invent candidate experience."
    ),
}


@lru_cache(maxsize=1)
def _client() -> genai.Client:
    if not settings.GEMINI_API_KEY.strip():
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="Gemini AI is not configured. Set GEMINI_API_KEY in the backend environment.",
        )
    return genai.Client(api_key=settings.GEMINI_API_KEY)


def generate_ai_response(
    *,
    action: AIAction,
    prompt: str,
    context: str | None = None,
) -> str:
    client = _client()

    context_block = context.strip() if context else "No additional user context was supplied."
    user_prompt = (
        f"{SYSTEM_INSTRUCTIONS[action]}\n\n"
        f"USER CONTEXT:\n{context_block}\n\n"
        f"REQUEST:\n{prompt.strip()}"
    )

    try:
        response = client.models.generate_content(
            model=settings.GEMINI_MODEL,
            contents=user_prompt,
        )
    except Exception as exc:
        raise HTTPException(
            status_code=status.HTTP_502_BAD_GATEWAY,
            detail="Gemini AI request failed. Please try again.",
        ) from exc

    text = (response.text or "").strip()
    if not text:
        raise HTTPException(
            status_code=status.HTTP_502_BAD_GATEWAY,
            detail="Gemini AI returned an empty response.",
        )

    return text
