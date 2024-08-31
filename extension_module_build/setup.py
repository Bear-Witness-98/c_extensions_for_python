from setuptools import Extension, setup


module_first_path = "module_first"
sources = [
        f"{module_first_path}/main.c",
        f"{module_first_path}/src/ops/facto.c",
        f"{module_first_path}/src/ops/fib.c",
        f"{module_first_path}/src/misc/misc.c",
]
include_dirs = [f"{module_first_path}/include"]
# I can add compiler specific flags here
# don't know if I can compile by parts though
module_1 = Extension(
    name="module_first",
    sources=sources,
    include_dirs=include_dirs,
)

module_first_path = "module_second"
sources = [
        f"{module_first_path}/main.c",
        f"{module_first_path}/src/ops/facto.c",
        f"{module_first_path}/src/ops/fib.c",
        f"{module_first_path}/src/misc/misc.c",
]
include_dirs = [f"{module_first_path}/include"]
module_2 = Extension(
    name="module_second",
    sources=sources,
    include_dirs=include_dirs,
)

setup(
    name='pkg',
    version='1.0',
    description='A sample Python C extension module',
    ext_modules=[module_1, module_2],       # List of extension modules
)