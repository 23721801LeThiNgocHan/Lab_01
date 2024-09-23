# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 14:17:46 2024

@author: PC
"""

s=float(input("Nhap quang duong di duoc (km): "))
tien=0
if s<=1:
        tien = 15000
        print(f'So tien cua ban la {tien} VND')
elif 1<s<=5:
        tien = 15000 + (s-1)*13500
        print(f'So tien cua ban la {tien} VND')
elif s>5:
        tien = 15000 + (s-1)*13500 + (s-6)*11000
        print(f'So tien cua ban la {tien} VND')
        if s>120:
          tien=tien*0.9
          print(f'So tien cua ban da duoc giam con {tien} VND')
else:
    print("Hay nhap lai")