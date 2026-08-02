"""fix email otp pending user

Revision ID: 48aca86a4697
Revises: 62d18d6bf385
Create Date: 2026-08-01

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers
revision: str = "48aca86a4697"
down_revision: Union[str, None] = "62d18d6bf385"
branch_labels = None
depends_on = None


def upgrade() -> None:

    # =====================================================
    # EMAIL OTP TABLE FIX ONLY
    # =====================================================

    with op.batch_alter_table(
        "email_otps"
    ) as batch_op:

        # user_id optional for pending users flow
        batch_op.alter_column(
            "user_id",
            existing_type=sa.Integer(),
            nullable=True,
        )


    # =====================================================
    # PENDING USERS INDEXES
    # =====================================================

    op.create_index(
        "ix_pending_users_email",
        "pending_users",
        ["email"],
        unique=False,
    )


    op.create_index(
        "ix_pending_users_id",
        "pending_users",
        ["id"],
        unique=False,
    )



def downgrade() -> None:


    # remove indexes

    op.drop_index(
        "ix_pending_users_email",
        table_name="pending_users",
    )


    op.drop_index(
        "ix_pending_users_id",
        table_name="pending_users",
    )


    with op.batch_alter_table(
        "email_otps"
    ) as batch_op:

        batch_op.alter_column(
            "user_id",
            existing_type=sa.Integer(),
            nullable=False,
        )