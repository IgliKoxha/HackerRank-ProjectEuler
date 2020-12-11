#!/bin/python3

import sys

def fibRec(n):
    if n == 1: return 1
    if n == 2: return 2
    return fibRec(n - 1) + fibRec(n - 2)

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    f1 = 1
    f2 = 2
    nxt = 0
    s = 2
    while True:
        nxt = f1 + f2
        f1 = f2
        f2 = nxt
        if nxt >= n:
            break
        if nxt % 2 == 0:
            s += nxt
    print(s)
    