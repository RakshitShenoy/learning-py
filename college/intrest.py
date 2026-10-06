# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 11:38:49 2026

@author: hp210
"""

p=float(input("enter principle ammount: "))
y=float(input("enter years:  "))
r=float(input("enter rate of intrest:  "))
n=1.0
n2=n*y
iii=1.0*(r/n)
si = (p*r*y)/100
ci=float(p(pow(iii,n2)))
print("simple intrest is : ",si)
print("compund intrest is :  ",ci)
