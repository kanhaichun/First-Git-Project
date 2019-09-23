#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 13:26:22 2017

@author: haichunkan
"""

def appointment(patient_name,time,work):
    for i in range(0,p):
        print i+1,patient_name[i],time[i],work[i]
    return
def add(patient_name,time,work):
    m=input("Which period do you want to make an appointment?(1-4)")
    patient_name[m-1]=raw_input("Patient_name:")
    time[m-1]=raw_input("Time:")
    work[m-1]=raw_input("Work:")
    return
def delete(patient_name,time,work):
    del patient_name[n-1],time[n-1],work[n-1]
    return

p=0
patient_name=["","","",""]
time=["","","",""]
work=["","","",""]

choice=""
while choice!="f":
    choice=raw_input("Do you want to add,edit,or delete an appointment?a=add,e=edit,d=delete,f=finish.")
    if choice=="a":
        p+=1
        if p>4:
            print"Your time is full!"
            continue
        else:
            add(patient_name,time,work)    
    if choice=="e":
        ii=input("Which period do you want to make change in?(1-4)")
        content=input("What do you want to change?1=patient name,2=time,3=work")
        if content==1:
            patient_name[ii-1]=raw_input("Enter your new information here:")
        if content==2:
            time[ii-1]=raw_input("Enter your new information here:")
        if content==3:
            work[ii-1]=raw_input("Enter your new information here:")    
    if choice=="d":
        n=input("Which period of work do you want to delete?")
        delete(patient_name,time,work)
    print"Your appointment:",appointment(patient_name,time,work)       