.PHONY: test coverage

test:
	uv run -m unittest discover -s . -p '*_test.py'

coverage:
	uv run coverage run -m unittest discover -s . -p '*_test.py'
	uv run coverage report -m
	uv run coverage html

watch:
	uv run watchexec --exts py "make test"