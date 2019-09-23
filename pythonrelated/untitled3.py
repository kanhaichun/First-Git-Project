#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 14:14:57 2017

@author: haichunkan
"""

#Read - import required modules
import tkinter
import sys
from math import *

#MenuBar class - called by the main class
class MenuBar(tkinter.Menu):
    #roots - opens a new top level window named filewin
    def roots(self):
        filewin = tkinter.Toplevel(self)
        #Use grid to organize all of the widgets - labels, entries, buttons
        self.title_label = tkinter.Label(filewin,text="Enter quadratic coefficients, a, b and c").grid(row=0,column=0,columnspan=2)
        self.a_label=tkinter.Label(filewin,text="a coefficient:").grid(row=1,column=0)
        self.b_label=tkinter.Label(filewin,text="b coefficient:").grid(row=2,column=0)
        self.c_label=tkinter.Label(filewin,text="c coefficient:").grid(row=3,column=0)
        self.button_label=tkinter.Label(filewin,text="Calculate:").grid(row=4,column=0)
        self.r1_label=tkinter.Label(filewin,text="First Root:").grid(row=5,column=0)
        self.r2_label=tkinter.Label(filewin,text="Second Root:").grid(row=6,column=0)
        self.a_entry = tkinter.Entry(filewin,bd=5,textvariable=tkinter.StringVar(value="0"))
        self.a_entry.grid(row=1,column=1)
        self.b_entry = tkinter.Entry(filewin,bd=5,textvariable=tkinter.StringVar(value="0"))
        self.b_entry.grid(row=2,column=1) 
        self.c_entry = tkinter.Entry(filewin,bd=5,textvariable=tkinter.StringVar(value="0"))
        self.c_entry.grid(row=3,column=1)
        self.calculate = tkinter.Button(filewin, text="Enter", command=self.calculateRoots)
        self.calculate.grid(row=4,column=1)
        #(float(a_entry.Get()), float(b_entry.Get()),float(c_entry.Get())))
        self.rootsLabel1 = tkinter.Label(filewin, textvariable=self.r1)
        self.rootsLabel1.grid(row=5,column=1)
        self.rootsLabel2 = tkinter.Label(filewin, textvariable=self.r2)
        self.rootsLabel2.grid(row=6,column=1)
     
    #Make the mathematical calculations - solves the roots problem 
    def calculateRoots(self):
        #Read values from Entry widgets using get()
        self.a = float(self.a_entry.get()) #convert from string to float 
        self.b = float(self.b_entry.get())
        self.c = float(self.c_entry.get())
        delta = self.b*self.b-4*self.a*self.c #b^2-4ac
        if delta > 0:
            #To change the value of the labels, use set()
            #Change the variable inside the label, not the label
            self.r1.set(str((-self.b+sqrt(delta))/(2*self.a)))
            self.r2.set(str((-self.b-sqrt(delta))/(2*self.a)))
        elif delta == 0:
            self.r1.set(str(-self.b/(4*self.a*self.c)))
            self.r2.set("No second root")
        else:
            self.r1.set("No Roots")
            self.r2.set("")
            
        print (self.r1.get())
    
    def vertex(self):
        filewin = tkinter.Toplevel(self)
        self.title_label = tkinter.Label(filewin,text="Enter quadratic coefficients, a, b and c").grid(row=0,column=0,columnspan=2)
        self.a_label=tkinter.Label(filewin,text="a coefficient:").grid(row=1,column=0)
        self.b_label=tkinter.Label(filewin,text="b coefficient:").grid(row=2,column=0)
        self.c_label=tkinter.Label(filewin,text="c coefficient:").grid(row=3,column=0)
        self.button_label=tkinter.Label(filewin,text="Vertex:").grid(row=4,column=0)
        self.a_entry = tkinter.Entry(filewin,bd=5,textvariable=tkinter.StringVar(value="0"))
        self.a_entry.grid(row=1,column=1)
        self.b_entry = tkinter.Entry(filewin,bd=5,textvariable=tkinter.StringVar(value="0"))
        self.b_entry.grid(row=2,column=1) 
        self.c_entry = tkinter.Entry(filewin,bd=5,textvariable=tkinter.StringVar(value="0"))
        self.c_entry.grid(row=3,column=1)
        
    #Place holder function - allows the program to work partially
    def donothing(self):
        pass
    
    def __init__(self, parent):
        tkinter.Menu.__init__(self, parent)
        #Two special variables - r1 and r2 - members of the MenuBar class
        self.r1 = tkinter.StringVar()
        self.r2 = tkinter.StringVar()
        fileMenu = tkinter.Menu(self, tearoff=False)
        self.add_cascade(label="File",underline=0, menu=fileMenu)
        fileMenu.add_command(label="Exit", underline=1, command=self.quit)
        fileMenu.add_command(label="Roots", command=self.roots)
        fileMenu.add_command(label="Vertex", command=self.donothing)
        self.add_cascade(label="Quadratic Equations", menu=fileMenu)
        editmenu = tkinter.Menu(self, tearoff=0)
        editmenu.add_command(label="Sine Law", command=self.donothing)
        editmenu.add_command(label="Cosine Law", command=self.donothing)
        self.add_cascade(label="Trigonometry", menu=editmenu)
        helpmenu = tkinter.Menu(self, tearoff=0)
        helpmenu.add_command(label="Arithmetic Series", command=self.donothing)
        helpmenu.add_command(label="Geometric Series", command=self.donothing)
        self.add_cascade(label="Sequences and Series", menu=helpmenu)

    def quit(self):
        sys.exit(0)
        
#Main class - calls menubar class
class App(tkinter.Tk):
    def __init__(self):
        tkinter.Tk.__init__(self)
        menubar = MenuBar(self)
        self.config(menu=menubar)

#Start the program:
if __name__ == "__main__":
    app=App()
    app.mainloop()