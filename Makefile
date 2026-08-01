# Usage: make run LANG=python YEAR=2015 DAY=01

LANG ?= python
YEAR ?=
DAY  ?=

.PHONY: run
run:
ifeq ($(YEAR),)
	$(error YEAR is required, e.g. make run LANG=python YEAR=2015 DAY=01)
endif
ifeq ($(DAY),)
	$(error DAY is required, e.g. make run LANG=python YEAR=2015 DAY=01)
endif
ifeq ($(LANG),python)
	uv run python/$(YEAR)/day$(DAY).py
else
	$(error Unknown LANG "$(LANG)" — add a branch to the Makefile for it)
endif
