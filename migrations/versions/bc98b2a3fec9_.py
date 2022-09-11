"""empty message

Revision ID: bc98b2a3fec9
Revises: 7493d10c9b73
Create Date: 2022-08-27 16:28:11.337538

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bc98b2a3fec9'
down_revision = '7493d10c9b73'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_address_timestamp', table_name='address')
    op.drop_column('address', 'timestamp')
    op.drop_index('ix_user_email', table_name='user')
    op.drop_column('user', 'email')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('email', sa.VARCHAR(length=120), nullable=True))
    op.create_index('ix_user_email', 'user', ['email'], unique=False)
    op.add_column('address', sa.Column('timestamp', sa.DATETIME(), nullable=True))
    op.create_index('ix_address_timestamp', 'address', ['timestamp'], unique=False)
    # ### end Alembic commands ###
