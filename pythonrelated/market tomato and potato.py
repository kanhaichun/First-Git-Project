#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 17:28:24 2017

@author: haichunkan
"""
x=0
p=2
t=2
amount_p=1000
amount_t=1000
import random
num_players = input("How many players?")
player_names=[]
money=[]
own_p=[]
own_t=[]
n=[]
for i in range (0,num_players):
   a=raw_input("Player name:")
   player_names.append(a)
   n.append(a)
   money.append(1000)
   own_p.append(0)
   own_t.append(0)
num_turns=input("How many turns do you want to play?")
print"Welcome! Be a successful businessman!"
for ii in range (0,num_turns):
    if ii>0:
        print"News! The price has changed by",x,"."
    for iii in range (0,num_players):
         b=int(random.random()*num_players)
         name=player_names[b]
         print ii+1,".",iii+1,name
         player_names.remove(name)
         num_players-=1
         print"There are",amount_p,"potatoes and",amount_t,"tomatoes on the market." 
         print"The price for potatoes is",p,"and the price for tomatoes is",t,"."
         print"You own",own_p[b],"potatoes and",own_t[b],"tomatoes."
         print"You have $",money[b],"now."
         if ii>0:
             q=raw_input("Do you want to buy or sell?")
             if q=="buy":
                 c=raw_input("Do you want to buy tomato or potato?")
                 d=input("How many do you want to buy(at most you can afford)? Quantity:")
             else:
                 c=raw_input("What do you want to sell?")
                 d=input("How many do you want to sell(at most the quantity you own)? Quantity:")
                 d=-d
         else:
             c=raw_input("Do you want to buy tomato or potato?")
             d=input("How many do you want to buy(1000/players at most)? Quantity:")
         if c=="tomato":
             money[b]-=t*d
             own_t[b]+=d
             amount_t+=-d
             t=20000/amount_t
             print"Your money left:", money[b]
         if c=="potato":
             money[b]-=p*d
             own_p[b]+=d
             amount_p+=-d
             p*=20000/amount_p
             print"Your money left:", money[b]
         if len(player_names)==0:
             player_names=n
             num_players=iii+1
    x=int(random.random()*5)*0.1-0.5
    p*=1+x
    t*=1+x
money+=own_p*p+own_t*t
print player_names, money        