.PHONY: build
build:
	python main.py
	python inline_building.py

.PHONY: unbuild
unbuild:
	rm _new_module*
	rm src/misc/misc.o
	rm src/ops/facto.o
	rm src/ops/fib.o
	rm _example*
	
.PHONY: rebuild
rebuild: unbuild build

.PHONY: venv
venv:
	virtualenv .venv

.PHONY: test
test:
	python test.py