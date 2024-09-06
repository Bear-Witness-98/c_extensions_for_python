# test script

# simple working example of using cffi to call a C function in a 
# compiled shared object (DLL) from python. (First section)

# cffi is flexible and has several other use cases (second section?)

# third section shows how to export python functions to a python
# interpreter embedded in a C or C++ application, not interested in this
# , at least for now.

###
# build object
##
from cffi import FFI
ffibuilder = FFI()

ffibuilder.cdef(
    """
        int factorial(unsigned int n);

        int fibonacci(unsigned int n);

        int custom_sum(int a, int b);

    """)

ffibuilder.set_source(
    "_new_module",  # name of the output C extension
    """
        #include "include/misc.h"
        #include "include/ops.h"
    """,
    sources=[
        'src/misc/misc.c',
        'src/ops/facto.c',
        'src/ops/fib.c',
    ],   # includes additional sources
    libraries=['m'] # on Unix, link with the math library
)    

if __name__ == "__main__":
    ffibuilder.compile(verbose=True)