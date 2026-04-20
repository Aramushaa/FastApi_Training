"""add foreign-key to post table

Revision ID: cde30f9b7f42
Revises: 719c28a2c075
Create Date: 2026-04-18 04:53:58.936105

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'cde30f9b7f42'
down_revision: Union[str, Sequence[str], None] = '719c28a2c075'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('posts',sa.Column('owner_id',sa.Integer(),nullable=False))
    op.create_foreign_key('post_users_fk',source_table='posts',referent_table='users',local_cols=['owner_id'],remote_cols=['id'],ondelete='CASCADE')
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_constraint('post_users_fk',source_table='posts',type_='foreignkey')
    op.drop_column('posts','owner_id')
