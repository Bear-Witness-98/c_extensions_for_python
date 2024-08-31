// Code to reproduce the example at https://docs.python.org/3/extending/extending.html

// We want to do something like this:
/*
import spam
status = spam.system("ls -l")
*/
// and for the function to return an integer

// The following may include some preprocessor stuff, so it should be included
// before any standard headers are included
// It is also recomended to initialize this macro befor the import
#define PY_SSIZE_T_CLEAN
#include <Python.h>


// The thing we want to execute when we do our call
static PyObject *spam_system(PyObject *self, PyObject *args){
    const char *command;
    int sts;

    if (!PyArg_ParseTuple(args, "s", &command))
        return NULL;
    sts = system(command);
    if (sts < 0) {
        PyErr_SetString(SpamError, "System command failed");
        return NULL;
    }
    return PyLong_FromLong(sts); // convets sys (int) to a python object
}

/*
The self argument points to the module object for module-level functions; for a method it would point to the object instance.
The args argument will be a pointer to a Python tuple object containing the arguments. Each item of the tuple is a python object
*/

static PyMethodDef SpamMethods[] = {
    //...
    {"system",  
    spam_system, 
    METH_VARARGS, // indicates the calling convention to be used for the C function. It is usually this one or METH_VARARGS | METH_KEYWORDS
    "Execute a shell command."},
    //...
    {NULL, NULL, 0, NULL}        /* Sentinel */
};

// The method table must be referenced in the module definition structure:
static struct PyModuleDef spammodule = {
    PyModuleDef_HEAD_INIT,
    "spam",   /* name of module */
    spam_doc, /* module documentation, may be NULL */
    -1,       /* size of per-interpreter state of the module,
                 or -1 if the module keeps state in global variables. */
    SpamMethods
};

// initialization and error handling stuff
static PyObject *SpamError;
PyMODINIT_FUNC PyInit_spam(void) {
    PyObject *m;

    m = PyModule_Create(&spammodule);
    if (m == NULL)
        return NULL;

    SpamError = PyErr_NewException("spam.error", NULL, NULL);
    Py_XINCREF(SpamError);
    if (PyModule_AddObject(m, "error", SpamError) < 0) {
        Py_XDECREF(SpamError);
        Py_CLEAR(SpamError);
        Py_DECREF(m);
        return NULL;
    }

    return m;
}