# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 13:21:13 2024

@author: PC
"""

a=int(input("Nhap N: "))
nghin = a//1000
s=a%1000
tram =s//100
r=s%100
chuc = r//10
don_vi = r%10
T=nghin+tram+chuc+don_vi
if a>0:
    print("Tong N duoc la: ",T)
else:
    print("Nhap lai")