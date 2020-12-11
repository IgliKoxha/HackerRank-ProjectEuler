#!/bin/python3

import sys
import math

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    
    while n % 2 == 0:
        n = n >> 1
    
    if n == 1:
        print(2)
        continue
    
    largest_prime = 3
    i = 3
    while i*i <= n:
        while n % i == 0:
            largest_prime = i
            n //= i
        i += 2
    if n > largest_prime:
        largest_prime = n;
    print(largest_prime)
        
    
