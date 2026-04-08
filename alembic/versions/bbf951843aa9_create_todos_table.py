"""create todos table

Revision ID: bbf951843aa9
Revises: 588a0d0a781e
Create Date: 2026-04-08 13:49:17.840540

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'bbf951843aa9'
down_revision: Union[str, Sequence[str], None] = '588a0d0a781e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def upgrade():
    op.create_table(
        'todos',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('task', sa.String(length=200))
    )

def downgrade():
    op.drop_table('todos')
