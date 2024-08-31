#define PY_SSIZE_T_CLEAN
#include <Python.h>

#include <stdio.h>

#include <ops.h>
#include <misc.h>

// initialization and error handling stuff
static PyObject *module_firstError;

//////////////////////////////////////////
/*Definition of the functions to be used*/
//////////////////////////////////////////
// The thing we want to execute when we do our call
static PyObject *spam_system(PyObject *self, PyObject *args){
    const char *command;
    int sts;

    if (!PyArg_ParseTuple(args, "s", &command))
        return NULL;
    sts = system(command);
    if (sts < 0) {
        PyErr_SetString(module_firstError, "System command failed");
        return NULL;
    }
    return PyLong_FromLong(sts); // convets sys (int) to a python object
}

static PyObject *fibonacci_handler(PyObject *self, PyObject *args){
    const int number;
    int sts;

    if (!PyArg_ParseTuple(args, "l", &number))
        return NULL;
    sts = fibonacci(number);
    return PyLong_FromLong(sts); // convets sys (int) to a python object
}

static PyObject *factorial_handler(PyObject *self, PyObject *args){
    const int number;
    int sts;

    if (!PyArg_ParseTuple(args, "l", &number))
        return NULL;
    sts = factorial(number);
    return PyLong_FromLong(sts); // convets sys (int) to a python object
}

static PyObject *custom_sum_handler(PyObject *self, PyObject *args){
    const int num_1;
    const int num_2;
    int sts;

    if (!PyArg_ParseTuple(args, "ii", &num_1, &num_2))
        return NULL;
    sts = custom_sum(num_1, num_2);
    return PyLong_FromLong(sts); // convets sys (int) to a python object
}


// Methods of the module to package
static PyMethodDef module_first_methods[] = {
    {
        "system",  
        spam_system, 
        METH_VARARGS, // indicates the calling convention to be used for the C function. It is usually this one or METH_VARARGS | METH_KEYWORDS
        "Execute a shell command."
    },
    {
        "fibonacci",  
        fibonacci_handler, 
        METH_VARARGS, // indicates the calling convention to be used for the C function. It is usually this one or METH_VARARGS | METH_KEYWORDS
        "Computes the nth fibonacci number."
    },
    {
        "factorial",  
        factorial_handler, 
        METH_VARARGS, // indicates the calling convention to be used for the C function. It is usually this one or METH_VARARGS | METH_KEYWORDS
        "Computes the nth factorial number."
    },
    {
        "custom_sum",  
        custom_sum_handler, 
        METH_VARARGS, // indicates the calling convention to be used for the C function. It is usually this one or METH_VARARGS | METH_KEYWORDS
        "Computes the hypotenuse of a right triangle, given its legs."
    },
    {NULL, NULL, 0, NULL}        /* Sentinel */
};

// Module definition structure
static struct PyModuleDef module_first = {
    PyModuleDef_HEAD_INIT,
    "module_first",
    "module_first documentation\n",
    -1,
    module_first_methods
};

PyMODINIT_FUNC PyInit_module_first(void) {
    PyObject *m;

    m = PyModule_Create(&module_first);
    if (m == NULL)
        return NULL;

    module_firstError = PyErr_NewException("module_first.error", NULL, NULL);
    Py_XINCREF(module_firstError);
    if (PyModule_AddObject(m, "error", module_firstError) < 0) {
        Py_XDECREF(module_firstError);
        Py_CLEAR(module_firstError);
        Py_DECREF(m);
        return NULL;
    }

    return m;
}