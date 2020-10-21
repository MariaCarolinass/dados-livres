"""update tagging

Revision ID: bb0cd63a5e4f
Revises: 7dbd1ed198bc
Create Date: 2020-10-19 23:41:02.957814

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bb0cd63a5e4f'
down_revision = '7dbd1ed198bc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('tags', schema=None) as batch_op:
        batch_op.add_column(sa.Column('software_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(batch_op.f('fk_tags_software_id_software'), 'software', ['software_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('tags', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('fk_tags_software_id_software'), type_='foreignkey')
        batch_op.drop_column('software_id')

    # ### end Alembic commands ###
