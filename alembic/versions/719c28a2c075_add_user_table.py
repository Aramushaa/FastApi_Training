"""add user table

Revision ID: 719c28a2c075
Revises: 91aadd18912a
Create Date: 2026-04-18 04:44:19.231226

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '719c28a2c075'
down_revision: Union[str, Sequence[str], None] = '91aadd18912a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table('users',sa.Column('id',sa.Integer(),nullable=False,primary_key=True),
        sa.Column('email',sa.String(),nullable=False,unique=True),
        sa.Column('password',sa.String(),nullable=False),
        sa.Column('created_at',sa.TIMESTAMP(timezone=True),nullable=False,server_default=sa.text('now()')),
    )
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table('users')
    pass
