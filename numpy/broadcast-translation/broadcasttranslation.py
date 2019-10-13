# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 15:57:56 2019

@author: Jouni
"""
import numpy
import matplotlib.pyplot as plt

points = numpy.loadtxt('points_circle.dat')

print(points)
plt.plot(points[:,0], points[:,1], 'bo')
plt.gca().set_aspect('equal')
new_points = points + numpy.array((2.1, 1.1))
plt.plot(new_points[:,0], new_points[:,1], 'r+')
plt.show()