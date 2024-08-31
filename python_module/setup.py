from setuptools import Extension, setup

setup(
    ext_modules=[
        Extension(
            name="mylib.foo",  # as it would be imported
                               # may include packages/namespaces separated by `.`

            sources=["foo.c"], # all sources are compiled into a single binary file
        ),
    ]
)