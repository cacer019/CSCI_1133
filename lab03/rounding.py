#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  7 09:13:16 2019

@author: caceres
"""
def roundfloat(x):
    y = int(x)
    if (x > 0) and (x - y) >= 0.5: 
        return(int(x + 1))
    elif (x > 0) and (x - y) < 0.5:
        return(int(x))
    elif (x < 0) and (x - y) <= -0.5:
        return(int(x - 1))
    elif (x - y) and (x - y) > -0.5:
        return(int(x))

x = float(input("Enter a number in decimal form for me to round: "))
print(roundfloat(x))