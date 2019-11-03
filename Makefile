test:
	python3 -m unittest

coverage:
	coverage run -m unittest
	coverage report

install:
	pip3 install coverage
	pip3 install retrying

.PHONY: test coverage install

