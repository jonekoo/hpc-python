# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 22:04:24 2019

@author: Jouni
"""

import numpy
import numexpr


a = numpy.random.rand(10**6)
b = numpy.random.rand(10**6)

c = numpy.sum(a * b)


d = numexpr.evaluate("sum(a * b)")

print(c, d)