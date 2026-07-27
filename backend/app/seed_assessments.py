from app.assessment_data.aptitude_questions import (
    APTITUDE_QUESTIONS,
)
from app.assessment_data.coding_questions import (
    CODING_QUESTIONS,
)
from app.assessment_data.high_school.common_questions import (
    HIGH_SCHOOL_COMMON_QUESTIONS,
)
from app.assessment_data.high_school.class11_pcm_questions import (
    CLASS11_PCM_QUESTIONS,
)
from app.assessment_data.high_school.class11_pcb_questions import (
    CLASS11_PCB_QUESTIONS,
)
from app.db.database import SessionLocal
from app.models.assessment import AssessmentQuestion


# ---------------------------------------------------------
# Managed Assessment Question Banks
# ---------------------------------------------------------

QUESTIONS = (
    APTITUDE_QUESTIONS
    + CODING_QUESTIONS
    + HIGH_SCHOOL_COMMON_QUESTIONS
    + CLASS11_PCM_QUESTIONS
    + CLASS11_PCB_QUESTIONS
)


# ---------------------------------------------------------
# Fields Stored In AssessmentQuestion
# ---------------------------------------------------------

QUESTION_FIELDS = {
    "assessment_type",
    "question_text",
    "option_a",
    "option_b",
    "option_c",
    "option_d",
    "correct_answer",
    "explanation",
    "difficulty",
    "is_active",
    "user_role",
    "category",
    "skill",
    "student_class",
    "stream",
    "degree",
    "branch",
    "experience_level",
    "domain",
}


UPDATABLE_FIELDS = (
    "option_a",
    "option_b",
    "option_c",
    "option_d",
    "correct_answer",
    "explanation",
    "difficulty",
    "user_role",
    "category",
    "skill",
    "student_class",
    "stream",
    "degree",
    "branch",
    "experience_level",
    "domain",
)


# ---------------------------------------------------------
# Helpers
# ---------------------------------------------------------

def clean_question_data(
    question_data: dict,
) -> dict:
    """
    Keep only fields supported by AssessmentQuestion.

    This intentionally ignores conversion-only metadata such
    as frontend_id.
    """
    return {
        key: value
        for key, value in question_data.items()
        if key in QUESTION_FIELDS
    }


def validate_question_banks():
    expected_total = 285

    if len(QUESTIONS) != expected_total:
        raise ValueError(
            "Managed assessment bank must contain "
            f"exactly {expected_total} questions. "
            f"Found: {len(QUESTIONS)}"
        )

    required_fields = {
        "assessment_type",
        "question_text",
        "option_a",
        "option_b",
        "option_c",
        "option_d",
        "correct_answer",
        "difficulty",
    }

    valid_answers = {
        "A",
        "B",
        "C",
        "D",
    }

    for index, question in enumerate(
        QUESTIONS,
        start=1,
    ):
        missing_fields = [
            field
            for field in required_fields
            if field not in question
        ]

        if missing_fields:
            raise ValueError(
                f"Question #{index} is missing "
                f"required fields: {missing_fields}"
            )

        if not str(
            question["question_text"]
        ).strip():
            raise ValueError(
                f"Question #{index} has empty text"
            )

        if (
            question["correct_answer"]
            not in valid_answers
        ):
            raise ValueError(
                f"Question #{index} has invalid "
                "correct_answer"
            )


# ---------------------------------------------------------
# Seed Assessment Questions
# ---------------------------------------------------------

def seed_assessment_questions():
    validate_question_banks()

    db = SessionLocal()

    try:
        added = 0
        updated = 0
        unchanged = 0

        for raw_question_data in QUESTIONS:
            question_data = clean_question_data(
                raw_question_data
            )

            existing_question = (
                db.query(AssessmentQuestion)
                .filter(
                    AssessmentQuestion.assessment_type
                    == question_data[
                        "assessment_type"
                    ],
                    AssessmentQuestion.question_text
                    == question_data[
                        "question_text"
                    ],
                )
                .first()
            )

            if existing_question is None:
                question = AssessmentQuestion(
                    **question_data
                )

                db.add(question)
                added += 1
                continue

            changed = False

            for field in UPDATABLE_FIELDS:
                if field not in question_data:
                    continue

                new_value = question_data[field]

                old_value = getattr(
                    existing_question,
                    field,
                )

                if old_value != new_value:
                    setattr(
                        existing_question,
                        field,
                        new_value,
                    )
                    changed = True

            desired_active = question_data.get(
                "is_active",
                True,
            )

            if (
                existing_question.is_active
                != desired_active
            ):
                existing_question.is_active = (
                    desired_active
                )
                changed = True

            if changed:
                updated += 1
            else:
                unchanged += 1

        db.commit()

        assessment_types = sorted(
            {
                question["assessment_type"]
                for question in QUESTIONS
            }
        )

        counts = {}

        for assessment_type in assessment_types:
            counts[assessment_type] = (
                db.query(AssessmentQuestion)
                .filter(
                    AssessmentQuestion.assessment_type
                    == assessment_type
                )
                .count()
            )

        print(
            "Assessment questions seeded successfully."
        )
        print(f"Added: {added}")
        print(f"Updated: {updated}")
        print(f"Unchanged: {unchanged}")

        print("\nQuestion counts:")

        total = 0

        for assessment_type, count in counts.items():
            print(
                f"{assessment_type}: {count}"
            )
            total += count

        print(
            f"Total managed assessment questions: "
            f"{total}"
        )

    except Exception:
        db.rollback()
        raise

    finally:
        db.close()


if __name__ == "__main__":
    seed_assessment_questions()