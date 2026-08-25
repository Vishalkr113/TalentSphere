"""
Assessment Engine

Responsibilities
----------------
- Load question banks
- Generate assessments
- Select questions
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
    Core Assessment Generator
    """



    def __init__(self):

        self.validator = QuestionValidator()



    # --------------------------------------------------
    # Generate Assessment
    # --------------------------------------------------


    def generate_assessment(
        self,
        user_type: str,
        question_banks: dict[str,list],
        difficulty: str = "medium",
    ) -> dict[str,Any]:


        if user_type not in QUESTION_COUNT:

            raise ValueError(
                f"Unsupported user type: {user_type}"
            )


        total_questions = (
            QUESTION_COUNT[user_type]
        )


        selected_questions = (
            self._select_questions(
                user_type=user_type,
                question_banks=question_banks,
                total_questions=total_questions,
                difficulty=difficulty,
            )
        )


        if RULES.validate_questions:

            self.validate_question_bank(
                selected_questions
            )


        if RULES.shuffle_questions:

            random.shuffle(
                selected_questions
            )


        prepared_questions = [

            self._prepare_question(
                question
            )

            for question in selected_questions

        ]



        return {


            "assessment_id":
                str(uuid.uuid4()),


            "user_type":
                user_type,


            "difficulty":
                difficulty,


            "duration":
                ASSESSMENT_DURATION.get(
                    user_type,
                    30
                ),


            "total_questions":
                len(prepared_questions),


            "questions":
                prepared_questions,

        }



    # --------------------------------------------------
    # Select Questions
    # --------------------------------------------------


    def _select_questions(
        self,
        user_type: str,
        question_banks: dict[str,list],
        total_questions: int,
        difficulty: str,
    ) -> list:



        distribution = (
            QUESTION_DISTRIBUTION.get(
                user_type,
                {}
            )
        )


        selected = []



        for section,count in distribution.items():


            bank = question_banks.get(
                section,
                []
            )


            if not bank:

                continue



            filtered = [

                q

                for q in bank

                if getattr(
                    q,
                    "difficulty",
                    difficulty
                )
                == difficulty

            ]



            if not filtered:

                filtered = bank



            if len(filtered) <= count:

                selected.extend(
                    filtered
                )


            else:

                selected.extend(

                    random.sample(
                        filtered,
                        count
                    )

                )



        selected = (
            self._remove_duplicates(
                selected
            )
        )


        return selected[:total_questions]



    # --------------------------------------------------
    # Prepare Question
    # --------------------------------------------------


    def _prepare_question(
        self,
        question,
    ):


        q = deepcopy(
            question
        )


        if RULES.shuffle_options:

            shuffle_options(
                q
            )



        if RULES.remove_answers:


            if hasattr(
                q,
                "correct_answer"
            ):

                q.correct_answer = None



            if hasattr(
                q,
                "explanation"
            ):

                q.explanation = None



        return q



    # --------------------------------------------------
    # Remove Duplicate Questions
    # --------------------------------------------------


    def _remove_duplicates(
        self,
        questions,
    ):


        seen=set()

        unique=[]



        for question in questions:


            question_id = getattr(
                question,
                "id",
                None
            )



            if question_id in seen:

                continue



            seen.add(
                question_id
            )


            unique.append(
                question
            )



        return unique



    # --------------------------------------------------
    # Validate Question Bank
    # --------------------------------------------------


    def validate_question_bank(
        self,
        questions,
    ):


        self.validator.validate_question_bank(
            questions
        )


        return True