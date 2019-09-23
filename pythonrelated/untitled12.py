#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  9 12:54:29 2018

@author: haichunkan
"""
'''
list1=[3,5,4,8,7,2,1,6]
while
    for i in range(0,len(list1)-1):
        if list1[i]>list1[i+1]:
            
            a=list1[i]
            list1[i]=list1[i+1]
            list1[i+1]=a
print(list1)        
'''
def shortBubbleSort(alist):
    exchanges = True
    passnum = len(alist)-1
    while passnum > 0 and exchanges:
       exchanges = False
       for i in range(passnum):
           if alist[i]>alist[i+1]:
               exchanges = True
               temp = alist[i]
               alist[i] = alist[i+1]
               alist[i+1] = temp
       passnum = passnum-1

alist=[3,1,8,4,2,5,9,7,6]
shortBubbleSort(alist)
print(alist)        
        

