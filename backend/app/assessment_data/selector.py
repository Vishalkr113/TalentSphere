"""
Assessment Question Selector

Responsible for:
- filtering
- random selection
- difficulty selection
- question type selection
"""


import random

from .enums import (
    Difficulty,
    QuestionType,
)

from .schemas import Question



class QuestionSelector:


    @staticmethod
    def select(
        questions: list[Question],

        question_type: QuestionType | None = None,

        difficulty: Difficulty | None = None,

        topic: str | None = None,

        limit: int = 10,

        exclude_codes: set[str] | None = None,

    ) -> list[Question]:


        exclude_codes = (
            exclude_codes
            or set()
        )


        filtered = [

            question

            for question in questions

            if question.is_active

            and question.question_code
            not in exclude_codes

            and (

                question_type is None

                or question.question_type == question_type

            )

            and (

                difficulty is None

                or question.difficulty == difficulty

            )

            and (

                topic is None

                or question.topic == topic

            )

        ]


        random.shuffle(
            filtered
        )


        return filtered[:limit]



    @staticmethod
    def shuffle_options(
        question: Question,
    ) -> Question:

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



    @staticmethod
    def shuffle_questions(
        questions: list[Question],
    ) -> list[Question]:


        shuffled = questions.copy()


        random.shuffle(
            shuffled
        )


        return shuffled