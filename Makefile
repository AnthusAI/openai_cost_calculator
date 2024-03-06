.PHONY: test coverage

test:
	python3 -m unittest discover -s . -p '*_test.py'

coverage:
	coverage run -m unittest discover -s . -p '*_test.py'
	coverage report -m
	coverage html

watch:
	watchexec --exts py "make test"