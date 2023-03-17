import pytest
from pytest_mock import MockerFixture
from sqlalchemy import MetaData, Table, delete, func, select, update

from hello_world.database.main import data_delete, data_insert, main
from hello_world.database.models import Test
from hello_world.database.setting import Database

session = main()


# def test_data_insert_delete():
#     data_insert(session)
#     stmt = select(Test)
#     result = session.execute(stmt)
#     t1 = Test(id=0, name="test1", value=100)
#     t2 = Test(id=1, name="test2", value=200)
#     test_list = [t1, t2]
#     for test_obj, result_obj in zip(test_list, result.scalars()):
#         assert (
#             (test_obj.id == result_obj.id) & (test_obj.name == result_obj.name) & (test_obj.value == result_obj.value)
#         )
#     result = data_delete(session)

#     for test_obj in result.scalars():
#         assert test_obj == {}


@pytest.fixture
def set_session(mocker: MockerFixture) -> main:
    mocker.patch("hello_wordl.database.main")
    return main()


def test_data_insert_mock(mocker: MockerFixture):
    mocker.patch("hello_world.database.main")


@pytest.mark.parametrize("id,name,value", [(0, "t1", 10), (1, "t2", 20), (2, "t3", 30)])
def test_data_insert_mark(mocker: MockerFixture, id, name, value):
    mocker.patch.object(Database, "session")
    s_session = main()
    test_list = [
        Test(id=id, name=name, value=value),
    ]
    # with as :
    data_insert(s_session, test_list)
    stmt = select(Test)
    result = s_session.execute(stmt)
    #    t2 = Test(id=1, name="test2", value=200)
    for test_obj, result_obj in zip(test_list, result.scalars()):
        assert (
            (test_obj.id == result_obj.id) & (test_obj.name == result_obj.name) & (test_obj.value == result_obj.value)
        )
    result = data_delete(s_session)
    # s_session.close()
    for test_obj in result.scalars():
        assert test_obj == {}


@pytest.mark.parametrize(
    "items",
    [
        [[0, "t1", 10], [1, "t2", 20], [2, "t3", 30]],
        [[1, "t1", 10], [3, "t2", 20], [4, "t3", 30]],
        [[0, "t1", 10], [1, "t2", 20], [2, "test", 40]],
    ],
)
def test_data_read_item(mocker: MockerFixture, items):
    mocker.patch.object(Database, "session")
    s_session = main()
    test_list = []
    for item in items:
        id, name, value = item
        test_list.append(Test(id=id, name=name, value=value))
    data_insert(s_session, test_list)
    stmt = select(Test)
    result = s_session.execute(stmt)
    for test_obj, result_obj in zip(test_list, result.scalars()):
        assert (test_obj[0] == result_obj.id) & (test_obj[1] == result_obj.name) & (test_obj[2] == result_obj.value)
