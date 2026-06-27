.PHONY: install format lint type test validate demo clean

install:
	pip install -r requirements.txt
	pip install -r requirements-dev.txt

format:
	ruff format app examples tests

lint:
	ruff check app examples tests

type:
	mypy app

test:
	pytest

validate:
	python -m compileall app
	ruff check app examples tests
	mypy app
	pytest

demo:
	python examples/embedding_demo.py

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -name "*.pyc" -delete

all: clean validate demo
