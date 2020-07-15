"""empty message

Revision ID: d5305bfd2309
Revises: 3784ad0348c8
Create Date: 2020-07-15 02:12:21.782683

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd5305bfd2309'
down_revision = '3784ad0348c8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Artist', sa.Column('created_at', sa.DateTime(), nullable=True))
    op.add_column('Venue', sa.Column('created_at', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('Venue', 'created_at')
    op.drop_column('Artist', 'created_at')
    # ### end Alembic commands ###