"""added league table

Revision ID: abfd09eb16c1
Revises: 
Create Date: 2022-11-06 13:40:02.560700

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'abfd09eb16c1'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('leagues',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=200), nullable=False),
    sa.Column('type', sa.String(length=50), nullable=False),
    sa.Column('country_name', sa.String(length=50), nullable=False),
    sa.Column('country_code', sa.String(length=3), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('leagues')
    # ### end Alembic commands ###
