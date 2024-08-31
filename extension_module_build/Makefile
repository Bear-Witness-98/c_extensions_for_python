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
	pip install dist/*.whl


.PHONY: rebuild
rebuild: unbuild build


