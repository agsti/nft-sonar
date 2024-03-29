"""your migration description

Revision ID: 306c4571ab00
Revises: b91257b99d65
Create Date: 2022-01-05 10:58:12.658936

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '306c4571ab00'
down_revision = 'b91257b99d65'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'collections', ['slug'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'collections', type_='unique')
    # ### end Alembic commands ###
