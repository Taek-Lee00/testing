import os
import sys
from multiprocessing import Process

import pytest
import uvicorn
from fastapi import FastAPI
from fastapi.testclient import TestClient

from hello_world import main
from hello_world.main import app
from tests.conftest import Foo, EnvValue, EnvValueA, EnvValueB

# def test_app(mocker: MockerFixture) -> None:
#     run_mock = mocker.patch("uvicorn.run")
#     mocker.patch.object(sys, "argv", [--port, ""])
#     run.run()
#     run_mock.assert_called()


def run_server():
    uvicorn.run(app, host="127.0.0.1", port=8000)


@pytest.fixture
def server():
    proc = Process(target=run_server, args=(), daemon=True)
    proc.start()
    yield proc
    proc.kill()  # Cleanup after test


def test_read_main(change):
    client = TestClient(app)
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": f"""hello, {change} """}

    client2 = TestClient(app)
    response = client2.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": f"""hello, {change} """}


def test_read_main2(env_val: Foo):
    client = TestClient(app)
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": f"""hello, {env_val.set_EnvValue()} """}

    env_val.envValue = EnvValueA()
    client2 = TestClient(app)
    response = client2.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": f"""hello, {env_val.set_EnvValue()} """}
