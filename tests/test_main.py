import sys
import os

import pytest
from pytest_mock import MockerFixture
from fastapi import FastAPI
from fastapi.testclient import TestClient
import uvicorn
from hello_world import main, run
from hello_world.main import app
from multiprocessing import Process
import requests


# def test_app(mocker: MockerFixture) -> None:
#     run_mock = mocker.patch("uvicorn.run")
#     mocker.patch.object(sys, "argv", [--port, ""])
#     run.run()
#     run_mock.assert_called()

def run_server():
    uvicorn.run(app, host= "127.0.0.1", port=8000)

@pytest.fixture
def server():
    proc = Process(target=run_server, args=(), daemon=True)
    proc.start() 
    yield proc
    proc.kill() # Cleanup after test


def test_read_main():
    #uvicorn.run("main:app", host = "0.0.0.0", port=8000)
    client = TestClient(app)
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello, World!"}




