"""add_admin_table

Revision ID: 4931602d05b2
Revises: f65d515bf64a
Create Date: 2026-06-20 10:43:42.510978

"""
"""add_admin_table"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

revision = "4931602d05b2"
down_revision = "f65d515bf64a"
branch_labels = None
depends_on = None


def upgrade() -> None:

    op.create_table(
        "admins",
        sa.Column(
            "id",
            sa.Integer(),
            nullable=False,
        ),
        sa.Column(
            "email",
            sa.String(length=255),
            nullable=False,
        ),
        sa.Column(
            "hashed_password",
            sa.String(length=255),
            nullable=False,
        ),
        sa.Column(
            "is_active",
            sa.Boolean(),
            nullable=False,
            server_default="true",
        ),
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
        ),
        sa.PrimaryKeyConstraint("id"),
    )

    op.create_index(
        "ix_admins_id",
        "admins",
        ["id"],
    )

    op.create_index(
        "ix_admins_email",
        "admins",
        ["email"],
        unique=True,
    )


def downgrade() -> None:

    op.drop_index(
        "ix_admins_email",
        table_name="admins",
    )

    op.drop_index(
        "ix_admins_id",
        table_name="admins",
    )

    op.drop_table("admins")