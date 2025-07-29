"""posts table creation

Revision ID: 1edcee5e2092
Revises:
Create Date: 2025-07-28 13:05:53.156374

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "1edcee5e2092"
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "posts",
        sa.Column("id", sa.Integer(), primary_key=True, nullable=False, index=True),
        sa.Column("title", sa.String(200), nullable=False),
        sa.Column("content", sa.String(300), nullable=False),
        sa.Column("published", sa.Boolean(), server_default="1", nullable=False),
        sa.Column(
            "created_at",
            sa.TIMESTAMP(timezone=True),
            nullable=False,
            server_default=sa.text("now()"),
        ),
    )

    """Upgrade schema."""
    pass


def downgrade() -> None:
    op.drop_table("posts")
    """Downgrade schema."""
    pass
