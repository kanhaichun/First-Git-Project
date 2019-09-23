#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 13:22:32 2017

@author: haichunkan
"""
import random
class planet:
    name=""
    product=1000
    population=100
    satellite=10
planets=[]    
for i in range(0,10):
    tempplanet=planet()
    tempplanet.name="Planet "+str(input("name your planet:"))
    tempplanet.product=int(random.random()*1000)+1
    tempplanet.population=int(random.random()*100)+1
    tempplanet.satellite=int(random.random()*10)+1
    planets.append(tempplanet)
print ("planet product population satellite")
for i in range(0,10):
    print (planets[i].name,":", planets[i].product, planets[i].population, planets[i].satellite)
        
    