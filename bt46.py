# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 13:09:57 2024

@author: PC
"""

bo_nghiem = []
for x in range(1,490):
    for y in range(1,140):
        for z in range(1,110):
            if 2*x + 7*y + 9*z == 979:
                bo_nghiem += [(x,y,z)]
if bo_nghiem:
    print(bo_nghiem)