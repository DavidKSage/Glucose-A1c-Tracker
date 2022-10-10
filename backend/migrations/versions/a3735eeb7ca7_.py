"""empty message

Revision ID: a3735eeb7ca7
Revises: 
Create Date: 2022-08-13 18:34:03.427942

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a3735eeb7ca7'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('reading',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=35), nullable=False),
    sa.Column('my_reading', sa.Integer(), nullable=False),
    sa.Column('reading_date', sa.Date(), nullable=False),
    sa.Column('reading_time', sa.Time(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('fname', sa.String(length=25), nullable=False),
    sa.Column('lname', sa.String(length=30), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('username', sa.String(length=35), nullable=False),
    sa.Column('pwdhash', sa.String(length=128), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    op.drop_table('reading')
    # ### end Alembic commands ###