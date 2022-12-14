"""empty message

Revision ID: caf73d547c77
Revises: f67aeb5498eb
Create Date: 2022-08-30 12:29:03.570953

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'caf73d547c77'
down_revision = 'f67aeb5498eb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'last_seen')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('last_seen', sa.DATETIME(), nullable=True))
    # ### end Alembic commands ###
