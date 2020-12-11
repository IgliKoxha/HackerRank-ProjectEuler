#!/bin/python3

import sys
import math

primes = {}

p = 2
for i in range(1, 10**4+1):
    while(True):
        isPrime = True
        for j in range(2, int(math.sqrt(p) + 1)):
            if p % j == 0: isPrime = False
        if isPrime:
            primes[i] = p
            p+=1
            break
        else:
            p+=1        

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    
    print(primes[n])