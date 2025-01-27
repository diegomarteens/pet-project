"""empty message

Revision ID: fb12516ed7ff
Revises: 7a357fd2431a
Create Date: 2022-02-05 17:46:38.912540

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fb12516ed7ff'
down_revision = '7a357fd2431a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('pet_michrochip_key', 'pet', type_='unique')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint('pet_michrochip_key', 'pet', ['michrochip'])
    # ### end Alembic commands ###
