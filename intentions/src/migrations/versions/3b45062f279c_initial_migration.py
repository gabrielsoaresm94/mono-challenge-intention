"""initial_migration

Revision ID: 3b45062f279c
Revises: 
Create Date: 2023-06-03 23:18:23.924290

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3b45062f279c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('client',
    sa.Column('client_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=128), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('client_id')
    )
    op.create_table('address',
    sa.Column('address_id', sa.Integer(), nullable=False),
    sa.Column('country', sa.String(length=64), nullable=False),
    sa.Column('state', sa.String(length=64), nullable=False),
    sa.Column('city', sa.String(length=64), nullable=False),
    sa.Column('street', sa.Text(), nullable=False),
    sa.Column('number', sa.Integer(), nullable=False),
    sa.Column('apartment', sa.Integer(), nullable=True),
    sa.Column('complement', sa.Text(), nullable=True),
    sa.Column('client_id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['client_id'], ['client.client_id'], ),
    sa.PrimaryKeyConstraint('address_id')
    )
    op.create_table('intention',
    sa.Column('intention_id', sa.Integer(), nullable=False),
    sa.Column('status', sa.Enum('EM_SELECAO', 'SELECIONADO', name='intentionstatusenum'), nullable=False),
    sa.Column('client_id', sa.Integer(), nullable=False),
    sa.Column('address_id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['address_id'], ['address.address_id'], ),
    sa.ForeignKeyConstraint(['client_id'], ['client.client_id'], ),
    sa.PrimaryKeyConstraint('intention_id')
    )
    op.create_table('intention_product',
    sa.Column('intention_product_id', sa.Integer(), nullable=False),
    sa.Column('product_id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=256), nullable=False),
    sa.Column('price', sa.Double(), nullable=False),
    sa.Column('category', sa.String(length=64), nullable=False),
    sa.Column('description', sa.Text(), nullable=False),
    sa.Column('image', sa.String(length=128), nullable=False),
    sa.Column('quantity', sa.Integer(), nullable=True),
    sa.Column('intention_id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['intention_id'], ['intention.intention_id'], ),
    sa.PrimaryKeyConstraint('intention_product_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('intention_product')
    op.drop_table('intention')
    op.drop_table('address')
    op.drop_table('client')
    # ### end Alembic commands ###
