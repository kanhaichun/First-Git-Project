#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 13:02:29 2017

@author: haichunkan
"""
#Make the numbers random
import random
a=int(random.random()*10)
#Put the questions in a loop:
for i in range(0,10):
    print "Questions here"

a=0
answer1=input ("Let's start our questions. 1. what is 3*7?")
if answer1 == 21:
    print("You are correct!Your score:10.")
    a=a+10
else:
    print("You are wronbg!Your score:0.")
answer2=input ("Next: 2. what is 18+12?")
if answer2 == 30:
    print("You are correct!+10 points")
    a=a+10
else:
    print("You are wrong!")
answer3=input ("Next: 3. what is 66/11?")
if answer3 == 6:
    print("You are correct!+10 points")
    a=a+10
else:
    print("You are wrong!")
answer4=input ("Next: 4. what is 23-8?")
if answer4 == 15:
    print("You are correct!+10 points")
    a=a+10
else:
    print("You are wrong!")
answer5=input ("LNext: 5. what is 12*12?")
if answer5 == 144:
    print("You are correct!+10 points")
    a=a+10
else:
    print("You are wrong!")
answer6=input ("Next: 6. what is 100/5?")
if answer6 == 20:
    print("You are correct!+10 points")
    a=a+10
else:
    print("You are wrong!")   
answer7=input ("Next: 7. what is 58-40?")
if answer7 == 18:
    print("You are correct!+10 points")
    a=a+10
else:
    print("You are wrong!")
answer8=input ("Next: 8. what is 19*3?")
if answer8 == 57:
    print("You are correct!+10 points")
    a=a+10
else:
    print("You are wrong!")
answer9=input ("Next: 9. what is 36+82?")
if answer9 == 118:
    print("You are correct!+10 points")
    a=a+10
else:
    print("You are wrong!")
answer10=input ("Next: 10. what is 64/8?")
if answer10 == 8:
    print("You are correct!+10 points")
    a=a+10
else:
    print("You are wrong!")
print("You finished!")
print a
    
    
    

