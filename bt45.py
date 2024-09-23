# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 14:02:17 2024

@author: PC
"""

s=0
ts=0
ms=1
n=int(input("Nhap N: "))
while n<=0:
    n=int(input("Nhap N: "))
x=float(input("Nhap x: "))
for i in range(1,n+1):
    ts = x**i
    ms = ms + i
    s += ts/ms
print(round(s,2))