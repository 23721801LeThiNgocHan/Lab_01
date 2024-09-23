# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 14:08:32 2024

@author: PC
"""

s=0
n=int(input("Nhap N: "))
while n<=0:
    n=int(input("Nhap N: "))
for i in range(1,n+1):
    s+= i/(i+1)
print(round(s,2))