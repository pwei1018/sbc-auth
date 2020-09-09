"""create account login options

Revision ID: 4d115fc3642c
Revises: f1ce3f279b60
Create Date: 2020-07-10 05:54:37.982727

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4d115fc3642c'
down_revision = 'f1ce3f279b60'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('account_login_options',
    sa.Column('created', sa.DateTime(), nullable=True),
    sa.Column('modified', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('login_source', sa.String(length=20), nullable=False),
    sa.Column('org_id', sa.Integer(), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.Column('created_by_id', sa.Integer(), nullable=True),
    sa.Column('modified_by_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['created_by_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['modified_by_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['org_id'], ['org.id'], ),
    sa.PrimaryKeyConstraint('id')
    )

    op.add_column('invitation', sa.Column('login_source', sa.String(length=20), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('invitation', 'login_source')
    op.drop_table('account_login_options')

    # ### end Alembic commands ###
