# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 11:09:59 2026

@author: hp210
"""

# loooooooooooops
for i in range(6):
    for j in range(6-i):
        print(" ",end="")
    for k in range(i+1):    
        print("*",end="")
    print()

for i in range(6):
    for j in range(i+1):
        print("",end=" ")
    for k in range(6-i):    
        print("*",end="")
    print()
