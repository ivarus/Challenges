'''
Created on Mar 18, 2015

@author: Ivan Varus
'''

import sys


def minsweeper_gen(field, size):
    m, n = size
    for i in range(m):
        for j in range(n):
            if field[i*n + j] == '.':
                r1 = range(max(0, j-1), min(n, j+2))
                r2 = range(max(0, i-1), min(m, i+2))
                s = sum(field[k*n+l] == '*' for l in r1 for k in r2)
                yield str(s)
            else:
                yield '*'


def minesweeper(field, size):
    return ''.join(minsweeper_gen(field, size))


with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        size, sep, field = test.partition(';')
        print(minesweeper(field, map(int, size.split(','))))
