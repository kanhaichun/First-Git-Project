#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 12:58:34 2017

@author: haichunkan
"""

import random
num_rounds=input("How many rounds do you want to play?")
num_players=input("How many players?")
player_names=[]
money=[]
stocks=["Diamond","Gold","Silver","Copper","Stone"]
stock_prices=[100,100,100,100,100]
portfolio=[1000,1000,1000,1000,1000]
for i in range(0,num_players):
    player_names.append(raw_input("Player name:"))
    money.append(5000)
for round_number in range(0,num_rounds):
    for stock in range(0,len(stocks)):
        x=int(11*random.random())-1
        stock_prices[stock]+=x
        print"stock prices for",stocks[stock], stock_prices
        if stock_prices<0:
            portfolio[stock]=0
            
            
        else:    
            if round_number>0:
                if random.random()<0.2:
                    percentage=int(20*random.random()+1)
                    print"You get a dividend of",percentage,"% for",stocks[stock]
                    money+=percentage/100.0*stock_prices[stock]*portfolio[stock]
            if stock_prices[stock]>200:
                portfolio[stock]*=2
                stock_prices[stock]=100
        print"you have",stocks[stock],"*", portfolio[stock]            
        print "you have $",money
            