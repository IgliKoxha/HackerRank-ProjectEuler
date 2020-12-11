#!/bin/python3

import sys
import math


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    
    sq_of_sum = sum(n for n in range(1, n + 1))**2 
    sum_of_sqs = n * (n + 1) * (2 * n + 1) // 6 #Formula to get first n perfect squares
    print(sq_of_sum - sum_of_sqs)
