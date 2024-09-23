# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 15:05:26 2024

@author: PC
"""

s=0
n=int(input("Nhap N (N>0): "))
while n<=0:
    n=int(input(" Hay nhap lai N: "))
if n>0:
  for i in range(1,n+1):    
      s+=i
print(f"Tong S la: {s}")