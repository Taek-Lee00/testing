from collections.abc import MutableMapping

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, declarative_base, sessionmaker
from sqlalchemy_utils import create_database, database_exists, drop_database

# class _Base:
#     __allow_unmapped__ = True


# t_user, t_password, t_host, t_db
class Database:
    def __init__(self, *, user: str, password: str, host: str, db_name: str):
        url = f"postgresql+psycopg2://{user}:{password}@{host}/{db_name}"
        self.engine = create_engine(url, echo=True)

    def session(self):
        from hello_world.database import models

        models.Base.metadata.create_all(bind=self.engine)
        # autocommit=False, autoflush=False, expire_on_commit=False,
        return sessionmaker(bind=self.engine)
