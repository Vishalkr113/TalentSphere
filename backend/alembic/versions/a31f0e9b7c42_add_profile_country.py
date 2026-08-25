"""add country to profile

Revision ID: a31f0e9b7c42
Revises: bf1c6f7e2a10
"""
from alembic import op
import sqlalchemy as sa

revision = "a31f0e9b7c42"
down_revision = "bf1c6f7e2a10"
branch_labels = None
depends_on = None

def upgrade() -> None:
    op.add_column("profiles", sa.Column("country", sa.String(), nullable=True))

def downgrade() -> None:
    op.drop_column("profiles", "country")
