#!/bin/python3

import sys
import math


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    
    a = 1
    for i in range(2, n + 1):
        a = abs(a*i) // math.gcd(a, i)
    print(a)