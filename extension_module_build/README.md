# C Extension Module For Python

Add a little toy C extension module for python

Tested:
* Creating a simple sources for additional functionalities.
* Creating multiple sources and headers, and adding them by the setup.py
functionality.
* Discovered that the setup.py functionality is almost deprecated, almost
exclusively used for adding extension modules.
* Sort of discovered that the suggested way of generating modules is by
exclusievely using the pyproject.toml (in absence of extension modules).
* Creating multiple modules, and sorting them in tidies up files.
* Created a makefile to automate recurrent code executions.