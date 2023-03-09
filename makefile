.PHONY: default all \
	install install-dev download-ta-lib \
	format lint \
	test coverage docs badge \
	docker docker-push \
	run collector celery \

default: all

install:
	@poetry install --only main --no-root

install-dev:
	@poetry install --no-root
# compile:
# 	@poetry run python -m compileall $(APP_NAME)

format:
	@poetry run isort .
	@poetry run black .

lint:
	@poetry run \
		isort --check-only .
	@poetry run \
		black --check .
	@poetry run \
		flake8 . --config setup.cfg
	@poetry run \
		mypy .

test:
	@poetry run \
		python -m pytest . \
			--junitxml=public/test/junit.xml \
			--html=public/test/report.html

coverage:
	@poetry run coverage run -m pytest
	@poetry run coverage report

badge:
	@poetry run \
		genbadge tests \
		--input-file public/test/junit.xml \
		--output-file public/tests.svg
	@poetry run \
		genbadge coverage \
		--input-file public/coverage/coverage.xml \
		--output-file public/coverage.svg
	
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

# all: install-dev test

# check-ta-lib:
# ifeq ($(shell ls ta-lib 2>/dev/null),)
# 	$(error You have to download ta-lib to the project directory (Run `make download-ta-lib`).)
# endif

# check-env:
# ifeq ($(AUTH_TOKEN),)
# 	$(error 'GITLAB_ACCESS_TOKEN' is not defined.)
# endif

