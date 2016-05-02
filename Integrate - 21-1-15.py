# -*- coding: utf-8 -*-
"""
Created on Wed Jan 21 10:59:42 2015

@author: vhd
"""

from scipy.integrate import quad
import scipy as sc

mh=1
mc=2
def f1(T):
    y=4184+10**(-4)*T+10**(-6)*T**2+10**(-9)*T**3
    return y

i1=quad(f1,303.50937355,373.15)
i2=quad(f1,303.15,337.82138949)
print i1
print i2
i=sc.array((mh*i1[0]) - (mc*i2[0]))
err=i/(mh*i1[0])
print err