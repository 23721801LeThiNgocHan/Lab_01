# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 14:48:51 2024

@author: PC
"""

import math
n=int(input("Nhap N: "))
while n<=0:
    print("Hay nhap lai")
a=math.sqrt(n)
if a.is_integer():
    print(f'{n} la so chinh phuong')
else:
    print("Do khong phai la so chinh phuong")