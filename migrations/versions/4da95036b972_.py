"""empty message

Revision ID: 4da95036b972
Revises: da393c79ca17
Create Date: 2021-04-27 12:22:49.198782

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4da95036b972'
down_revision = 'da393c79ca17'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('Venue', 'city')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Venue', sa.Column('city', sa.VARCHAR(length=120), autoincrement=False, nullable=False))
    # ### end Alembic commands ###
