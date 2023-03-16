.PHONY: default all \
	install install-dev download-ta-lib \
	format lint \
	test coverage docs badge \
	docker docker-push \
	run collector celery \

PROJECT_NAME ?= $(shell sed -n 's/^name = "\(.*\)"/\1/p' pyproject.toml)
APP_NAME ?= "hello_world"
DOCKER_APP_IMAGE_TAG ?= "$(PROJECT_NAME)"



default: all

install:
	@poetry install --only main --no-root

install-dev:
	@poetry install --no-root
# compile:
# 	@poetry run python -m compileall $(APP_NAME)

run: 
	@poetry run python -m $(APP_NAME)

format:
	@poetry run isort .
	@poetry run black . 

lint:
	@poetry run \
		isort --check-only .
	@poetry run \
		black --check .
	@poetry run \
		mypy .
	@poetry run \
		flake8 . --exit-zero --config setup.cfg
	

test:
	@poetry run \
		python -m pytest -v \
			--junitxml docs/test/junit.xml \
			--html=docs/test/report.html

coverage:
	@poetry run coverage run -m pytest
	@poetry run coverage report

badge:
	@poetry run \
		genbadge tests \
		--input-file docs/test/junit.xml \
		--output-file docs/tests.svg
	@poetry run \
		genbadge coverage \
		--input-file docs/coverage/coverage.xml \
		--output-file docs/coverage.svg

docker: 
	@docker build \
		-f docker/Dockerfile \
		--pull \
		-t "$(DOCKER_APP_IMAGE_TAG)" .



# @VERSION=$(shell poetry run python -m $(APP_NAME) docs --version); \
# poetry run \
# 	anybadge \
# 	-l docs \
# 	-v $$VERSION \
# 	-f public/docs.svg \
# 	-c green

# docs:
# 	@poetry run python -m $(APP_NAME) docs

# run:
# 	@poetry run python -m $(APP_NAME) run

# collect:
# 	@poetry run python -m $(APP_NAME) collect

all: install-dev test

# check-ta-lib:
# ifeq ($(shell ls ta-lib 2>/dev/null),)
# 	$(error You have to download ta-lib to the project directory (Run `make download-ta-lib`).)
# endif

# check-env:
# ifeq ($(AUTH_TOKEN),)
# 	$(error 'GITLAB_ACCESS_TOKEN' is not defined.)
# endif

