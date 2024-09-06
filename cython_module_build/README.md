# Use of cython in python to generate an extension module

The fundamental nature of Cython can be summed up as follows: Cython
is Python with C data types.

Cython is an optimising static compiler for both the Python
programming language and the extended Cython programming language
(based on Pyrex). It makes writing C extensions for Python as easy as
Python itself.

The Cython language is a superset of the Python language that
additionally supports calling C functions and declaring C types on
variables and class attributes. This allows the compiler to generate
very efficient C code from Cython code.

So I assume this module needs to be compiled to work.

Indeed, it is compiled to C code as before with cffi, with the same
format as the extension module.

it works with two syntaxes. Pure python, or cython syntax.
The first one uses type anottations to convert to c types and tightly
optimze the C code generated
The second one is used in older codebases and in modules that need
to make use of advanced C/C++ features when interacting with libraries

Seems an interesting way to compile python or pseudo-python (cython) code into
C with an interesting speedup. It is worth noting thougn, that the pyx code is
a little bit tricky, as it does not get so much properly highlighted.

I think the not syntax highlighting makes it lose quite a bit of attractive.
Maybe I haven't explored them much though.
