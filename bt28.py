# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 13:46:07 2024

@author: PC
"""

n=-1
while n<=0:
    n=int(input("Nhap N:"))
    if n<=0:
        print("N la so nguyen duong")
print("Cac uoc so cua N:")
for i in range(1, n+1):
    if n%i ==0:
        print(i)