#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 16:35:32 2018

@author: haichunkan
"""


import time
class Quiz():
    def playerInformation(self):
        self.first_name=input("Your first name:")
        self.last_name=input("Your last name:") 
        fn=list(self.first_name)
        ln=list(self.last_name)
        if ord(fn[0])>=97 and ord(fn[0])<=122:
            fn[0]=chr(ord(fn[0])-32)
        if ord(ln[0])>=97 and ord(ln[0])<=122:
            ln[0]=chr(ord(ln[0])-32)
        self.initials=fn[0]+ln[0]    
    def quizQuestions(self):
        self.score=0
        D={"What is as fast as a cheetah and as slow as a tortoise?":"shadow","What belongs to you but others use it more than yourself?":"name","How long do you need to finish reading a book":"one second","What is the largest ant in the world?":"elephant","What kind of tables do not have legs?":"vegetables"}
        Dk=list(D.keys())
        Dv=list(D.values())
        for i in range (0,len(Dk)): 
            print(Dk[i])
            answer=input("Your answer:")
            if answer==Dv[i]:
                print ("True")
                self.score+=1
            else:
                print("False")
            self.c= str((i+1)*100/len(Dk))+"%"  
            print("You have completed",self.c)        
    def date(self):
        self.time=time.strftime('%Y%m%d%H%M%S')
           
    def file(self):
        self.name="quiz"+self.time+self.initials+".txt"
        File = open(self.name,'w')
        File.write(self.name)
        File.write("Name:"+self.first_name+self.last_name)
        File.write("Completeness:"+self.c)
        File.write("Score:"+str(self.score))
        File.close()
q=Quiz()        
q.playerInformation()
q.quizQuestions()
q.date()
q.file()

                   