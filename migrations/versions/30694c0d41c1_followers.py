"""followers

Revision ID: 30694c0d41c1
Revises: 0db832af24a6
Create Date: 2018-06-09 13:36:43.533636

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '30694c0d41c1'
down_revision = '0db832af24a6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('followers',
    sa.Column('follower_id', sa.Integer(), nullable=True),
    sa.Column('followed_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['followed_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['follower_id'], ['user.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('followers')
    # ### end Alembic commands ###
