"""
Assessment Question Seeder

Loads questions from assessment_data loader,
validates them and inserts into database.
"""


from app.db.database import SessionLocal

from app.models.assessment import (
    AssessmentQuestion,
)

from app.assessment_data.loader import (
    get_all_questions,
)

from app.assessment_data.validator import (
    validate_question_bank,
)


# =========================================================
# Assessment Type Mapper
# =========================================================


def get_assessment_type(question):

    code = question.question_code.upper()


    # Aptitude
    if code.startswith("APT-"):
        return "college_aptitude"


    # Coding
    if code.startswith("COD-"):
        return "college_coding"


    # DSA
    if code.startswith("DSA-"):
        return "college_coding"


    # High School Foundation
    if code.startswith("HS-COMMON"):
        return "high_school_foundation"


    # High School PCM
    if code.startswith("HS-PCM"):
        return "high_school_pcm"


    # High School PCB
    if code.startswith("HS-PCB"):
        return "high_school_pcb"


    # High School Commerce
    if code.startswith("HS-COM"):
        return "high_school_commerce"


    # High School Arts
    if code.startswith("HS-ART"):
        return "high_school_arts"


    # Reasoning
    if code.startswith("REA-"):
        return "reasoning"


    # Default

    return "aptitude"


# =========================================================
# Question Category Mapper
# =========================================================

def get_question_category(question):

    code = question.question_code.upper()


    if code.startswith("HS-PCM"):
        return "math"


    if code.startswith("HS-PCB"):
        return "science"


    if code.startswith("HS-COMMON"):
        return "science"


    if code.startswith("HS-COM"):
        return "commerce"


    if code.startswith("HS-ART"):
        return "arts"

    return getattr(
        question,
        "category",
        None,
    )




# =========================================================
# Convert Question Schema
# To Database Format
# =========================================================


def prepare_question_data(question):


    options = question.options or []


    return {


        "question_code":
            question.question_code,


        "assessment_type":
            get_assessment_type(question),



        "question_text":
            question.question,



        "option_a":
            options[0]
            if len(options) > 0
            else None,


        "option_b":
            options[1]
            if len(options) > 1
            else None,


        "option_c":
            options[2]
            if len(options) > 2
            else None,


        "option_d":
            options[3]
            if len(options) > 3
            else None,



        "correct_answer":
            question.answer,



        "explanation":
            question.explanation,



        "difficulty":
            question.difficulty,



        "category":
            get_question_category(question),


        "topic":
            question.topic,



        "sub_topic":
            getattr(
                question,
                "sub_topic",
                None,
            ),



        "skill":
            getattr(
                question,
                "skill",
                None,
            ),



        "language":
            getattr(
                question,
                "language",
                None,
            ),



        "question_type":
            question.question_type,



        "user_role":
            getattr(
                question,
                "user_role",
                None,
            ),



        "student_class":
            getattr(
                question,
                "student_class",
                None,
            ),



        "stream":
            getattr(
                question,
                "stream",
                None,
            ),



        "degree":
            getattr(
                question,
                "degree",
                None,
            ),



        "branch":
            getattr(
                question,
                "branch",
                None,
            ),



        "experience_level":
            getattr(
                question,
                "experience_level",
                None,
            ),



        "domain":
            getattr(
                question,
                "domain",
                None,
            ),



        "is_active":
            question.is_active,

    }





# =========================================================
# Seed Function
# =========================================================


def seed_assessment_questions():


    questions = get_all_questions()


    if not questions:

        print(
            "No assessment questions found."
        )

        return



    # Validation before insert

    raw_questions = [

        question.model_dump()

        for question in questions

    ]


    validate_question_bank(
        raw_questions
    )



    db = SessionLocal()


    try:

        added = 0

        updated = 0



        for question in questions:


            data = prepare_question_data(
                question
            )



            existing = (

                db.query(
                    AssessmentQuestion
                )

                .filter(

                    AssessmentQuestion.question_code
                    ==
                    data["question_code"]

                )

                .first()

            )



            if existing:


                for key, value in data.items():

                    setattr(
                        existing,
                        key,
                        value,
                    )


                updated += 1



            else:


                db.add(

                    AssessmentQuestion(
                        **data
                    )

                )


                added += 1



        db.commit()



        print(
            "Assessment question seed completed."
        )

        print(
            f"Added: {added}"
        )

        print(
            f"Updated: {updated}"
        )

        print(
            f"Total: {len(questions)}"
        )



    except Exception as e:


        db.rollback()

        raise e



    finally:

        db.close()


