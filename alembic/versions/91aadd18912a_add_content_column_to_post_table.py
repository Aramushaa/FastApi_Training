"""add content column to post table

Revision ID: 91aadd18912a
Revises: eaa13d636794
Create Date: 2026-04-17 23:06:24.549697

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '91aadd18912a'
down_revision: Union[str, Sequence[str], None] = 'eaa13d636794'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('posts',sa.Column('content',sa.String(),nullable=False))
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column('posts','content')
    pass
    pass
