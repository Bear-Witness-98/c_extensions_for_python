.PHONY: build
build:
	gcc -c -fPIC src/misc/misc.c src/ops/facto.c src/ops/fib.c -Iinclude
	gcc -shared -o ../new_module.so *.o

.PHONY: unbuild
unbuild:
	rm -rf fib.o facto.o misc.o
	rm -rf ../new_module.so


.PHONY: rebuild
rebuild: unbuild build

.PHONY: venv
venv:
	virtualenv .venv