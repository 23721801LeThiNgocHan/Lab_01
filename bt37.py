# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 15:16:54 2024

@author: PC
"""

s=0
n=int(input("Nhap N: "))
while n<=0 and n%2!=0:
    n=int(input(" Hay nhap lai N: "))
if n>0 and n%2==0:
  for i in range(2,n+1,2):    
      s+=i
  print(f"Tong S la: {s}")
else:
    print("Hay nhap lai")