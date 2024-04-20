from sqlalchemy import Table, Column
from sqlalchemy import BigInteger
from sqlalchemy import MetaData
from sqlalchemy.ext.declarative import DeclarativeMeta, declarative_base


metadata = MetaData()
Base: DeclarativeMeta = declarative_base()


articles = Table(
    "user_subs",
    metadata,
    Column('id', BigInteger, nullable=False, primary_key=True, autoincrement=True),
    Column('user_id', BigInteger, nullable=False),
    Column('sub_id', BigInteger, nullable=True),
)


class Subs(Base):
    __tablename__ = "user_subs"
    id = Column(BigInteger, nullable=False, primary_key=True, autoincrement=True)
    user_id = Column(BigInteger, nullable=False)
    sub_id = Column(BigInteger, nullable=True)
