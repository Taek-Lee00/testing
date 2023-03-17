from __future__ import annotations

import os
from abc import ABC, abstractmethod

import pytest
from dotenv import find_dotenv, load_dotenv, set_key
from fastapi import FastAPI

from hello_world.main import app


@pytest.fixture
def fastapi_app() -> FastAPI:
    return app


# @pytest.fixture
# def change(fastapi_app) -> str:
#     dot_file = find_dotenv()
#     load_dotenv(dot_file)

#     yield os.environ["FOO"]
#     set_key(dot_file, "FOO", "worl")
#     dot_file = find_dotenv()
#     load_dotenv(dot_file)
#     fastapi_app.dependency_overrides = {}

#     return os.environ["FOO"]


@pytest.fixture
def change(fastapi_app) -> str:
    dot_file = find_dotenv()
    # yield os.environ["FOO"]
    set_key(dot_file, "FOO", "world")
    load_dotenv(dot_file)
    yield os.environ["FOO"]
    set_key(dot_file, "FOO", "foo_A")
    load_dotenv(dot_file)
    fastapi_app.dependency_overrides = {}

    return os.environ["FOO"]


class Foo:
    def __init__(self, env_val: EnvValue) -> None:
        self._env_val = env_val

    @property
    def envValue(self) -> EnvValue:
        return self._env_val

    @envValue.setter
    def envValue(self, env_val: EnvValue):
        self._env_val = env_val

    def set_EnvValue(self) -> str:
        return self._env_val.get_EnvValue("")


class EnvValue(ABC):
    @abstractmethod
    def get_EnvValue(self, data: str) -> str:
        pass


class EnvValueN(EnvValue):
    def get_EnvValue(self, data: str = "world") -> str:
        return data


class EnvValueA(EnvValue):
    def get_EnvValue(self, data: str = "foo_A") -> str:
        return data


class EnvValueB(EnvValue):
    def get_EnvValue(self, data: str = "foo_B") -> str:
        return data


@pytest.fixture
def env_val() -> Foo:
    foo = Foo(EnvValueN())
    return foo
