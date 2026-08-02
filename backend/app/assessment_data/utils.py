"""
Assessment Question Utilities

Common helper functions for:
- Shuffle questions
- Shuffle options
- Group questions
"""


import random

from .schemas import Question



def shuffle_questions(
    questions: list[Question],
) -> list[Question]:
    """
    Return shuffled copy of questions.
    """

    shuffled = questions.copy()

    random.shuffle(
        shuffled
    )

    return shuffled



def shuffle_options(
    question: Question,
) -> Question:
    """
    Shuffle MCQ options while
    keeping Question schema format.
    """

    options = [

        question.option_a,

        question.option_b,

        question.option_c,

        question.option_d,

    ]


    random.shuffle(
        options
    )


    return question.model_copy(
        update={

            "option_a": options[0],

            "option_b": options[1],

            "option_c": options[2],

            "option_d": options[3],

        }
    )



def group_by_topic(
    questions: list[Question],
) -> dict[str, list[Question]]:


    grouped = {}


    for question in questions:

        key = question.topic


        grouped.setdefault(
            key,
            []
        ).append(
            question
        )


    return grouped



def group_by_difficulty(
    questions: list[Question],
) -> dict[str, list[Question]]:


    grouped = {}


    for question in questions:

        key = question.difficulty.value


        grouped.setdefault(
            key,
            []
        ).append(
            question
        )


    return grouped