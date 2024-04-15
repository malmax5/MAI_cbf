"""user_stats

Revision ID: 85c0d99efd54
Revises: 
Create Date: 2024-04-16 01:40:55.885113

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '85c0d99efd54'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'user_stats',
        sa.Column('id', sa.BigInteger(), nullable=False, primary_key=True, autoincrement=True),
        sa.Column('subs', sa.JSON, nullable=True),
        sa.Column('articles', sa.JSON(), nullable=True),
    )
    op.create_table(
        'user_publics',
        sa.Column('id', sa.BigInteger(), nullable=False, primary_key=True, autoincrement=True),
        sa.Column('user_id', sa.BigInteger(), nullable=False),
        sa.Column('book_id', sa.Integer(), nullable=False),
        sa.Column('article_name', sa.String(50), nullable=False),
        sa.Column('text', sa.Text(), nullable=False),
        sa.Column('likes', sa.Integer(), default=0),
        sa.Column('viewed', sa.Integer(), default=0),
    )
    op.create_foreign_key(
        'fk_user_publics_user_stats_id',
        'user_publics',
        'user_stats',
        ['user_id'],
        ['id'],
        ondelete='CASCADE'
    )


def downgrade() -> None:
    op.drop_table('user_stats')
    op.drop_table('user_publics')
