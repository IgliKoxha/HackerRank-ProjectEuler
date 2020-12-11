#!/bin/python3

import sys

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    three = int((n - 1) / 3)
    five = int((n - 1) / 5)
    fifteen = int((n - 1) / 15)
    
    print(int(
    ((3 + three * 3) * three // 2)
    + ((5 + five * 5) * five // 2)
    - ((15 + fifteen * 15) * fifteen // 2)
    ))
