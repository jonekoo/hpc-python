# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 15:47:14 2019

@author: Jouni
"""

import numpy

a = numpy.arange(64)
a.shape = (8, 8)

b,c = numpy.split(a, 2)
print(b)
print(c)

a = numpy.concatenate((b, c))
print(a)

b, c = numpy.split(a, 2, axis=1)
print(b)
print(c)

a = numpy.concatenate((b, c), axis=1)
print(a)