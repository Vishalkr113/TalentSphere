"""centralize role profile fields

Revision ID: 9b7c4d8e1a21
Revises: 48aca86a4697
Create Date: 2026-08-14

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

revision: str = "9b7c4d8e1a21"
down_revision: Union[str, Sequence[str], None] = "48aca86a4697"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    with op.batch_alter_table("profiles", schema=None) as batch_op:
        batch_op.add_column(sa.Column("university_name", sa.String(), nullable=True))
        batch_op.add_column(sa.Column("semester", sa.String(), nullable=True))
        batch_op.add_column(sa.Column("cgpa", sa.String(), nullable=True))
        batch_op.add_column(sa.Column("target_role", sa.String(), nullable=True))
        batch_op.add_column(sa.Column("board", sa.String(), nullable=True))
        batch_op.add_column(sa.Column("medium", sa.String(), nullable=True))
        batch_op.add_column(sa.Column("roll_number", sa.String(), nullable=True))
        batch_op.add_column(sa.Column("admission_year", sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column("percentage", sa.String(), nullable=True))
        batch_op.add_column(sa.Column("blood_group", sa.String(), nullable=True))
        batch_op.add_column(sa.Column("district", sa.String(), nullable=True))
        batch_op.add_column(sa.Column("pin_code", sa.String(), nullable=True))
        batch_op.add_column(sa.Column("parent_name", sa.String(), nullable=True))
        batch_op.add_column(sa.Column("parent_mobile", sa.String(), nullable=True))
        batch_op.add_column(sa.Column("parent_email", sa.String(), nullable=True))
        batch_op.add_column(sa.Column("parent_occupation", sa.String(), nullable=True))
        batch_op.add_column(sa.Column("favorite_subject", sa.String(), nullable=True))
        batch_op.add_column(sa.Column("weak_subject", sa.String(), nullable=True))
        batch_op.add_column(sa.Column("hobbies", sa.JSON(), nullable=True))
        batch_op.add_column(sa.Column("languages", sa.JSON(), nullable=True))
        batch_op.add_column(sa.Column("expected_salary", sa.String(), nullable=True))


def downgrade() -> None:
    with op.batch_alter_table("profiles", schema=None) as batch_op:
        for name in [
            "expected_salary", "languages", "hobbies", "weak_subject",
            "favorite_subject", "parent_occupation", "parent_email",
            "parent_mobile", "parent_name", "pin_code", "district",
            "blood_group", "percentage", "admission_year", "roll_number",
            "medium", "board", "target_role", "cgpa", "semester",
            "university_name",
        ]:
            batch_op.drop_column(name)
