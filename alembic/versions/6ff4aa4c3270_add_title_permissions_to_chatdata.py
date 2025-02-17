"""add title permissions to ChatData

Revision ID: 6ff4aa4c3270
Revises: 6e3c11194f82
Create Date: 2024-04-05 22:44:03.204318

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "6ff4aa4c3270"
down_revision: Union[str, None] = "6e3c11194f82"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("chat_data", sa.Column("title_permissions", sa.JSON(), nullable=True))
    # op.alter_column('chat_data', 'id',
    #            existing_type=sa.INTEGER(),
    #            type_=sa.BigInteger(),
    #            existing_nullable=False,
    #            autoincrement=False)
    # op.alter_column('quotes', 'chat_id',
    #            existing_type=sa.INTEGER(),
    #            type_=sa.BigInteger(),
    #            existing_nullable=True)
    # op.alter_column('quotes', 'message_id',
    #            existing_type=sa.INTEGER(),
    #            type_=sa.BigInteger(),
    #            existing_nullable=False)
    # op.alter_column('quotes', 'user_id',
    #            existing_type=sa.INTEGER(),
    #            type_=sa.BigInteger(),
    #            existing_nullable=True)
    # op.alter_column('quotes', 'qer_id',
    #            existing_type=sa.INTEGER(),
    #            type_=sa.BigInteger(),
    #            existing_nullable=True)
    # op.alter_column('user_chat_association', 'user_id',
    #            existing_type=sa.INTEGER(),
    #            type_=sa.BigInteger(),
    #            existing_nullable=False,
    #            autoincrement=False)
    # op.alter_column('user_chat_association', 'chat_id',
    #            existing_type=sa.INTEGER(),
    #            type_=sa.BigInteger(),
    #            existing_nullable=False,
    #            autoincrement=False)
    # op.alter_column('user_chat_association', 'waifu_id',
    #            existing_type=sa.INTEGER(),
    #            type_=sa.BigInteger(),
    #            existing_nullable=True)
    # op.alter_column('user_data', 'id',
    #            existing_type=sa.INTEGER(),
    #            type_=sa.BigInteger(),
    #            existing_nullable=False,
    #            autoincrement=False)
    # op.alter_column('user_data', 'married_waifu_id',
    #            existing_type=sa.INTEGER(),
    #            type_=sa.BigInteger(),
    #            existing_nullable=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    # op.alter_column('user_data', 'married_waifu_id',
    #            existing_type=sa.BigInteger(),
    #            type_=sa.INTEGER(),
    #            existing_nullable=True)
    # op.alter_column('user_data', 'id',
    #            existing_type=sa.BigInteger(),
    #            type_=sa.INTEGER(),
    #            existing_nullable=False,
    #            autoincrement=False)
    # op.alter_column('user_chat_association', 'waifu_id',
    #            existing_type=sa.BigInteger(),
    #            type_=sa.INTEGER(),
    #            existing_nullable=True)
    # op.alter_column('user_chat_association', 'chat_id',
    #            existing_type=sa.BigInteger(),
    #            type_=sa.INTEGER(),
    #            existing_nullable=False,
    #            autoincrement=False)
    # op.alter_column('user_chat_association', 'user_id',
    #            existing_type=sa.BigInteger(),
    #            type_=sa.INTEGER(),
    #            existing_nullable=False,
    #            autoincrement=False)
    # op.alter_column('quotes', 'qer_id',
    #            existing_type=sa.BigInteger(),
    #            type_=sa.INTEGER(),
    #            existing_nullable=True)
    # op.alter_column('quotes', 'user_id',
    #            existing_type=sa.BigInteger(),
    #            type_=sa.INTEGER(),
    #            existing_nullable=True)
    # op.alter_column('quotes', 'message_id',
    #            existing_type=sa.BigInteger(),
    #            type_=sa.INTEGER(),
    #            existing_nullable=False)
    # op.alter_column('quotes', 'chat_id',
    #            existing_type=sa.BigInteger(),
    #            type_=sa.INTEGER(),
    #            existing_nullable=True)
    # op.alter_column('chat_data', 'id',
    #            existing_type=sa.BigInteger(),
    #            type_=sa.INTEGER(),
    #            existing_nullable=False,
    #            autoincrement=False)
    op.drop_column("chat_data", "title_permissions")
    # ### end Alembic commands ###
