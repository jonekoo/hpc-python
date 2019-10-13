# -*- coding: utf-8 -*-
"""
This is a temporary script file.
"""
import numpy

l = [0, 1, 1.2, 3, 2.2]
a = numpy.array(l)

b = numpy.arange(-2, 2, 0.2)
print(b)

c = numpy.linspace(0.5, 1.5, 11)
print(c[::2])

s = 'Tarja'
chararr = numpy.array(s, dtype='c')
print(repr(chararr))

