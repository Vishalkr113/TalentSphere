"""upgrade_profile_model

Revision ID: c0f0d2ea1cb7
Revises: 523d0b64bcc4
Create Date: 2026-07-30 23:14:01.421031

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "c0f0d2ea1cb7"
down_revision: Union[str, Sequence[str], None] = "523d0b64bcc4"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""

    with op.batch_alter_table(
        "profiles",
        schema=None,
    ) as batch_op:

        # Add nullable first because old rows already exist
        batch_op.add_column(
            sa.Column(
                "created_at",
                sa.DateTime(),
                nullable=True,
            )
        )

        batch_op.add_column(
            sa.Column(
                "updated_at",
                sa.DateTime(),
                nullable=True,
            )
        )

        batch_op.alter_column(
            "date_of_birth",
            existing_type=sa.VARCHAR(),
            type_=sa.Date(),
            existing_nullable=True,
        )

        batch_op.alter_column(
            "skills",
            existing_type=sa.TEXT(),
            type_=sa.JSON(),
            existing_nullable=True,
        )

        batch_op.alter_column(
            "interests",
            existing_type=sa.TEXT(),
            type_=sa.JSON(),
            existing_nullable=True,
        )


    # Fill old existing records
    op.execute(
        """
        UPDATE profiles
        SET 
            created_at = CURRENT_TIMESTAMP,
            updated_at = CURRENT_TIMESTAMP
        WHERE created_at IS NULL
        """
    )


    # Make future records consistent
    with op.batch_alter_table(
        "profiles",
        schema=None,
    ) as batch_op:

        batch_op.alter_column(
            "created_at",
            existing_type=sa.DateTime(),
            nullable=False,
        )

        batch_op.alter_column(
            "updated_at",
            existing_type=sa.DateTime(),
            nullable=False,
        )


def downgrade() -> None:
    """Downgrade schema."""

    with op.batch_alter_table(
        "profiles",
        schema=None,
    ) as batch_op:

        batch_op.alter_column(
            "interests",
            existing_type=sa.JSON(),
            type_=sa.TEXT(),
            existing_nullable=True,
        )

        batch_op.alter_column(
            "skills",
            existing_type=sa.JSON(),
            type_=sa.TEXT(),
            existing_nullable=True,
        )

        batch_op.alter_column(
            "date_of_birth",
            existing_type=sa.Date(),
            type_=sa.VARCHAR(),
            existing_nullable=True,
        )

        batch_op.drop_column("updated_at")
        batch_op.drop_column("created_at")