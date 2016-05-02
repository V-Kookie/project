# -*- coding: utf-8 -*-
"""
Created on Tue Jan 13 11:21:43 2015

@author: vhd
"""

import scipy
import matplotlib.pyplot as plt
def f1(x):
    return scipy.cos(x)
def f2(x):
    return scipy.cos(2*x)
f3 = lambda x: scipy.cos(3*x)
f4 = lambda x: scipy.cos(4*x)
listf = [f1,f2,f3,f4]
x = scipy.linspace(0,2*scipy.pi,1000)
fig = plt.figure()
ax = fig.add_subplot(242)
ax1 = fig.add_subplot(241)

fig.show()
i=1
for i in range(1,100):
    for f in listf:
        y = f(x)
        ax.clear()
        ax1.clear()
        ax.plot(x,y,'r')
        ax1.plot(x,y,'b')
        plt.pause(0.1)
    i+=1