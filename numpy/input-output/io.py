# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 16:24:39 2019

@author: Jouni
"""
import numpy

a = numpy.loadtxt('xy-coordinates.dat')
print(a)
a[:,1] = a[:, 1] + 2
print(a)
numpy.savetxt('ouput.dat', a)