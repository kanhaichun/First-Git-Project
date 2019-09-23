#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 11:31:19 2018

@author: haichunkan
"""
a=0
w=input()
k=[]
for i in range(2,int(w)+1):
   k.append(i) 
k.reverse()   
for i in k:
    n=0
    for j in range(1,int(w)+1):
        if i*j<=int(w):
            n+=1
            if n>1:
                break
            else:
                a+=1
        else:
            break
print(a)        