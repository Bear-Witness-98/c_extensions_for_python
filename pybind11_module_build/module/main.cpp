// Python binding library
#include <pybind11/pybind11.h>
namespace py = pybind11;

#include <ops.h>
#include <misc.h>


PYBIND11_MODULE(main, m) {
    m.doc() = "pybind11 example plugin"; // optional module docstring

    m.def("fibonacci", &fibonacci, "A function that computes the nth fibonacci number");
    m.def("factorial", &factorial, "A function computes the factorial of a number");
    m.def("custom_sum", &custom_sum, "A function that adds two numbers");
}