# shotpy


The example pybind11 .so file was build using this: 
c++ -O3 -Wall -shared -std=c++11 -fPIC $(python3-config --includes) -Iextern/pybind11/include pybind11_example.cpp -o pybind11_example$(python3-config --extension-suffix)