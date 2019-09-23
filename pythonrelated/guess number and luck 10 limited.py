#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  9 22:04:01 2017

@author: haichunkan
"""

n=100
m=0
import random
a=int(random.random()*11)
b=input("Guess the number of a, 0<=a<=10. Your answer: a=")
for i in range (0,10):
    if a==b and m<10:
        print"Congradulations! You got the true number!"
        print"Your luck:", n
        exit()
    else:
        n=n-10
        m=m+1
        if m<10:
            print"You got the wrong number!"
            print"Your luck:",n 
            b=input("Try again! a=")
        else:
            print"You lost!"
print"a=",a
       
        
        
        
    