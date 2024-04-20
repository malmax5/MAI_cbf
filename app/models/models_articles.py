from sqlalchemy import Table, Column
from sqlalchemy import BigInteger, Integer, Text, String
from sqlalchemy import MetaData
from sqlalchemy.ext.declarative import DeclarativeMeta, declarative_base


metadata = MetaData()
Base = declarative_base()


publics = Table(
    "user_publics",
    metadata,
    Column('id', BigInteger(), nullable=False, primary_key=True, autoincrement=True),
    Column('user_id', BigInteger(), nullable=False),
    Column('book_id', Integer(), nullable=False),
    Column('article_name', String(50), nullable=False),
    Column('text', Text(), nullable=False),
    Column('likes', Integer(), default=0),
    Column('viewed', Integer(), default=0),
)


class Publics(Base):
    __tablename__ = "user_publics"
    id = Column(BigInteger(), nullable=False, primary_key=True, autoincrement=True)
    user_id = Column(BigInteger(), nullable=False)
    book_id = Column(Integer(), nullable=False)
    article_name = Column(String(50), nullable=False)
    text = Column(Text(), nullable=False)
    likes = Column(Integer(), default=0)
    viewed = Column(Integer(), default=0)