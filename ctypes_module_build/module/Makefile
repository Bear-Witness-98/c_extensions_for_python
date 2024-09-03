.PHONY: unbuild
unbuild:
	rm -rf dist
	rm -rf build
	rm -rf *.so
	find . -name '*egg*' | xargs rm -rf 

.PHONY: build
build:
	python -m build

.PHONY: xbuild
xbuild:
	python setup.py build_ext --inplace
	python setup.py sdist bdist_wheel
	pip install --force-reinstall dist/*.whl


.PHONY: rebuild
rebuild: unbuild build

.PHONY: venv
venv:
	virtualenv .venv

.PHONY: compile
compile:
	gcc -c -fPIC src/misc/misc.c src/ops/facto.c src/ops/fib.c -Iinclude
	gcc -shared -o ../new_module.so *.o


