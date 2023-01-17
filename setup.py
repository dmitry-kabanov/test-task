from Cython.Build import cythonize
from setuptools import Extension, setup

extensions = [
    Extension(
        name="optimize.functionals",
        sources=["src/optimize/functionals.pyx", "src/optimize/functionals_impl.cpp"],
        include_dirs=["src/optimize"],
        language="c++",
        extra_compile_args=["-std=c++17"],
    )
]

setup(
    ext_modules=cythonize(
        extensions,
        compiler_directives={"language_level": "3"},
    )
)
