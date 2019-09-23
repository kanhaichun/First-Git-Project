#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 09:44:39 2018

@author: haichunkan
"""

numv=input()
pov=[]
for i in range(0,int(numv)):
    position=input()
    pov.append(int(position))    
pov.sort()
sov=[]
for i in range(1,len(pov)-1):
    size=(pov[i+1]-pov[i-1])/2
    sov.append(size) 
sov.sort()   
print (sov[0])        