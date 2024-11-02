#include <iostream>
#include <pybind11/pybind11.h>


namespace py = pybind11;

int main() {
    std::cout << "Hello World!\n";
    return 0;
}

PYBIND11_MODULE(pybind11_example, m) {
    m.doc() = "pybind11 example plugin"; // optional module docstring

    m.def("main", &main, "A function that prints 'Hello World!'");
}