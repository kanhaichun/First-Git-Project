#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 13:48:56 2018

@author: haichunkan
"""

import random
import datetime
class playerInformation():
    def __init__(self):
        self.first_name=input("Your first name:")
        self.last_name=input("Your last name:")
        
    def option(self):
        self.option=input("Your level:")
   
    
class quiz():
    def LvOne():
        score=0
        for i in range (0,2):
            j=random.randint(0,2)
            a=random.randint(0,10)
            b=random.randint(0,10)
            if j==0:
                q=str(a)+"+"+str(b)+"="
                user_answer=input(q)
                if str(a+b)==user_answer:
                    print(True)
                    score+=1
                else:
                    print(False)
            if j==1:
                q=str(a)+"-"+str(b)+"="
                user_answer=input(q)
                if user_answer==str(a-b):
                    print(True)
                    score+=1
                else:
                    print(False) 
    def LvTwo(self):
        for i in range (0,2):
            j=random.randint(0,2)
            a=random.randint(0,100)
            b=random.randint(0,100)
            if j==1:
                user_answer=input(a,"+",b)
                if user_answer==a+b:
                    print(True)
                    self.score+=1
                else:
                    print(False)
            if j==2:
                user_answer=input(a,"-",b)
                if user_answer==a-b:
                    print(True)
                    self.score+=1
                else:
                    print(False) 
    def LVThree(self):
        for i in range (0,2):
            j=random.randint(1,5)
            a=random.randint(0,100)
            b=random.randint(0,100)
            if j==1:
                user_answer=input(a,"+",b)
            if user_answer==a+b:
                print(True)
                self.score+=1
            else:
                print(False)
            if j==2:
                user_answer=input(a,"-",b)
                if user_answer==a-b:
                    print(True)
                    self.score+=1
                else:
                    print(False)        
            if j==3:
                user_answer=input(a,"*",b)
                if user_answer==a*b:
                    print(True)
                    self.score+=1
                else:
                    print(False)
            if j==4:
                user_answer=input(a,"/",b)
                if user_answer==a/b:
                    print(True)
                    self.score+=1
                else:
                    print(False)
        
playerInformation()
if playerInformation.option=="one":
    quiz.LvOne()
if playerInformation.option=="two":
    quiz.LvTwo()
if playerInformation.option=="three":
    quiz.LvThree()    
                    