.PHONY: unbuild
unbuild:
	rm module/*.so 

.PHONY: build
build:
	c++ -O3 -Wall -shared -std=c++11 -Imodule/include -undefined dynamic_lookup $$(python3 -m pybind11 --includes) module/main.cpp module/src/misc/* module/src/ops/* -o module/main$$(python3-config --extension-suffix)

.PHONY: rebuild
rebuild: unbuild build

.PHONY: venv
venv:
	virtualenv .venv


