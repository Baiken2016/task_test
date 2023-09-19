"""empty message

Revision ID: 820a77f9508b
Revises: 69df4bfe4aca
Create Date: 2023-09-19 15:04:41.905153

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '820a77f9508b'
down_revision: Union[str, None] = '69df4bfe4aca'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
