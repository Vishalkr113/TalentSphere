import random

from .schemas import Question


def shuffle_questions(questions: list[Question]) -> list[Question]:
    """
    Return a shuffled copy of the question list.
    """
    shuffled = questions.copy()
    random.shuffle(shuffled)
    return shuffled


def shuffle_options(question: Question) -> Question:
    """
    Return a copy of the question with shuffled options.
    """
    options = question.options.copy()
    random.shuffle(options)

    return question.model_copy(
        update={
            "options": options
        }
    )


def group_by_topic(
    questions: list[Question],
) -> dict[str, list[Question]]:
    grouped: dict[str, list[Question]] = {}

    for question in questions:
        key = question.topic.value
        grouped.setdefault(key, []).append(question)

    return grouped


def group_by_difficulty(
    questions: list[Question],
) -> dict[str, list[Question]]:
    grouped: dict[str, list[Question]] = {}

    for question in questions:
        key = question.difficulty.value
        grouped.setdefault(key, []).append(question)

    return grouped