import random

from .enums import Difficulty, QuestionType, UserType
from .schemas import Question


class QuestionSelector:
    @staticmethod
    def select(
        questions: list[Question],
        question_type: QuestionType | None = None,
        difficulty: Difficulty | None = None,
        limit: int = 10,
        exclude_ids: set[str] | None = None,
    ) -> list[Question]:
        """
        Select random questions with optional filters.
        """

        exclude_ids = exclude_ids or set()

        filtered = [
            question
            for question in questions
            if question.is_active
            and question.id not in exclude_ids
            and (
                question_type is None
                or question.question_type == question_type
            )
            and (
                difficulty is None
                or question.difficulty == difficulty
            )
        ]

        random.shuffle(filtered)

        return filtered[:limit]

    @staticmethod
    def shuffle_options(question: Question) -> Question:
        options = question.options.copy()
        random.shuffle(options)

        return question.model_copy(
            update={
                "options": options
            }
        )

    @staticmethod
    def shuffle_questions(
        questions: list[Question],
    ) -> list[Question]:
        shuffled = questions.copy()
        random.shuffle(shuffled)
        return shuffled