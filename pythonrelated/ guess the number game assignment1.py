#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 12:43:54 2017

@author: haichunkan
"""
import random
guess=0
print"Welcome to the Guess the Number game!"
number=int(random.random()*50)+1
player_number=input("Guess a number between 1 and 50:")
while player_number!=number:
    if player_number>number:
        player_number=input("Too high,try again:")
    else:
        player_number=input("Too low,try again:")
    guess+=1
print "You guessed it! You win!"           
print"It took",guess+1,"Guesses to win the game."            