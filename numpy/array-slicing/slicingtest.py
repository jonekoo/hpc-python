# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 23:47:02 2019

@author: Jouni
"""
a = numpy.random.rand(4, 4)
print(a)

print(a[1, :])
print(a[:, 2])
a[:2,:2] = 0.21
print(a)

b = numpy.zeros((8, 8))
b[0::2, 0::2] = 1
b[1::2, 1::2] = 1
print(b)

