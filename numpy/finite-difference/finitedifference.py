# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 21:55:45 2019

@author: Jouni
"""

import numpy

dx = 0.1
xi = numpy.arange(0, numpy.pi/2, dx)
dfx = (numpy.sin(xi[2:]) - numpy.sin(xi[:-2])) / (2 * dx)
print((numpy.cos(xi[1:-1]) - dfx) / numpy.cos(xi[1:-1]))
print(dfx)
print(numpy.cos(xi))