# shotpy


The example pybind11 .so file was build using this: 
c++ -O3 -Wall -shared -std=c++11 -fPIC $(python3-config --includes) -Iextern/pybind11/include pybind11_example.cpp -o pybind11_example$(python3-config --extension-suffix)

The example swig .so file was build using this:
swig -c++ -python swig_example.i
python swig_setup.py build_ext --inplace



Useful links:
https://medium.com/@brandon.a.alvarez1/python-wrappers-and-c-supercharge-your-projects-c18ffe8476c6