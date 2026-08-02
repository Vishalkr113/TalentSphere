"""
Assessment Question Loader

Single entry point for all question banks.

Flow:

Question Files
        |
        |
     loader.py
        |
        |
  ALL_QUESTIONS
        |
        |
 validator.py
        |
        |
 seed_assessments.py
        |
        |
 Database
"""


# =========================================================
# Imports
# =========================================================

from .aptitude_questions import (
    APTITUDE_QUESTIONS,
)

from .reasoning_questions import (
    REASONING_QUESTIONS,
)

from .coding_questions import (
    CODING_QUESTIONS,
)

from .dsa_questions import (
    DSA_QUESTIONS,
)



# =========================================================
# High School
# =========================================================

from .high_school.common_questions import (
    HIGH_SCHOOL_COMMON_QUESTIONS,
)

from .high_school.pcm_questions import (
    PCM_QUESTIONS,
)

from .high_school.pcb_questions import (
    PCB_QUESTIONS,
)

from .high_school.commerce_questions import (
    COMMERCE_QUESTIONS,
)

from .high_school.arts_questions import (
    ARTS_QUESTIONS,
)



# =========================================================
# College
# =========================================================

from .college.common_questions import (
    COLLEGE_COMMON_QUESTIONS,
)

from .college.technical_questions import (
    COLLEGE_TECHNICAL_QUESTIONS,
)

from .college.career_questions import (
    COLLEGE_CAREER_QUESTIONS,
)

from .college.dsa_questions import (
    COLLEGE_DSA_QUESTIONS,
)



# =========================================================
# Professional
# =========================================================

from .professional.common_questions import (
    PROFESSIONAL_COMMON_QUESTIONS,
)

from .professional.technical_questions import (
    PROFESSIONAL_TECHNICAL_QUESTIONS,
)

from .professional.situational_questions import (
    PROFESSIONAL_SITUATIONAL_QUESTIONS,
)


from .professional.dsa_questions import (
    PROFESSIONAL_DSA_QUESTIONS,
)



# =========================================================
# Language DSA
# =========================================================

from .languages.python_dsa import (
    PYTHON_DSA_QUESTIONS,
)

from .languages.java_dsa import (
    JAVA_DSA_QUESTIONS,
)

from .languages.cpp_dsa import (
    CPP_DSA_QUESTIONS,
)

from .languages.javascript_dsa import (
    JAVASCRIPT_DSA_QUESTIONS,
)

from .languages.c_dsa import (
    C_DSA_QUESTIONS,
)



# =========================================================
# Final Question Collection
# =========================================================


ALL_QUESTIONS = (

    APTITUDE_QUESTIONS

    + REASONING_QUESTIONS

    + CODING_QUESTIONS

    + DSA_QUESTIONS


    + HIGH_SCHOOL_COMMON_QUESTIONS
    + PCM_QUESTIONS
    + PCB_QUESTIONS
    + COMMERCE_QUESTIONS
    + ARTS_QUESTIONS


    + COLLEGE_COMMON_QUESTIONS
    + COLLEGE_TECHNICAL_QUESTIONS
    + COLLEGE_CAREER_QUESTIONS
    + COLLEGE_DSA_QUESTIONS


    + PROFESSIONAL_COMMON_QUESTIONS
    + PROFESSIONAL_TECHNICAL_QUESTIONS
    + PROFESSIONAL_SITUATIONAL_QUESTIONS
    + PROFESSIONAL_DSA_QUESTIONS


    + PYTHON_DSA_QUESTIONS
    + JAVA_DSA_QUESTIONS
    + CPP_DSA_QUESTIONS
    + JAVASCRIPT_DSA_QUESTIONS
    + C_DSA_QUESTIONS

)



# =========================================================
# Public Functions
# =========================================================


def get_all_questions():

    return ALL_QUESTIONS



def get_question_count():

    return len(
        ALL_QUESTIONS
    )



# =========================================================
# Convert Question Objects
# For Validator + Database
# =========================================================


def get_all_questions_as_dict():

    questions = []


    for question in ALL_QUESTIONS:

        if hasattr(
            question,
            "model_dump"
        ):

            questions.append(
                question.model_dump()
            )


        elif hasattr(
            question,
            "dict"
        ):

            questions.append(
                question.dict()
            )


        else:

            questions.append(
                question
            )


    return questions



# =========================================================
# Filter Questions
# =========================================================


def get_questions_by_type(
    assessment_type: str,
):

    return [

        question

        for question in ALL_QUESTIONS

        if getattr(
            question,
            "assessment_type",
            None
        )
        ==
        assessment_type

    ]



# =========================================================
# Category Filter
# =========================================================


def get_questions_by_category(
    category: str,
):

    return [

        question

        for question in ALL_QUESTIONS

        if getattr(
            question,
            "category",
            None
        )
        ==
        category

    ]



# =========================================================
# Topic Filter
# =========================================================


def get_questions_by_topic(
    topic: str,
):

    return [

        question

        for question in ALL_QUESTIONS

        if getattr(
            question,
            "topic",
            None
        )
        ==
        topic

    ]



# =========================================================
# Validation Helper
# =========================================================


def validate_all_questions():

    from .validator import (
        validate_question_bank
    )


    questions = get_all_questions_as_dict()


    return validate_question_bank(
        questions
    )