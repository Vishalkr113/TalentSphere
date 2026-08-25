"""clear old assessment question bank

Revision ID: 6ecf08d2d7ed
Revises: a8d96599dccc
Create Date: 2026-08-01
"""

from typing import Sequence, Union

from alembic import op


revision: str = "6ecf08d2d7ed"

down_revision: Union[str, Sequence[str], None] = "a8d96599dccc"

branch_labels = None

depends_on = None


def upgrade() -> None:
    """
    Remove old temporary assessment questions.
    New question bank will be added through
    final roadmap based system.
    """

    op.execute(
        """
        DELETE FROM assessment_questions
        """
    )


def downgrade() -> None:
    """
    Old questions are intentionally not restored.
    """
    pass