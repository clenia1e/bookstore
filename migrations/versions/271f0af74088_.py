"""empty message

Revision ID: 271f0af74088
Revises: e512345095f9
Create Date: 2021-06-05 09:55:42.907485

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '271f0af74088'
down_revision = 'e512345095f9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('books', sa.Column('category_id', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('books', 'category_id')
    # ### end Alembic commands ###