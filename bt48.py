# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 13:14:21 2024

@author: PC
"""
min = 979
bo_nghiem = []
for x in range(1,490):
    for y in range(1,140):
        for z in range(1,110):
            if 2*x + 7*y + 9*z == 979:
                tong = x+y+z
                if tong < min:
                    min = tong
                    bo_nghiem = [(x,y,z)]
if bo_nghiem:
    print(f'{bo_nghiem} voi {x+y+z} = {min}')