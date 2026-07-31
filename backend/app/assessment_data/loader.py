from .schemas import Question
from .validator import QuestionValidator


class QuestionLoader:
    @staticmethod
    def load(*question_banks: list[Question]) -> list[Question]:
        """
        Merge multiple question banks into one validated list.
        """

        questions: list[Question] = []

        for bank in question_banks:
            questions.extend(bank)

        QuestionValidator.validate_question_bank(questions)

        return questions