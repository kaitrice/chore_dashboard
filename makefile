.PHONY: all reset run test create_tests

DB = database.db
PYTHON = py
PY_FILES := $(wildcard *.py)
TEST_DIR := test

all: reset run

reset:
	@if [ -f $(DB) ]; then rm $(DB); fi
	# Database removed

run:
	$(PYTHON) main.py

test:
	$(PYTHON) -m unittest

# Create test files
create_tests: $(TEST_DIR)
	@for f in $(PY_FILES); do \
		TEST_FILE=$(TEST_DIR)/$${f%.py}_test.py; \
		if [ ! -f $$TEST_FILE ]; then \
			echo "# Auto-generated test file for $$f" > $$TEST_FILE; \
			echo "import unittest" >> $$TEST_FILE; \
			echo "from $$f import *" >> $$TEST_FILE; \
			echo "" >> $$TEST_FILE; \
			echo "class Test$$(basename $$f .py)(unittest.TestCase):" >> $$TEST_FILE; \
			echo "    pass" >> $$TEST_FILE; \
			echo "Created $$TEST_FILE"; \
		fi \
	done