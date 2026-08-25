"""
Assessment Question Validator

Validates all question banks before
database insertion.
"""


from app.assessment_data.schemas import Question



# =========================================================
# Required Fields
# =========================================================

REQUIRED_FIELDS = {

    "question_code",

    "question",

    "options",

    "answer",

    "difficulty",

    "topic",

    "question_type",

}



VALID_ANSWERS = {

    "A",
    "B",
    "C",
    "D",

}



# =========================================================
# Single Question Validation
# =========================================================

def validate_question(
    question: dict,
    index: int = 0,
) -> bool:


    missing_fields = [

        field

        for field in REQUIRED_FIELDS

        if field not in question

    ]


    if missing_fields:

        raise ValueError(

            f"Question #{index} missing fields: "
            f"{missing_fields}"

        )



    if not str(
        question["question"]
    ).strip():

        raise ValueError(

            f"Question #{index} has empty question text"

        )

# Check options count

    if len(question["options"]) != 4:

        raise ValueError(
            f"Question #{index} must have exactly 4 options"
        )


    if question["answer"] not in VALID_ANSWERS:

        raise ValueError(

            f"Question #{index} has invalid answer "
            f"{question['answer']}"

        )



    return True



# =========================================================
# Complete Bank Validation
# =========================================================

def validate_question_bank(
    questions: list[dict],
):


    if not isinstance(
        questions,
        list,
    ):

        raise TypeError(
            "Question bank must be a list"
        )



    codes = set()



    for index, question in enumerate(
        questions,
        start=1,
    ):


        validate_question(
            question,
            index,
        )


        code = question["question_code"]



        if code in codes:

            raise ValueError(

                f"Duplicate question code found: {code}"

            )


        codes.add(code)



    return True