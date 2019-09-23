#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 13:20:24 2017

@author: haichunkan
"""
import random
class mob():
    def __init__(self,name,species):
        self.name=name
        self.species=species
        self.mass=int(random.random()*100)+1
    def Name(self):
        return self.name
    def Species(self):    
        return self.species
    def _str_(self):
        return "%s is a %s"%(self.name, self.species)
class farm_animal(mob):
    def __init__(self,name,needtofeed):
        mob.__init__(self,name,"a farm animal")
        self.needtofeed= needtofeed
    def Needtofeed(self):
        return self.needtofeed
    def Mass(self):
        return self.mass
    def __add__(self,other1,other2):
        return (self.mass+other1.mass+other2.mass)
class monster(mob):
    def __init__(self,name,attackhuman):
        mob.__init__(self,name,"a monster")
        self.attackhuman=attackhuman
    def Attackhuman(self):
        return self.attackhuman
    
mob1=mob("hg","jhg")
print(mob1.Name(),mob1.Species(),mob1._str_())
farm_animal1=farm_animal("e",True)
farm_animal2=farm_animal("f",True)
farm_animal3=farm_animal("g",True)
print(farm_animal1.Name(),farm_animal1.Needtofeed(),farm_animal1.__add__(farm_animal2,farm_animal3))
monster1=monster("drm",True)
print(monster1.Name(),monster1.Attackhuman())    
