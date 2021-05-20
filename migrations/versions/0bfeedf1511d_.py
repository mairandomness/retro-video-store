"""empty message

Revision ID: 0bfeedf1511d
Revises: f80c639f651a
Create Date: 2021-05-19 21:09:06.565630

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0bfeedf1511d'
down_revision = 'f80c639f651a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('checked',
    sa.Column('customer_id', sa.Integer(), nullable=False),
    sa.Column('video_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['customer_id'], ['customer.customer_id'], ),
    sa.ForeignKeyConstraint(['video_id'], ['video.video_id'], ),
    sa.PrimaryKeyConstraint('customer_id', 'video_id')
    )
    op.drop_table('association')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('association',
    sa.Column('customer_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('video_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['customer_id'], ['customer.customer_id'], name='association_customer_id_fkey'),
    sa.ForeignKeyConstraint(['video_id'], ['video.video_id'], name='association_video_id_fkey'),
    sa.PrimaryKeyConstraint('customer_id', 'video_id', name='association_pkey')
    )
    op.drop_table('checked')
    # ### end Alembic commands ###
