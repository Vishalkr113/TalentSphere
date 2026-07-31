from typing import List

from pydantic import BaseModel, Field

from .enums import Difficulty, QuestionType, Topic


class Question(BaseModel):
    id: str = Field(..., min_length=1)
    question: str = Field(..., min_length=5)

    options: List[str] = Field(
        ...,
        min_length=4,
        max_length=4,
    )

    answer: str

    difficulty: Difficulty
    question_type: QuestionType
    topic: Topic

    explanation: str = ""
    marks: int = 1
    is_active: bool = True

    class Config:
        frozen = True