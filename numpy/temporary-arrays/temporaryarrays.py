# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 20:51:04 2019

@author: Jouni
"""

import numpy
#from memory_profiler import profile


@profile
def main():
    a = numpy.random.rand(1000)
    b = numpy.random.rand(1000)

    c = a - b
    
    d = a[:, numpy.newaxis] - b

    print(d.shape)
    
    print(d.itemsize * d.size / 1024.0**2, 'MiB')
    
    e = (numpy.sin(a) + numpy.cos(b)) + 2.0 * a - 4.5 * b
    f = 2.0 * a
    f -= 4.5 * b
    f += numpy.sin(a)
    f += numpy.cos(b)

    
    
if __name__ == '__main__':
    main()
    