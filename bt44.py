# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 14:06:38 2024

@author: PC
"""

s=0
n=int(input("Nhap N: "))
while n<=0:
    n=int(input("Nhap N: "))
for i in range(1,n+1):
    s+= (2*i + 1)/(2*i+2)
print(round(s,2))