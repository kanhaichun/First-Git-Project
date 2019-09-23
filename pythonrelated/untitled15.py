#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 11:16:11 2018

@author: haichunkan
"""

numv=5
pov=[16,0,10,4,15]
pov.sort()
sov=[]
for i in range(1,len(pov)-1):
    size=(pov[i+1]-pov[i-1])/2
    sov.append(size) 
sov.sort()   
print ("the smallest neighbourhood size is",sov[0])