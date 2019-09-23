#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 12:49:46 2017
explore the universe
@author: haichunkan
"""
import random
x=0
y=[]
price=[10000,5000,1000]
amount=[50,200,200]
num_players = input("How many players?")
player_names=[]
money=[]
own=[]
stuff=["star","planet","satellite"]
for i in range (0,num_players):
   a=raw_input("Player name:")
   player_names.append(a)
   money.append(100000)
   own.extend((0,0,0))
   y.append(1)
random.shuffle(player_names)   
num_rounds=input("How many rounds do you want to play?")
print"Great! Enjoy your space exploration!"
for ii in range (0,num_rounds):
    if ii>0:
        if x>=0:
            print"News! The price has increased by",x,"."
        else:
            print"News! The price has decreased by",-x,"."
    for iii in range (0,num_players):
        print"player",player_names[iii],", it's your turn! Start your space trip!"
        trip=int(random.random()*2)
        change=int(random.random()*10000)
        if trip==0:
            money[iii]+=change
            print"You just came across a comet! Money+",change
        else:
            money[iii]-=change
            print"You just crashed into a pile of space rubbish! Money-",change
        
        if money[iii]>10000:
            luck=raw_input("Do you want to spend $5000 to have another space trip(risky)? Y= yes, N= no.")
            if luck=="Y":
                trip=int(random.random()*5)
                change=int(random.random()*1000000)
                if trip==0:
                        money[iii]+=change
                        print"You just find a new glaxy! Money+",change
                if trip==1:
                        money[iii]-=change/1000
                        print"You just came across a meteorolite! Money-",change/1000
                if trip==2:
                        money[iii]+=change/1000
                        print"You just find a nebula! Money+",change/1000
                if trip==3:
                        money[iii]=0
                        print"Your spaceship is out of power! All your money will be taken. What a shame!"
                        print"Your money:$",money[iii]
                else:
                    print"You just came across a black hole! All your achievements will be removed!"
                    money[iii]=0
                    for vii in range(0,len(stuff)):
                         own[3*iii+vii]=0
            else:
                print"Thank You!"
        for vi in range(0,len(stuff)):
            print"There are",amount[vi],stuff[vi],"s available in storage."
            print"The price for a",stuff[vi],"is $",price[vi],"."
            print"You own",own[3*iii],stuff[vi]
        print"You have $",money[iii],"now."        
                
        b=""
        while b!="F":
            b=raw_input("Do you want to buy or sell or finish your turn? B=buy,S=sell,F=finished.")
            if b=="B" or b=="S":
                if b=="B":
                    c=input("What do you want to buy? Star or planet or satellite? 1=star, 2= planet, 3= satellite.")
                    d=input("How many do you want to buy? Quantity:")
                    while d>amount[c-1] or money[iii]-price[c-1]*d<0 or c>3 or c<1:
                        d=input("Stuff/your money not available! Try again! Quantity you want to buy:")
                if b=="S":
                    c=raw_input("What do you want to sell? Star or planet or satellite? 1=star, 2= planet, 3= satellite.")
                    d=input("How many do you want to sell? Quantity:")
                    while d>own[3*iii+c-1] or c>3 or c<1:
                        d=input("Your storage not available! Try again! Quantity you want to sell:")
                    d=-d
                money[iii]-=price[c-1]*d
                own[3*iii+c-1]+=d
                amount[c-1]+=-d
                price[c-1]*=1+int(d/amount[c-1]*100)*0.01
                print"Your money available:", money[iii]
                print"Another decision?"
            else:
                if b!="F":
                    print"You entered the wrong letter. Please try again."
            
    x=int(random.random()*3)*0.1-0.3
    for vi in range(0,len(amount)):
        price[vi]*=1+x
print"All rounds finished! Now caculate your glaxy value!(Satellites will improve the productivity of planets, and planets will improve the productivity of stars.)"    
for iv in range(0,len(player_names)):
    money[iv]+=own[3*iv]*price[0]*(1+own[3*iv+1]*0.05)*(1+own[3*iv+2]*0.025)+own[3*iv+1]*price[1]*(1+own[3*iv+2]*0.05)+own[3*iv+2]*price[2]
    print player_names[iv], money[iv]
print"Final Score:"    
for v in range (0,len(player_names)):
    m=0
    while money[m]!=max(money):
        m+=1
    print v+1,player_names[m],"with $",money[m],"value"
    del player_names[m]
    del money[m]
    
        
        
        