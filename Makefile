test:
	python3 -m unittest

coverage:
	coverage run -m unittest
	coverage report

.PHONY: test coverage

