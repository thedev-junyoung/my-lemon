"""Remove unique constraint from name

Revision ID: de28faa5494e
Revises: 0c4874febcf5
Create Date: 2024-06-10 16:24:35.585625

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'de28faa5494e'
down_revision: Union[str, None] = '0c4874febcf5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_users_name', table_name='users')
    op.create_index(op.f('ix_users_name'), 'users', ['name'], unique=False)

    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_users_name'), table_name='users')
    op.create_index('ix_users_name', 'users', ['name'], unique=True)
    # ### end Alembic commands ###