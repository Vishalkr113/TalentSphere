from typing import Literal

from pydantic import BaseModel, Field


AIAction = Literal[
    "chat",
    "learning_support",
    "resume_analysis",
    "career_recommendation",
    "mock_interview",
]


class AIGenerateRequest(BaseModel):
    action: AIAction
    prompt: str = Field(min_length=1, max_length=12000)
    context: str | None = Field(default=None, max_length=16000)


class AIGenerateResponse(BaseModel):
    action: AIAction
    text: str
    model: str
