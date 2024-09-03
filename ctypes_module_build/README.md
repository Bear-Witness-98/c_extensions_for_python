# Use of ctypes in python

Followed the official guide on working with ctypes
https://docs.python.org/3/library/ctypes.html

Seems really easy to use from python, given that the functions you need are in
a .so object. 

The difference with building external modules with setup.py, is that the
interface in this case is in the python side. With the other way, the interface
is on the C side. Don't know whether this may carry issues of some sort.

Seems pretty easy to use, though some unexpected behaviour may happen due to the
typings of stuff.

Also, it seems well documented on the guide pointed above, so if more complex
things need to be done, the guide may be usefull.