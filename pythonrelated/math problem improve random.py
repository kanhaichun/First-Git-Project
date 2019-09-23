#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 14:03:32 2017

@author: haichunkan
"""
score=0
num=10
import random
for i in range (0,num):
 a=int(random.random()*10)
 b=int(random.random()*10)
 c=int(random.random()*4)+1
 print"a=",a,"b=",b
 
 if c==1:
     d = a+b
     e=input("What is a+b?")
 if c==2:
     d=a-b
     e=input("What is a-b?")
 if c==3:
     d=a*b
     e=input("What is a*b?")
 if c==4:
     d=round(a*1.0/b,3)
     e=input("What is a/b(round to 3 decimal places?")
 if d==e:
     print"You are right!"
     score +=10
 else:
     print"You are wrong!"
print"Your final score is:",score     
    
     
     
    
 
 
     
    
    
    
       
        
     
    
    
