"""upgrade assessment question bank structure

Revision ID: a8d96599dccc
Revises: 47d61aa81928
Create Date: 2026-08-01
"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = "a8d96599dccc"

down_revision: Union[str, Sequence[str], None] = "47d61aa81928"

branch_labels = None

depends_on = None


def upgrade() -> None:
    """
    Add new question bank management fields.
    """

    with op.batch_alter_table(
        "assessment_questions"
    ) as batch_op:

        # Temporary nullable fields
        batch_op.add_column(
            sa.Column(
                "question_code",
                sa.String(length=100),
                nullable=True,
            )
        )

        batch_op.add_column(
            sa.Column(
                "topic",
                sa.String(length=100),
                nullable=True,
            )
        )

        batch_op.add_column(
            sa.Column(
                "sub_topic",
                sa.String(length=100),
                nullable=True,
            )
        )

        batch_op.add_column(
            sa.Column(
                "language",
                sa.String(length=50),
                nullable=True,
            )
        )

        batch_op.add_column(
            sa.Column(
                "question_type",
                sa.String(length=50),
                nullable=True,
                server_default="mcq",
            )
        )

        batch_op.add_column(
            sa.Column(
                "updated_at",
                sa.DateTime(timezone=True),
                nullable=True,
            )
        )


    # Fill existing rows temporarily
    op.execute(
        """
        UPDATE assessment_questions
        SET
            question_code = 'OLD-' || id,
            question_type = 'mcq'
        """
    )


    # Create indexes after data exists

    with op.batch_alter_table(
        "assessment_questions"
    ) as batch_op:

        batch_op.create_index(
            "idx_question_filter",
            [
                "assessment_type",
                "category",
                "difficulty",
            ],
            unique=False,
        )

        batch_op.create_index(
            "ix_assessment_questions_question_code",
            [
                "question_code"
            ],
            unique=True,
        )

        batch_op.create_index(
            "ix_assessment_questions_language",
            [
                "language"
            ],
            unique=False,
        )

        batch_op.create_index(
            "ix_assessment_questions_topic",
            [
                "topic"
            ],
            unique=False,
        )

        batch_op.create_index(
            "ix_assessment_questions_sub_topic",
            [
                "sub_topic"
            ],
            unique=False,
        )

        batch_op.create_index(
            "ix_assessment_questions_question_type",
            [
                "question_type"
            ],
            unique=False,
        )



def downgrade() -> None:

    with op.batch_alter_table(
        "assessment_questions"
    ) as batch_op:

        batch_op.drop_index(
            "ix_assessment_questions_question_type"
        )

        batch_op.drop_index(
            "ix_assessment_questions_sub_topic"
        )

        batch_op.drop_index(
            "ix_assessment_questions_topic"
        )

        batch_op.drop_index(
            "ix_assessment_questions_language"
        )

        batch_op.drop_index(
            "ix_assessment_questions_question_code"
        )

        batch_op.drop_index(
            "idx_question_filter"
        )


        batch_op.drop_column(
            "updated_at"
        )

        batch_op.drop_column(
            "question_type"
        )

        batch_op.drop_column(
            "language"
        )

        batch_op.drop_column(
            "sub_topic"
        )

        batch_op.drop_column(
            "topic"
        )

        batch_op.drop_column(
            "question_code"
        )