from setuptools import setup
from Cython.Build import cythonize

setup(
    # ext_modules = cythonize("helloworld.py")
    # ext_modules = cythonize("fibonacci.py")
    # ext_modules = cythonize("primes.py")
    ext_modules = cythonize("primes.pyx")
)