"""empty message

Revision ID: da393c79ca17
Revises: c1d102431563
Create Date: 2021-04-27 12:04:59.466234

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'da393c79ca17'
down_revision = 'c1d102431563'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Venue', sa.Column('city', sa.String(length=120), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('Venue', 'city')
    # ### end Alembic commands ###