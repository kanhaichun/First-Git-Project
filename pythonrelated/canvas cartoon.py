#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 13:33:15 2017

@author: haichunkan
"""
import time
import tkinter
from tkinter import *
canvas = tkinter.Canvas(width=400,height=400,bg="white")
filename=tkinter.PhotoImage(file="image1.jpg")
image01=canvas.create_image(10,10,image=filename)
canvas.pack()
for x in range(0,60):
    C.move(1,5,5)
    top.update()
    time.sleep(0.6)