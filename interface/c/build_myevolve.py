# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 19:44:45 2019

@author: Jouni
"""

from cffi import FFI
ffi = FFI()

ffi.cdef("""
         void evolve(double *u, double *u_previous, int nx, int ny,
                     double a, double dt, double dx2, double dy2);
         """)
ffibuilder.set_source("_my_evolve",
"""
    #include "evolve.h"
""",
library_dirs=["."],
libraries=['evolve'])

ffibuilder.compile(verbose=True)
