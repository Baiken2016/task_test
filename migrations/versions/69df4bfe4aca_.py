"""empty message

Revision ID: 69df4bfe4aca
Revises: 39e565d555ec
Create Date: 2023-09-19 14:58:51.371486

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '69df4bfe4aca'
down_revision: Union[str, None] = '39e565d555ec'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
