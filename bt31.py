# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 13:50:06 2024

@author: PC
"""

a=int(input("Nhap a: "))
b=int(input("Nhap b: "))
c=int(input("Nhap c: "))
if a<=0 or b<=0 or c<=0:
   print("Hay nhap lai")
if a+b>c and a+c>b and b+c>a:
    if a==b and b==c:
       print("Day la tam giac deu")
    elif a==b or b==c or a==c:
       print("Day la tam giac can")
    elif a*a + b*b == c*c or a*a + c*c == b*b or b*b + c*c == a*a:
       print("Day la tam giac vuong")
    else:
       print("Day la tam giac thuong")
else:
       print("Day khong phai 1 tam giac")