from typing import List, Optional

from pydantic import BaseModel, Field, model_validator

from .enums import (
    Difficulty,
    QuestionType,
    Topic,
)



class Question(BaseModel):
    """
    Master Question Bank Schema

    Supports:
    - New format:
        question
        options
        answer

    - Legacy format:
        question_text
        option_a
        option_b
        option_c
        option_d
        correct_answer
    """


    # =====================================================
    # Basic Identification
    # =====================================================

    question_code: str = Field(
        ...,
        min_length=3,
        max_length=100,
    )


    # =====================================================
    # Question Content
    # =====================================================

    question: Optional[str] = Field(
        default=None,
    )


    question_text: Optional[str] = Field(
        default=None,
    )


    # =====================================================
    # Options
    # =====================================================

    options: Optional[List[str]] = Field(
        default=None,
    )


    option_a: Optional[str] = None

    option_b: Optional[str] = None

    option_c: Optional[str] = None

    option_d: Optional[str] = None



    # =====================================================
    # Answer
    # =====================================================

    answer: Optional[str] = None


    correct_answer: Optional[str] = None



    # =====================================================
    # Metadata
    # =====================================================

    difficulty: Difficulty


    question_type: QuestionType


    topic: Topic



    category: Optional[str] = None


    assessment_type: Optional[str] = None



    skill: Optional[str] = None



    explanation: str = ""



    marks: int = Field(
        default=1,
        ge=1,
    )



    is_active: bool = True



    # =====================================================
    # Auto Conversion
    # =====================================================

    @model_validator(mode="after")
    def normalize_question(self):


        # -----------------------------
        # Convert question_text
        # -----------------------------

        if not self.question and self.question_text:

            object.__setattr__(
                self,
                "question",
                self.question_text
            )


        if not self.question_text and self.question:

            object.__setattr__(
                self,
                "question_text",
                self.question
            )



        # -----------------------------
        # Convert options
        # -----------------------------

        if not self.options:

            if all(
                [
                    self.option_a,
                    self.option_b,
                    self.option_c,
                    self.option_d,
                ]
            ):

                object.__setattr__(
                    self,
                    "options",
                    [
                        self.option_a,
                        self.option_b,
                        self.option_c,
                        self.option_d,
                    ]
                )



        # -----------------------------
        # Convert answer
        # -----------------------------

        if not self.answer and self.correct_answer:

            object.__setattr__(
                self,
                "answer",
                self.correct_answer
            )


        if not self.correct_answer and self.answer:

            object.__setattr__(
                self,
                "correct_answer",
                self.answer
            )



        # -----------------------------
        # Default category
        # -----------------------------

        if not self.category:

            object.__setattr__(
                self,
                "category",
                self.question_type
            )



        return self



    class Config:

        frozen = True

        use_enum_values = True