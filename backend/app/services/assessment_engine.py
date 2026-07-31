"""
Assessment Engine

Responsibilities
----------------
- Load question banks
- Generate assessments
- Shuffle questions
- Shuffle options
- Remove answers
- Validate questions
"""

from __future__ import annotations

import random
import uuid
from copy import deepcopy
from typing import Any

from app.assessment_data.loader import QuestionLoader
from app.assessment_data.selector import shuffle_options
from app.assessment_data.validator import QuestionValidator

from .assessment_config import (
    ASSESSMENT_DURATION,
    QUESTION_COUNT,
    QUESTION_DISTRIBUTION,
    RULES,
)


class AssessmentEngine:
    """
    Core Assessment Engine
    """

    def __init__(self):

        self.loader = QuestionLoader()

        self.validator = QuestionValidator()

    # ----------------------------------------------------

    def generate_assessment(
        self,
        user_type: str,
        question_banks: dict[str, list],
        difficulty: str = "medium",
    ) -> dict[str, Any]:

        total_questions = QUESTION_COUNT[user_type]

        selected_questions = self._select_questions(
            user_type=user_type,
            question_banks=question_banks,
            total_questions=total_questions,
        )

        if RULES.shuffle_questions:
            random.shuffle(selected_questions)

        selected_questions = [
            self._prepare_question(q)
            for q in selected_questions
        ]

        return {
            "assessment_id": str(uuid.uuid4()),
            "user_type": user_type,
            "difficulty": difficulty,
            "duration": ASSESSMENT_DURATION[user_type],
            "total_questions": len(selected_questions),
            "questions": selected_questions,
        }

    # ----------------------------------------------------

    def _select_questions(
        self,
        user_type: str,
        question_banks: dict[str, list],
        total_questions: int,
    ) -> list:

        distribution = QUESTION_DISTRIBUTION[user_type]

        questions = []

        for section, count in distribution.items():

            bank = question_banks.get(section, [])

            if not bank:
                continue

            if len(bank) <= count:
                questions.extend(bank)

            else:
                questions.extend(
                    random.sample(bank, count)
                )

        questions = self._remove_duplicates(questions)

        return questions[:total_questions]

    # ----------------------------------------------------

    def _prepare_question(self, question):

        q = deepcopy(question)

        if RULES.shuffle_options:
            shuffle_options(q)

        if RULES.remove_answers:

            if hasattr(q, "correct_answer"):
                delattr(q, "correct_answer")

            if hasattr(q, "explanation"):
                delattr(q, "explanation")

        return q

    # ----------------------------------------------------

    def _remove_duplicates(self, questions):

        seen = set()

        unique = []

        for q in questions:

            qid = getattr(q, "question_id", None)

            if qid in seen:
                continue

            seen.add(qid)

            unique.append(q)

        return unique

    # ----------------------------------------------------

    def validate_question_bank(self, questions):

        if not RULES.validate_questions:
            return True

        self.validator.validate_question_bank(questions)

        return True