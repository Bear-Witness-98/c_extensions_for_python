from ctypes import CDLL, c_int, c_wchar_p

# "libSystem.dylib" is the C standard library object in macOS
libc = CDLL("libSystem.dylib")

print(f"Printf functions is stored at: {libc.printf}")

print(f"This is a random number given by the std library {libc.rand()}")

print(f"Apparently, the random number depends on something that is currenlty fixed {libc.rand()}")

print(f"Like, the line number? {libc.rand()}")

# called with the binary
libc.printf(b"This is a text\n")

# the faulthandler module can be helpful in debugging crashes


# None, integers, bytes objects and (unicode) strings are the only
# native Python objects that can directly be used as parameters in these function calls.

# None is passed as a C NULL pointer, bytes objects and strings are passed as pointer to
# the memory block that contains their data (char* or wchar_t*). Python integers are
# passed as the platforms default C int type, their value is masked to fit into the C type.

# lots of additional types defined to pass to the c functions.

i = c_int(42)
print(i)
print(i.value)
i.value = 99
print(i.value)

# assigning new values to pointer types, assignes new memory addresses to the 
# contents, as the underlying python objects are immutable.

print("===============================")
s = "Hello, World"
c_s = c_wchar_p(s)
print(c_s) # containes the pointer to the info, not the info itseald
print(c_s.value) # prints the info from the pointer
c_s.value = "Hi, there"
print(c_s)              # the memory location has changed
print(c_s.value)
print(s)                # first object is unchanged

"""
You should be careful, however, not to pass them to functions expecting pointers to
mutable memory. If you need mutable memory blocks, ctypes has a create_string_buffer()
function which creates these in various ways. The current memory block contents can be
accessed (or changed) with the raw property; if you want to access it as NULL terminated
string, use the value property:
"""
# there are ways to pass everything to these functions, lists, arrays, and a lot of
# other stuff. Doesn't make sense to go through all of them, I'll just try to load
# the relevant functions here and 
