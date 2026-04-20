"""create posts table

Revision ID: eaa13d636794
Revises: 
Create Date: 2026-04-16 15:59:24.301399

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'eaa13d636794'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table('posts',sa.Column('id',sa.Integer(),nullable=False,primary_key=True),
        sa.Column('title',sa.String(),nullable=False),
    )
    pass

 
def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table('posts')
    pass
