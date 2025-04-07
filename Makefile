# Makefile

.PHONY: install test

# Komenda do instalacji zależności w projekcie
install:
	poetry install

# Komenda do tworzenia dokumentacji w sphinx
docs:
	poetry run sphinx-build -b html docs/source docs/build

# Komenda do uruchomienia testów
test:
	poetry run pytest

# Komenda do uruchomienia aplikacji
run:
	poetry run python main.py

# Komenda do uruchomienia lintera w flake8
flake8-lint:
	poetry run flake8

# Komenda do uruchomienia lintera w pylint
pylint:
	poetry run pylint .
