.PHONY: all
all: install lint test build

.PHONY: clean
clean:
	find . -name "*.pyc" -delete
	rm -rf *.egg-info build
	rm -rf coverage*.xml .coverage
	rm -rf .mypy_cache
	rm -rf .ruff_cache

.PHONY: install
install:
	poetry install --all-extras --with=dev --with=docs

.PHONY: lint
lint: lint/ruff lint/mypy

.PHONY: lint/ruff
lint/ruff:
	poetry run ruff format --diff
	poetry run ruff check

.PHONY: lint/mypy
lint/mypy:
	poetry run mypy wozpy

.PHONY: format
format: format/ruff

.PHONY: format/ruff
format/ruff:
	poetry run ruff format
	poetry run ruff check --fix

.PHONY: test
test:
	poetry run pytest .

.PHONY: build
build:
	poetry build
