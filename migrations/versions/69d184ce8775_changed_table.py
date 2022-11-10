"""changed table

Revision ID: 69d184ce8775
Revises: b50f1eb1aac6
Create Date: 2022-11-09 17:38:00.869304

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '69d184ce8775'
down_revision = 'b50f1eb1aac6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('task', sa.Column('goal_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'task', 'goal', ['goal_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'task', type_='foreignkey')
    op.drop_column('task', 'goal_id')
    # ### end Alembic commands ###
