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
else ifeq ($(LANG),java)
	cd java/$(YEAR)/day$(DAY) && javac Main.java -d out && java -cp out Main
else ifeq ($(LANG),cpp)
	cd cpp/$(YEAR)/day$(DAY) && g++ -std=c++23 -O2 main.cpp -o main && ./main
else
	$(error Unknown LANG "$(LANG)" — add a branch to the Makefile for it)
endif
