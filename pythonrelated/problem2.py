#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 10:26:50 2018

@author: haichunkan
"""

num=input()
wrong=[[]]
for i in range(0,int(num)):
    for j in range(0,int(num)):
        wd=input()
        wrong[i].append(int(wd))    
for i in range(0,int(num)-1):
    for j in range(0,int(num)-1):
        if wrong[i][j]>wrong[i][j+1] and wrong[i][j]<wrong[i+1][j]:
            for j in range(0,int(num)):
                for i in range(0,int(num)):
                    print(wrong[-(j+1)][i])
        if wrong[i][j]<wrong[i][j+1] and wrong[i][j]>wrong[i+1][j]:
            for i in range(0,int(num)):
                for j in range(0,int(num)):
                    print(wrong[-(i+1)][j])
        if wrong[i][j]<wrong[i][j+1] and wrong[i][j]<wrong[i+1][j]:
            for i in range(0,int(num)):
                for j in range(0,int(num)):
                    print(wrong[-(i+1)][-(j+1)])
        else:
             print(wrong)

   
    
    
    