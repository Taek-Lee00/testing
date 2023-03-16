from sqlalchemy import BigInteger, Column, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Test(Base):
    __tablename__ = "people"

    id: int = Column(BigInteger, primary_key=True, index=True)
    name: str = Column(String(30), unique=True, index=True, nullable=False)
    value: int = Column(BigInteger, unique=True, index=True, nullable=False)
