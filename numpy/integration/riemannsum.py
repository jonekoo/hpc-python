# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 22:08:15 2019

@author: Jouni
"""
import numpy

for dx in [0.1, 0.01, 0.001]:
    xi = numpy.arange(0, numpy.pi/2, dx)
    xmid = (xi[1:] + xi[:-1]) / 2.
    f = numpy.sin
    s = sum(f(xmid) * dx)
    print("dx = ", dx, "sum = ", s)