#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 12:46:21 2017

@author: haichunkan
"""

a=raw_input("What's your team's name?")
b=raw_input("Player_name:")
c=input("Total number of games:")
record=[]
total=0
for i in range (0,c):
    print"Game",i+1,"has finished!"
    record.append(input("Your score is:"))
    total+=record[i]
print b,"in",a,":"
for ii in range(0,c):
    print"Game",ii+1,record[ii],"pts"
print"Total pts",total
print"Avg pts",round(total*1.0/c,2)