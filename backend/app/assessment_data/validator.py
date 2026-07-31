from collections import Counter

from .schemas import Question


class QuestionValidator:
    @staticmethod
    def validate_question(question: Question) -> None:
        if len(question.options) != 4:
            raise ValueError(f"{question.id}: Question must have exactly 4 options.")

        if question.answer not in question.options:
            raise ValueError(
                f"{question.id}: Answer must exist in the options list."
            )

    @staticmethod
    def validate_question_bank(questions: list[Question]) -> None:
        if not questions:
            raise ValueError("Question bank is empty.")

        ids = [question.id for question in questions]

        duplicates = [
            question_id
            for question_id, count in Counter(ids).items()
            if count > 1
        ]

        if duplicates:
            raise ValueError(
                f"Duplicate Question IDs found: {', '.join(duplicates)}"
            )

        for question in questions:
            QuestionValidator.validate_question(question)