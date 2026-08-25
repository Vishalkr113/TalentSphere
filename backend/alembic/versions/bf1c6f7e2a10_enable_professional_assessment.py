"""Enable the professional skill assessment question bank.

Revision ID: bf1c6f7e2a10
Revises: 9b7c4d8e1a21
"""
from alembic import op
import sqlalchemy as sa

revision = "bf1c6f7e2a10"
down_revision = "9b7c4d8e1a21"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.execute(
        sa.text(
            "UPDATE assessment_questions "
            "SET assessment_type = 'professional_skill', user_role = 'working_professional' "
            "WHERE question_code LIKE 'PROFESSIONAL-%'"
        )
    )


def downgrade() -> None:
    op.execute(
        sa.text(
            "UPDATE assessment_questions "
            "SET assessment_type = 'aptitude', user_role = NULL "
            "WHERE question_code LIKE 'PROFESSIONAL-%'"
        )
    )
