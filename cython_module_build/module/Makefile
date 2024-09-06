.PHONY: build
build:
	python setup.py build_ext --inplace

.PHONY: unbuild
unbuild:
	rm helloworld.c
	rm helloworld.cpython*
	rm -rf build/*
	rm *.c
	rm *.so


.PHONY: rebuild
rebuild: unbuild build

.PHONY: venv
venv:
	virtualenv .venv