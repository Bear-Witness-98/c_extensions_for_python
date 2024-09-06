# Use of cffi in python

Tested the usage of the cffi interface, seems quite messy.
The options to the compiler are sort of abstracted from me, so no easy liberty
on this is given. A simple thing that I wanted to do was to add a path to the
include path, but it was quite complicated.

The object here that is compiled and then generated a `.so` file from is a C
file in the same sense as the ones in the extension module iteration of this
repo. It appears to be quite complete with a lot of configurations and
documentation. But it is relatively obscure. Maybe it makes sense to generate
one of this as a first version for a library, and then continue using the
methodology of the Extension module?

It allows you to write C code in a plain string and compile that alone, to use,
which can make things simpler but also quite messy. Could have a separate file
that gets read and thrown into the python builder. But this seems to be quite
the patch just to use this.

I don't know if I have already fought too much with stuff, but I don't like it
that much.