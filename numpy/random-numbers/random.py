# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 18:10:56 2019

@author: Jouni
"""

import numpy

a = numpy.random.rand(1000)
s = numpy.std(a)
m = numpy.mean(a)

print(m, s)

b = numpy.random.randn(1000)
s = numpy.std(b)
m = numpy.mean(b)

print(m, s)
