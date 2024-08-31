.PHONY: unbuild
unbuild:
	rm -rf dist
	rm -rf *.egg-info

.PHONY: build
build:
	python -m build
	pip install dist/*.whl

.PHONY: rebuild
rebuild: unbuild build

.PHONY: venv
venv:
	virtualenv .venv

.PHONY: deps
deps:
	pip install setuptools
	pip install build


