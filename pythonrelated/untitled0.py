#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 13:24:50 2017

@author: haichunkan
"""
import random
class Minister():
    def __init__(self,name):
        self.name=input("Name:")
    def Name(self):
        return self.name
class Qua_Economy(Minister):
    def qoe(self):
        return int(random.random()*10)+1
class Qua_Agricultural(Minister):
    def qoa(self):
        return int(random.random()*10)+1
class Qua_Politics(Minister):
    def qop(self):
        return int(random.random()*10)+1
class Qua_Military(Minister):
    def qom(self):
        return int(random.random()*10)+1
    