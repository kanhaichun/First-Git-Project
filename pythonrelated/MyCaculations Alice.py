#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 13:04:11 2017

@author: haichunkan
"""
#define result and ramainder
result=0
remainder=0
#define functions to + - * / and print the result
def letsAdd(firstInteger, secondInteger):
    result=firstInteger+secondInteger
    print firstInteger,"+",secondInteger,"=",result
    return result
def letsSubtract(firstInteger, secondInteger):
    result=firstInteger-secondInteger
    print firstInteger,"-",secondInteger,"=",result
    return result
def letsDivide(firstInteger, secondInteger):
    result=firstInteger/secondInteger
    remainder=firstInteger%secondInteger
    print firstInteger,"/",secondInteger,"=",result,"...",remainder
    return result
def letsMultiply(firstInteger, secondInteger):
    result=firstInteger*secondInteger
    print firstInteger,"*",secondInteger,"=",result
    return result
#let the user enter two integers and use the defined fuctions
#the caculatation will continue or finish according to the user's choice
print"Welcome to My Python Caculator" 
go=True
while go==True:
    firstInteger=input("Enter your first integer:")
    secondInteger=input("Enter your second integer:")
    letsAdd(firstInteger, secondInteger)
    letsSubtract(firstInteger, secondInteger)
    letsDivide(firstInteger, secondInteger)
    letsMultiply(firstInteger, secondInteger)    
    print"Would you like to try again?(True/False)"
    go=input()
print"Thank you for using My Python Caculator!"    