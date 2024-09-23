# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 15:23:54 2024

@author: PC
"""

s=1
n=int(input("Nhap N: "))
while n<=0 or n%2==0:
    n=int(input(" Hay nhap lai N: "))
    
else:   
    for i in range(1, n+1):    
      s *= i
print(f"Tich S la: {s}")
