"""initial baseline

Revision ID: 26662a50c62a
Revises: 
Create Date: 2026-07-27 01:43:24.761408

"""
from typing import Sequence, Union
from alembic import op
import sqlalchemy as sa

revision: str = "26662a50c62a"
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "users",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("full_name", sa.String(), nullable=False),
        sa.Column("email", sa.String(), nullable=False),
        sa.Column("hashed_password", sa.String(), nullable=False),
        sa.Column("role", sa.String(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index("ix_users_id", "users", ["id"], unique=False)
    op.create_index("ix_users_email", "users", ["email"], unique=True)

    op.create_table(
        "profiles",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("user_id", sa.Integer(), nullable=False),
        sa.Column("phone", sa.String(), nullable=True),
        sa.Column("date_of_birth", sa.String(), nullable=True),
        sa.Column("gender", sa.String(), nullable=True),
        sa.Column("city", sa.String(), nullable=True),
        sa.Column("state", sa.String(), nullable=True),
        sa.Column("college_name", sa.String(), nullable=True),
        sa.Column("course", sa.String(), nullable=True),
        sa.Column("branch", sa.String(), nullable=True),
        sa.Column("graduation_year", sa.Integer(), nullable=True),
        sa.Column("skills", sa.Text(), nullable=True),
        sa.Column("interests", sa.Text(), nullable=True),
        sa.Column("career_goal", sa.String(), nullable=True),
        sa.Column("github_url", sa.String(500), nullable=True),
        sa.Column("portfolio_url", sa.String(500), nullable=True),
        sa.Column("profile_photo", sa.String(), nullable=True),
        sa.Column("resume_url", sa.String(), nullable=True),
        sa.Column("profile_completion", sa.Integer(), nullable=False, server_default="0"),
        sa.ForeignKeyConstraint(["user_id"], ["users.id"]),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("user_id"),
    )
    op.create_index("ix_profiles_id", "profiles", ["id"], unique=False)
    op.create_index("ix_profiles_user_id", "profiles", ["user_id"], unique=True)


def downgrade() -> None:
    op.drop_index("ix_profiles_user_id", table_name="profiles")
    op.drop_index("ix_profiles_id", table_name="profiles")
    op.drop_table("profiles")
    op.drop_index("ix_users_email", table_name="users")
    op.drop_index("ix_users_id", table_name="users")
    op.drop_table("users")
