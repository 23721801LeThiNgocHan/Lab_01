# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 13:31:29 2024

@author: PC
"""

month = 0
year = 0

while month < 1 or month > 12:
    month= int(input("Nhap thang (1-12): "))
    if month <1 or month >12:
        print("Thang khong hop le. Hay nhap lai")

year=int(input("Nhap nam: "))

nhuan=False
if year%4==0 and year%100!=0  or year%400==0:
    nhuan=True
    
if month in [1,3,5,7,8,10,12]:
    days=31
elif month in [4,6,9,11]:
    days=30
elif month==2:
    if nhuan:
        days=29
    else:
        days=28

print(f'Thang {month} nam {year} co {days} ngay')