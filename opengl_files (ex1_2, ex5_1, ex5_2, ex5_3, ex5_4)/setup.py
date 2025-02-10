from setuptools import setup, Extension
from Cython.Build import cythonize
import numpy as np

extensions = [
	Extension("ex1_2", ["ex1_2.pyx"], include_dirs=[np.get_include()], extra_compile_args=["-fopenmp"], extra_link_args=["-fopenmp"]),
	Extension("ex5_1", ["ex5_1.pyx"], include_dirs=[np.get_include()]),
	Extension("ex5_2", ["ex5_2.pyx"], include_dirs=[np.get_include()]),
	Extension("ex5_3", ["ex5_3.pyx"], include_dirs=[np.get_include()]),
	Extension("ex5_4", ["ex5_4.pyx"], include_dirs=[np.get_include()]),
]

setup(
	name="opengl_files (ex1_2, ex5_1, ex5_2, ex5_3, ex5_4)",
	ext_modules=cythonize(extensions, compiler_directives={"language_level": "3"}),
)