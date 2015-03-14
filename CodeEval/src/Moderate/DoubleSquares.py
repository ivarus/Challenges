'''
Created on Feb 28, 2015

@author: Ivan Varus
'''

import sys
from math import sqrt


def doubleSquares(n):
    solutions = 0
    x, y = int(sqrt(n)), 0
    sos = x * x
    while x >= y:
        if sos < n:
            sos += 2*y + 1
            y += 1
        elif sos > n:
            sos -= 2*x - 1
            x -= 1
        else:
            solutions += 1
            sos += 2*(y-x + 1)
            y += 1
            x -= 1
    return solutions


test_cases = open(sys.argv[1], 'r')
N = int(next(test_cases))
for i in range(N):
    print(doubleSquares(int(next(test_cases).rstrip())))
test_cases.close()
