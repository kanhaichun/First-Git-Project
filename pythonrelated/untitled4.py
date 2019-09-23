#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 11:03:25 2017

@author: haichunkan
"""
import tkinter
pw=tkinter.Tk()
pc=tkinter.Toplevel()
    CheckVar1=tkinter.IntVar()
    CheckVar2=tkinter.IntVar()
    tkinter.Checkbutton(pc,text="plant a",variable=CheckVar1,onvalue=1,offvalue=0).grid(row=0,column=0)
    tkinter.Checkbutton(pc,text="plant b",variable=CheckVar2,onvalue=1,offvalue=0).grid(row=1,column=0)
    pc.mainloop
pw.mainloop()