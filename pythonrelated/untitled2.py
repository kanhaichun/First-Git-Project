#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 13:01:46 2018

@author: haichunkan
"""
k1=[0,0.2,0.4,0.6,0.8]
e1=[32.05,7.98,-7.32,-21.43,-34.58]
k2=[0.1,0.3,0.5,0.7,0.9]
e2=[29.8,14.2,2.93,-8.11,-25.06]
import matplotlib.pyplot as plt
plt.plot(k1, e1, color='green')
plt.plot(k2, e2, color='orange')
plt.title('haha')
plt.show()