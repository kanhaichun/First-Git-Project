#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 13:06:51 2017

@author: haichunkan
"""

import random
num_rounds=input("How many rounds do you want to play?")
num_players=input("How many players?")
player_names=[]
money=[]
stocks=["Diamond","Gold","Silver","Copper","Stone"]
num_stocks=len(stocks)
stock_prices=[100,100,100,100,100]
portfolio=[[1000 for x in range(num_stocks)] for y in range(num_players)]
for i in range(0,num_players):
    player_names.append(raw_input("Player name:"))
    money.append(5000)
for ii in range(0,num_rounds):
    for iii in range (0,len(player_names)):
        print"player",player_names[iii],", it's your turn!"
        for v in range(0,len(stocks)):    
            stock_prices[v]+=int(11*random.random())-5
            if stock_prices[v]<0:
                portfolio[iii][v]=0    
            if ii>0 and random.random()<0.2:
                percentage=int(20*random.random()+1)
                print"You get a dividend of",percentage,"% for",stocks[v]
                money[iii]+=percentage/100.0*stock_prices[v]*portfolio[iii][v]
            if stock_prices[v]>200:
                portfolio[iii][v]*=2
                stock_prices[v]=100
        for iv in range(0,len(stocks)):
            print"The price for ",stocks[iv],"is $",stock_prices[iv],"."
            print"You own",portfolio[iii][iv]
        print"You have $",money[iii],"now."
        choice=""
        while choice!="F":
            choice=raw_input("Do you want to buy or sell or finish your turn? B=buy,S=sell,F=finished.")
            if choice=="B":
                c=input("What do you want to buy? 1=Diamond,2=Gold,3=Silver,4=Copper,5=Stone.")
                d=input("How many do you want to buy? Quantity:")
            if choice=="S":
                c=input("What do you want to sell? 1=Diamond,2=Gold,3=Silver,4=Copper,5=Stone.")
                d=input("How many do you want to sell? Quantity:")
                d=-d
            money[iii]-=stock_prices[c-1]*d
            portfolio[iii][c-1]+=d
            print"You have",stocks[c-1],"*",portfolio[iii][c-1]
            print"Your money available:", money[iii]
for vi in range(0,num_players):
    for vii in range(0,num_stocks):
        money[vii]+=portfolio[vi][vii]*stock_prices[vii]
    print player_names[vi],money[vi]        
            