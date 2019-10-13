# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 16:06:10 2019

@author: Jouni
"""
from distutils.core import setup, Extension
from Cython.Build import cythonize
import numpy

setup(
      ext_modules=cythonize("evolve.pyx"), 
      include_dirs=[numpy.get_include()]
)