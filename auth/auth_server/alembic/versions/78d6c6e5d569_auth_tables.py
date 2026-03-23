from alembic import op
import sqlalchemy as sa

revision = '78d6c6e5d569'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    
    op.create_table(
        'roles',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('name', sa.String(), nullable=False, unique=True),
        sa.Column('description', sa.String(), nullable=True),
        sa.Column('created_at', sa.Integer(), nullable=False),
        sa.Column('deleted_at', sa.Integer(), nullable=True),
    )

    op.create_table(
        'types',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('name', sa.String(), nullable=False, unique=True),
        sa.Column('description', sa.String(), nullable=True),
        sa.Column('created_at', sa.Integer(), nullable=False),
        sa.Column('deleted_at', sa.Integer(), nullable=True),
    )

    op.create_table(
        'users',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('mail', sa.String(), nullable=False, unique=True),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('password', sa.String(), nullable=False),
        sa.Column('last_login', sa.Integer(), nullable=True),
        sa.Column('created_at', sa.Integer(), nullable=False),
        sa.Column('deleted_at', sa.Integer(), nullable=True),
    )

    op.create_table(
        'assignments',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('user_id', sa.Integer(), sa.ForeignKey('users.id'), nullable=False),
        sa.Column('role_id', sa.Integer(), sa.ForeignKey('roles.id'), nullable=False),
        sa.Column('type_id', sa.Integer(), sa.ForeignKey('types.id'), nullable=False),
        sa.Column('resource_id', sa.Integer(), nullable=True),
        sa.Column('created_at', sa.Integer(), nullable=False),
        sa.Column('deleted_at', sa.Integer(), nullable=True),
    )


def downgrade() -> None:
    op.drop_table('assignments')
    op.drop_table('users')
    op.drop_table('types')
    op.drop_table('roles')
