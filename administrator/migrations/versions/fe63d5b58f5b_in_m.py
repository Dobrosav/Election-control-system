"""in m

Revision ID: fe63d5b58f5b
Revises: 
Create Date: 2021-08-15 10:43:35.426403

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fe63d5b58f5b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('elections',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('startDate', sa.DateTime(timezone=True), nullable=False),
    sa.Column('endDate', sa.DateTime(timezone=True), nullable=False),
    sa.Column('start', sa.String(length=24), nullable=False),
    sa.Column('end', sa.String(length=24), nullable=False),
    sa.Column('individual', sa.Boolean(), nullable=False),
    sa.Column('totalVotesNumber', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('participants',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=256), nullable=False),
    sa.Column('individual', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('participation_in_elections',
    sa.Column('participantId', sa.Integer(), nullable=False),
    sa.Column('electionId', sa.Integer(), nullable=False),
    sa.Column('number', sa.Integer(), nullable=False),
    sa.Column('result', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['electionId'], ['elections.id'], ),
    sa.ForeignKeyConstraint(['participantId'], ['participants.id'], ),
    sa.PrimaryKeyConstraint('participantId', 'electionId')
    )
    op.create_table('votes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('guid', sa.String(length=36), nullable=False),
    sa.Column('electionId', sa.Integer(), nullable=False),
    sa.Column('poolNumber', sa.Integer(), nullable=False),
    sa.Column('jmbg', sa.String(length=13), nullable=False),
    sa.Column('valid', sa.Boolean(), nullable=False),
    sa.Column('reason_invalid', sa.String(length=256), nullable=True),
    sa.ForeignKeyConstraint(['electionId'], ['elections.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('votes')
    op.drop_table('participation_in_elections')
    op.drop_table('participants')
    op.drop_table('elections')
    # ### end Alembic commands ###
