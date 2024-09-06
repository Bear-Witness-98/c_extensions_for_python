# file "example_build.py"

from cffi import FFI
ffibuilder = FFI()

ffibuilder.cdef("int foo(int n, int m);")

ffibuilder.set_source("_example",
    r"""
        static int foo(int n, int m){
            if(n == 0) return 1;
            if(m == 0) return 2;
            
            return 0;
        }
    """,
)

if __name__ == "__main__":
    ffibuilder.compile(verbose=True)