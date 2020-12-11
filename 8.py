#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
    n,k = input().strip().split(' ')
    n,k = [int(n),int(k)]
    num = input().strip()
    
    bp = 0
    
    for i in range(n - k + 1):
        prod = 1
        for j in range(i, i + k):
            prod *= int(num[j])
        bp = max(bp, prod)
        
    print(bp)