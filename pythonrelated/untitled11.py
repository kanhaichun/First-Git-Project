#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 17:20:23 2018

@author: haichunkan
"""

first_name=input("Your first name:")
last_name=input("Your last name:") 
fn=list(first_name)
ln=list(last_name)
if ord(fn[0])>=97 and ord(fn[0])<=122:
    fn[0]=chr(ord(fn[0])-32)
if ord(ln[0])>=97 and ord(ln[0])<=122:
    ln[0]=chr(ord(ln[0])-32)
initials=fn[0]+ln[0]
print (initials)
num=int(input("number of questions:"))
        for i in range (0,num):
            j=random.randint(1,4)
            a=random.randint(0,100)
            b=random.randint(0,100)
            if j==1:
                q=str(a)+"+"+str(b)+"="
                user_answer=input(q)
                if str(a+b)==user_answer:
                    print(True)
                    self.score+=1
                else:
                    print(False)
            if j==2:
                q=str(a)+"-"+str(b)+"="
                user_answer=input(q)
                if str(a-b)==user_answer:
                    print(True)
                    self.score+=1
                else:
                    print(False)        
            if j==3:
                b=random.randint(0,10)
                q=str(a)+"*"+str(b)+"="
                user_answer=input(q)
                if str(a*b)==user_answer:
                    print(True)
                    self.score+=1
                else:
                    print(False)
            if j==4:
                q=str(a)+"/"+str(b)+"="
                user_answer=input(q)
                if str(int(a/b))==user_answer:
                    print(True)
                    self.score+=1
                else:
                    print(False)