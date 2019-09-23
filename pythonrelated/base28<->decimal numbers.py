#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 13:41:30 2017

@author: haichunkan
"""
list4=[]
num=134847630546
while num>0:
    r=num%28
    if r<=9:
        list4.append(chr(r+48))
    else:
        list4.append(chr(r+55))
    num=int(num/28)
list4.reverse()
result="".join(list4)
print(result)

x=0
num="A743HD8042MQ" 
list2=[]
for i in num:
    if ord(i)<=59:
        list2.append(ord(i)-48)
    if ord(i)>=65:
        list2.append(ord(i)-55)
for ii in range(0,len(list2)):
     x+=list2[ii]*28**ii
print(x)     