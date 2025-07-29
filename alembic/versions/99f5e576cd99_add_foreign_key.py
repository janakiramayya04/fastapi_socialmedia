"""add foreign key

Revision ID: 99f5e576cd99
Revises: 72cc5988ab53
Create Date: 2025-07-28 13:17:27.840707

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "99f5e576cd99"
down_revision: Union[str, Sequence[str], None] = "72cc5988ab53"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column("posts", sa.Column("owner_id", sa.Integer(), nullable=False))
    op.create_foreign_key(
        "post_foreign_key",
        source_table="posts",
        referent_table="users",
        local_cols=["owner_id"],
        remote_cols=["id"],
        ondelete="CASCADE",
    )

    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_constraint("post_foreign_key", table_name="posts")
    op.drop_column("posts", "owner_id")
    pass
