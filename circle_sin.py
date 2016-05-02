# -*- coding: utf-8 -*-
"""
Created on Mon Jan 19 11:28:09 2015

@author: vhd
"""

import matplotlib.pyplot as plt
import scipy as sp 

fig=plt.figure(num=None, figsize=(10, 10), dpi=80, facecolor='w', edgecolor='k')
ax=fig.add_subplot(111)
fig.show()
ax.set_xlim([0, 40])
ax.set_ylim([-1.3,1.3])

for a in sp.linspace(0,10*sp.pi,100):
   
    circle = plt.Circle((a,sp.sin(a)), radius=0.1, fc='y')
    plt.gca().add_patch(circle)    
    plt.pause(0.1)
    
    circle1 = plt.Circle((a,sp.sin(-a)), radius=0.1, fc='r')
    plt.gca().add_patch(circle1)    
    plt.pause(0.1)

  