from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize

extensions = [Extension('cython_example',
                        ['cython_example.pyx', 'cython_example.cpp'],
                        language="c++",
                    )]
setup(
    name='cython_example', 
    ext_modules=cythonize(extensions)
)