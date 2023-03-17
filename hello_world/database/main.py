from sqlalchemy import MetaData, Table, delete, func, select, update
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.sql import Select
from sqlalchemy_utils import create_database, database_exists, drop_database

from hello_world.database.models import Test
from hello_world.database.setting import Database

# from sqlalchemy.sql.base import ImmutableColumnCollection


def main(db: Database = None):
    db = Database(user="t_user", password="", host="localhost", db_name="postgres")

    if not database_exists(db.engine.url):
        create_database(db.engine.url)

    Session = db.session()
    return Session()


def data_insert(session, data=None):
    # table: Table = Test.__table__
    # column: ImmutableColumnCollection = table.c

    # fields = (column["id"], column["name"], column["value"])
    session.add_all(data)
    session.commit()


def data_update(session):
    # table: Table = Test.__tablename__
    stmt_all = []
    stmt = update(Test).where(Test.name == "test2").values(value=950).returning(Test)
    stmt_all.append(stmt)
    result = session.execute(stmt)
    # session.commit()
    return result


def data_delete(session):
    stmt = delete(Test).where(Test.name == "test2").returning(Test)
    result = session.execute(stmt)
    stmt = delete(Test).where(Test.name == "test1").returning(Test)
    result = session.execute(stmt)
    session.commit()
    result = session.execute(select(Test))
    return result


if __name__ == "__main__":
    session = main()
    # insert(session)
    # result = data_update(session)
    result = data_delete(session)
    for test_obj in result.scalars():
        print(test_obj)
        print(f"{test_obj.name} _ {test_obj.value}")
    session.commit()
