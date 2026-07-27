"""migrate legacy assessment types

Revision ID: 78cb62c1af83
Revises: a192d5b399e1

"""

from typing import Sequence, Union

from alembic import op


# revision identifiers, used by Alembic.
revision: str = "78cb62c1af83"
down_revision: Union[str, Sequence[str], None] = (
    "a192d5b399e1"
)
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # -----------------------------------------------------
    # Questions
    # -----------------------------------------------------

    op.execute(
        """
        UPDATE assessment_questions
        SET assessment_type = 'college_aptitude',
            user_role = 'college_student'
        WHERE assessment_type = 'aptitude'
        """
    )

    op.execute(
        """
        UPDATE assessment_questions
        SET assessment_type = 'college_coding',
            user_role = 'college_student'
        WHERE assessment_type = 'coding'
        """
    )

    # -----------------------------------------------------
    # Attempts
    # -----------------------------------------------------

    op.execute(
        """
        UPDATE assessment_attempts
        SET assessment_type = 'college_aptitude'
        WHERE assessment_type = 'aptitude'
        """
    )

    op.execute(
        """
        UPDATE assessment_attempts
        SET assessment_type = 'college_coding'
        WHERE assessment_type = 'coding'
        """
    )


def downgrade() -> None:
    # -----------------------------------------------------
    # Attempts
    # -----------------------------------------------------

    op.execute(
        """
        UPDATE assessment_attempts
        SET assessment_type = 'aptitude'
        WHERE assessment_type = 'college_aptitude'
        """
    )

    op.execute(
        """
        UPDATE assessment_attempts
        SET assessment_type = 'coding'
        WHERE assessment_type = 'college_coding'
        """
    )

    # -----------------------------------------------------
    # Questions
    # -----------------------------------------------------

    op.execute(
        """
        UPDATE assessment_questions
        SET assessment_type = 'aptitude',
            user_role = NULL
        WHERE assessment_type = 'college_aptitude'
          AND user_role = 'college_student'
        """
    )

    op.execute(
        """
        UPDATE assessment_questions
        SET assessment_type = 'coding',
            user_role = NULL
        WHERE assessment_type = 'college_coding'
          AND user_role = 'college_student'
        """
    )