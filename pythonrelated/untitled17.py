#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 15 12:37:01 2018

@author: haichunkan
"""
import random
num=int(random.random()*10000)
list1=[0,111,555,1111,2222,3333,4444,5555,6666,7777,8888,9999]
lowest=list1[0]
highest=list1[-1]
while  list1.index(highest)-list1.index(lowest)!=1:
    index=(list1.index(highest)+list1.index(lowest))//2
    if list1[index]<num:
        lowest=list1[index]
    if list1[index]>num:
        highest=list1[index]
print(list1[list1.index(highest)],"is just greater than",num)