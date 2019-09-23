#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 20:33:20 2017
#    
@author: haichunkan
"""
n=100
m=0
import random
a=int(random.random()*555)
print"Guess the number of a, 0<=a<=555."
b=input("Have a guess now!")
for i in range(0,10):
     if a==b and m<10:
         print"You got the number! Congradulations!"
         print"Your luck:",n
         exit()
     else:
         
         n=n-10
         m=m+1
         if m<10:
             print"Try again!"
             if a<b:
                 print"a is smaller."
             if a>b:
                 print"a is larger."
             print"Good luck!"
             b=input("Have a guess again!")
         else:
             print"You lost! Better luck next time!"
print "Your luck:",n
print"a=",a
     
     
    
 