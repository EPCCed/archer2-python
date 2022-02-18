from setuptools import Extension, setup
from Cython.Build import cythonize, build_ext


extensions = [
    Extension("wrapper", ["wrapper.pyx"],
         compiler_directives={'language_level' : "3"},
         libraries=["wrapper"],
         library_dirs=["."]),
    ]

setup (
    name = "Fake",
    cmdclass = {"build_ext": build_ext},
    ext_modules = cythonize(extensions),
)
