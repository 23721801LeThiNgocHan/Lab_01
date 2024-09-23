# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 14:55:43 2024

@author: PC
"""

n=int(input("Nhap N: "))
while n<=0:
    print("Hay nhap lai")
    break
if n<2:
    print("Khong phai so nguyen to")
else:
    for i in range(2,n+1):
        if n%i==0:
            print("Day khong phai so nguyen to")
            break
        else:
            print("Day la so nguyen to")
            break