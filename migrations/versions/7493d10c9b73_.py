"""empty message

Revision ID: 7493d10c9b73
Revises: 5b8631c25a7b
Create Date: 2022-08-26 15:42:47.821837

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7493d10c9b73'
down_revision = '5b8631c25a7b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('address', sa.Column('lastStatus', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('address', 'lastStatus')
    # ### end Alembic commands ###
