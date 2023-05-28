#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  7 08:33:43 2019

@author: caceres
"""
print("This program will output the amount of chocolate bars that will satisfy the maximum calorie amount of your Basal Metabolic Rate")
Weight = float(input("Enter Weight in Pounds: "))
Height = float(input("Enter Height in Inches: "))
Age = float(input("Enter Age in Years: "))
S = (input("Gender (M or F): "))
if S == 'F':
    Calories = (655+(4.3 * Weight)+(4.7 * Height)-(4.7 * Age))
    print(Calories/230, "Chocolate Bars")
elif S == 'M':
    Calories = (66+(6.3 * Weight)+(12.9 * Height )-(6.8 * Age))
    print(Calories/230, "Chocolate Bars")
print("Done")
    
    