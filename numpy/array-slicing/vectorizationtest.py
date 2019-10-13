# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 00:00:42 2019

@author: Jouni
"""

# brute force using a for loop
import timeit
import numpy

t1 = timeit.timeit(
            stmt = "for i in range(1, len(arr)):\n" +
                   "    dif[i-1] = arr[i] - arr[i-1]",
            setup="import numpy; arr = numpy.arange(1000); dif = numpy.zeros(999, int)", number=100)
print(t1)

# vectorised operation
t2 = timeit.timeit(
        stmt="dif = arr[1:] - arr[:-1]",
        setup="import numpy; arr=numpy.arange(1000)", number=100)
arr = numpy.arange(1000)
dif = arr[1:] - arr[:-1]
print(t2)

