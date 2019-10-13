# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 18:21:27 2019

@author: Jouni
"""

import numpy

A = numpy.arange(-2, 2)
B = numpy.arange(0, 4)
A.shape = (2, 2)
B.shape = (2, 2)

A += A.T
B += B.T

C = numpy.dot(A, B)
print(A, "\n", B, "\n", C)
print(numpy.linalg.eigvals(C))
