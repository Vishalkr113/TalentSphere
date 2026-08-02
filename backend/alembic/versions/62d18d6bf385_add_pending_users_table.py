"""add pending users table

Revision ID: 62d18d6bf385
Revises: 6ecf08d2d7ed
Create Date: 2026-08-01
"""

from alembic import op
import sqlalchemy as sa


revision = "62d18d6bf385"

down_revision = "6ecf08d2d7ed"

branch_labels = None

depends_on = None



def upgrade():


    # Create pending users table

    op.create_table(

        "pending_users",

        sa.Column(
            "id",
            sa.Integer(),
            nullable=False
        ),

        sa.Column(
            "full_name",
            sa.String(),
            nullable=False
        ),

        sa.Column(
            "email",
            sa.String(),
            nullable=False
        ),

        sa.Column(
            "hashed_password",
            sa.String(),
            nullable=False
        ),

        sa.Column(
            "role",
            sa.String(),
            nullable=False
        ),

        sa.Column(
            "created_at",
            sa.DateTime(),
            nullable=True
        ),

        sa.PrimaryKeyConstraint(
            "id"
        ),

        sa.UniqueConstraint(
            "email"
        )

    )



    # Add pending user reference in OTP table

    op.add_column(

        "email_otps",

        sa.Column(
            "pending_user_id",
            sa.Integer(),
            nullable=True
        )

    )



    op.create_index(

        "ix_email_otps_pending_user_id",

        "email_otps",

        ["pending_user_id"]

    )





def downgrade():


    op.drop_index(
        "ix_email_otps_pending_user_id",
        table_name="email_otps"
    )


    op.drop_column(
        "email_otps",
        "pending_user_id"
    )


    op.drop_table(
        "pending_users"
    )